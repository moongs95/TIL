# 🌌 잠재 확산 모델(Latent Diffusion Model, LDM) & 개인화 기법 완전 정리

본 문서는 다음 주제를 모두 포함한다:

- 고해상도 생성의 어려움과 잠재 공간의 필요성
- LDM(Stable Diffusion)의 전체 구조
- VQ-GAN 기반 잠재공간 학습
- Text-to-Image 구조 (CLIP, Cross-Attention)
- X-to-Image 응용
- 개인화(Personalization) 기법: Textual Inversion, DreamBooth, LoRA, ControlNet, IP-Adapter 등

---

# 1. 잠재 공간의 필요성

## 1.1 고해상도 이미지 생성의 어려움

고해상도 이미지 생성은 다음 문제를 가진다:

- 이미지 크기(H, W, C)가 커질수록 연산량이 기하급수적으로 증가
- 확산 모델은 1000 step 이상 반복해야 하므로 추론 시간이 매우 길다
- 자원 낭비(비용/에너지)가 크며 연구·서비스 접근성이 낮음
- 아주 미세한 픽셀 단위까지 모델이 계산하므로 **불필요한 영역에도 많은 자원을 소모**

→ **이미지 공간이 아니라 더 압축된 “잠재 공간”에서 연산하면 효율이 크게 개선될 수 있음**

---

## 1.2 픽셀 공간 vs. 잠재 공간

### ● 픽셀 공간 특징
- 고차원
- 불필요한 세부 정보가 많음
- 확산 단계 1,000 step을 모두 이 공간에서 계산 → 비효율적

### ● 잠재 공간 특징
- 오토인코더(VAE/VQ-GAN)를 사용해 **의미적으로 중요한 정보만 압축**
- 고해상도 이미지도 낮은 차원의 feature map으로 변환
- 구조/형태 같은 핵심 정보는 유지하지만 미세한 디테일(노이즈 수준)은 제거

### ● 인지적 압축 / 의미적 압축

- **인지적 압축**: 사람의 인지에 큰 영향을 주지 않는 세부 픽셀을 버리고 본질적 요소만 남김  
- **의미적 압축**: 사물의 형태, 구조, 의미를 보존하는 방식으로 표현

→ 잠재 확산 모델(LDM)은 이 잠재공간에서 확산을 수행하여 **연산량을 10~40배 감소**시키며 **동시에 품질은 유지**한다.

---

# 2. 잠재 확산 모델(LDM)

Stable Diffusion의 기반 모델이 바로 LDM(Latent Diffusion Model).

## 2.1 LDM 구조 개요

LDM은 다음 순서대로 작동한다:

1. **이미지 → 잠재 표현 z**
   - 오토인코더(특히 VQ-GAN)의 Encoder가 이미지의 의미적 정보를 추출하여 z 생성

2. **잠재공간(z)에서 확산 모델 훈련**
   - DDPM/UNet이 z에 노이즈 주입/제거 학습
   - “픽셀이 아니라 feature map을 확산시키는 것”

3. **z → 이미지 복원**
   - 학습된 디코더가 z를 고해상도 이미지로 재구성

즉:

Image → Encoder → z → Diffusion Model → ẑ → Decoder → Generated Image


잠재 공간은 이미지보다 훨씬 작으므로  
**학습 비용, 추론 비용, VRAM을 대폭 절약한다.**

---

## 2.2 LDM 학습 단계

### 1단계: 잠재공간 학습 (VQ-GAN 기반 Autoencoder)

- 이미지 ↔ 재구성 이미지가 최대한 비슷하도록 Encoder/Decoder 훈련
- 단순 L2 손실이 아니라 **Patch 단위 Discriminator**를 포함해 고해상도 표현 유지
- 재구성 품질이 좋을수록 확산 모델이 의미적 정보에 집중 가능

### 2단계: 잠재 확산 모델 학습

- 이미지가 아니라 **잠재 z에 노이즈를 주입하고 제거**
- DDPM과 동일하게 **노이즈 ε 예측 방식**으로 학습
- UNet 구조 + 시간 임베딩 + (조건부 생성의 경우) Cross-Attention 사용

장점:

- 픽셀 공간 확산보다 10~20배 빠른 훈련/추론
- 고해상도(512×512 이상) 이미지 생성 가능

---

# 3. Text-to-Image (Stable Diffusion 구조)

## 3.1 전체 구성도

Stable Diffusion은 다음 3개의 주요 모듈로 구성:

1) **VAE Encoder/Decoder**  
   - 이미지를 잠재공간 z로 압축/복원

2) **UNet 기반 확산 모델**  
   - z + noise + time embedding → noise 예측

3) **텍스트 인코더(CLIP)**  
   - 입력 텍스트를 벡터 시퀀스로 변환

---

## 3.2 텍스트 인코딩: CLIP 활용

- CLIP은 이미지-텍스트 쌍을 사용해 대조학습으로 훈련된 모델
- 텍스트의 의미적 표현을 매우 잘 추출
- Stable Diffusion은 CLIP의 텍스트 인코더를 그대로 사용해 문장을 embedding vector로 만들고  
  **Cross-Attention으로 UNet에 주입**

---

## 3.3 Cross-Attention

이미지 feature-map ↔ 텍스트 토큰 간의 의미적 연결을 학습하는 구조.

특징:

- 텍스트-잠재표현(z)의 상관성을 학습
- 예: “a cat sitting on a chair”  
  → 고양이에 해당하는 feature를 강조하고 chair 부분은 별도 영역으로 매핑됨

Cross-attention이 Text-to-Image 성능을 결정짓는 핵심 요소.

---

## 3.4 X-to-Image 응용

LDM은 텍스트 외에도 다양한 조건 입력을 수용할 수 있다.

### ● Layout-to-Image  
- 레이아웃(객체 위치)을 조건으로 이미지 생성

### ● Masked-to-Image (Inpainting)  
- 특정 영역을 마스크로 가리고, 그 부분을 자연스럽게 재생성

### ● Depth / Edge / Pose / Sketch 등  
- ControlNet과 결합 시 더욱 정교한 X-to-Image 생성 가능

---

# 4. 개인화(Personalization)

Stable Diffusion이 발전한 핵심 이유 중 하나는 **매우 소량(5~15장)**의 데이터로  
개인을 위한 생성이 가능하다는 점.

개인화 기법 총정리:

---

# 4.1 Textual Inversion (2022)

핵심 개념:

- 새로운 단어(S\*) 하나를 만들어  
  **그 단어가 특정 사람/스타일/객체를 의미하도록 Embedding을 학습**
- Text Encoder는 고정 → **오직 새로운 토큰 임베딩만 업데이트**
- 데이터 3~5장만으로도 가능

학습 방식:

“a photo of S*” → 생성 이미지가 내가 넣은 사진과 최대한 유사하도록 임베딩 v* 업데이트

특징:

- 간단하고 안전한 방식
- 새로운 단어 하나만 학습하므로 모델 전체를 변경하지 않음
- 스타일/질감/특정 대상 학습에 적합

---

# 4.2 DreamBooth (2022)

Textual Inversion보다 훨씬 강력한 개인화.

핵심 개념:

- 사전학습된 UNet 전체를 **미세 조정(Fine-tuning)**
- 입력 텍스트는 반드시 “[식별자] [클래스]” 형태 사용  
  예: “sks dog”, “xtp person”

필요한 요소:

1) **Reconstruction Loss**:  
   “[식별자] [클래스]”로 모델이 정확히 이미지를 재현하도록 훈련

2) **Prior Preservation Loss**:  
   해당 클래스(dog/person 등)의 기본 다양성을 잃지 않도록  
   모델의 기존 클래스를 유지하는 정규화 역할

장단점:

- ✔ 매우 높은 품질
- ✔ 자세/포즈/색감까지 완벽히 재현  
- ✘ 과적합 위험 (5장 이하 데이터에서 특히)
- ✘ 모델 전체 업데이트로 용량 증가

---

# 4.3 LoRA (Low-Rank Adaptation, 2021)

현재 가장 많이 사용되는 개인화/파인튜닝 방식.

핵심 개념:

- 기존 모델 가중치는 그대로 두고  
  **변화량 ΔW만을 매우 작은 저랭크 행렬 2개로 분해해 학습**

W' = W + BA (rank r 매우 작음)

장점:

- 파라미터 수 10,000 → 수백 단위로 감소
- GPU 메모리 매우 적게 사용
- 기존 모델을 훼손하지 않고 개인화 가능
- DreamBooth와 함께 사용 시 시너지 큼

필요 데이터: 약 10~15장

---

# 4.4 ControlNet (2023)

구조적 입력(Edge, Depth, Pose, SCRIBBLE 등)을 조건으로 추가할 수 있는 기법.

핵심 개념:

- UNet의 main weight는 고정(Frozen)
- **ControlNet 전용 branch**를 학습하여  
  조건 정보를 안정적으로 주입

장점:

- 자세, 구도, 윤곽, 시선 방향 등 구조를 강제 가능
- Text-to-Image의 한계를 완벽 보완

---

# 4.5 Face0 (2023)

- 얼굴만을 위한 고정밀 개인화 모델
- 얼굴 특징 벡터 + 텍스트 정도만 넣어도 동일 인물 생성 가능
- 대규모 얼굴 학습 데이터 필요

---

# 4.6 IP-Adapter (2023)

이미지 조건을 직접 모델에 주입하는 기법.

- Text + Image feature 결합
- Cross-attention을 확장한 구조
- 얼굴/스타일/객체의 특징을 지도처럼 제공 가능
- ControlNet과도 병합 가능

---

# 4.7 Imagic (2023)

텍스트 기반 의미적 이미지 편집 방법.

- 입력 이미지 + 텍스트 프롬프트  
- 텍스트를 점진적으로 변화시키면서 의미적 편집 수행  
  (색, 형태, 분위기, 질감 등을 바꾸는 작업)

---

# 4.8 Perfusion (2023)

- 매우 작은 모델 크기
- Attention의 Key 쪽을 조절하여 여러 객체를 동시에 개인화 가능
- 빠르고 가벼운 개인화 기법 중 하나

---

# 5. 전체 요약

## ● Latent Diffusion Model(LDM)
- 고해상도 이미지 생성의 연산 비용을 획기적으로 낮춘 모델
- 픽셀 대신 잠재공간에서 확산을 수행
- VQ-GAN 오토인코더로 의미 압축된 공간을 사용
- Stable Diffusion의 핵심 기반 기술

## ● Text-to-Image의 핵심 구성
- CLIP 텍스트 인코더
- Cross-Attention
- Latent UNet Diffusion

## ● X-to-Image 다양화
- Layout-to-Image  
- Inpainting  
- Edge/Depth/Pose 기반 생성(ControlNet)

## ● 개인화(Personalization)
- **Textual Inversion**: 단어 임베딩만 학습  
- **DreamBooth**: UNet 전체 미세 조정  
- **LoRA**: 변화량만 학습하는 초경량 파인튜닝  
- **ControlNet/IP-Adapter**: 구조·이미지 기반 조건 생성  
- **Perfusion/Face0/Imagic**: 고급 개인화 기술들
