# Multilingual LLM (다국어 대규모 언어 모델)

## 1. Multilingual PLMs (다국어 사전학습 모델)

### 초기 다국어 모델

**발전 방향**:
- 초기 사전학습 모델에서 다국어 모델을 만드려는 노력
- **Only-encoder** 혹은 **Encoder-decoder**에서 주로 이루어짐

---

#### Only-Encoder 모델

**목적**:
- **"동일한 공간(space)에 언어적 정보를 매핑"**
- 언어적 자원이 없는 **"소수 언어(Low-resource Language)"**에서 적은 양의 데이터로 좋은 분류 성능을 내기 위함

---

#### Encoder-Decoder 모델

**목적**:
- 주로 **"번역"**을 위해서 사전학습 진행
- 언어적 자원이 없는 **"소수 언어"**에서의 번역 모델을 만들기 위함

---

### 단일 모델 vs 다국어 모델

**이전 상황**:
- 대부분 **단일 모델(Monolingual model)**의 성능이 좋았음

**현재 상황**:
- **모델과 데이터의 사이즈가 커질수록 그 격차는 줄어듦**

**의미**:
- ⇒ **충분한 데이터와 모델 크기로 언어의 공통적 특성을 배울 수 있음을 암시**

---

### 대표적인 다국어 모델

- **mBERT** (Multilingual BERT)
- **XLM** (Cross-lingual Language Model)
  - TLM이 언어의 중립적 특징을 학습함
- **MASS**
- **mBART** (Multilingual BART)
- **mT5** (Multilingual T5)

---

## 2. LLMs의 다양한 변화

### 주요 변화 방향

1. **Multilingual LLMs** (다국어 LLMs)
2. **Multimodal LLMs** (멀티모달 LLMs)
   - Image-Language (이미지-언어)
   - Audio-Language (오디오-언어)
   - Image-Audio-Language (이미지-오디오-언어)
   - Video-Language (비디오-언어)
3. **Cross-lingual LLMs** (언어 간 전이 LLMs)

---

## 3. Multilingual Large Language Models

### 3.1 Multilingual LLM의 중요성

#### 현재 상황

**긍정적 측면**:
- LLM의 등장으로 다양한 연구 및 기술 개발, 글로벌화 추진

**문제점**:
1. **대부분의 LLM은 소수의 주요 언어에 집중**
2. **여러 언어에 대한 지원이 부족**
   - 다양한 언어를 사용하는 사람들이 기술 접근에 어려움을 겪음
   - **비영어권 나라는 LLM의 불모지**
3. **많은 LLM이 다국어 코퍼스를 사용하고 있으나, 언어에 집중된 데이터로 인해 다른 언어로 사용이 불가**

---

#### 주요 언어 중심 LLM

**대표 모델**:
- PaLM
- LLaMA
- LLaMA2
- Alpaca
- Falcon
- RedPajama

**특징**:
- 대부분의 LLM은 **영어권 혹은 중국어, 인도어**에서만 사용 가능

---

#### LLaMA-2 70B의 한계 사례

**문제**:
```
한국어로 답변을 원해도:
- 영어로 답변함
- 이상한 답변 출력
```

---

### 3.2 다국어 답변이 뛰어난 Multilingual LLM

**대표 모델**:
- **PolyLM**
- **BLOOM**
- **PaLM2**
- **GPT-3.5 / GPT-4** (OpenAI)

**특징**:
- **'한국어', '일본어' 및 10개 언어 이상에도 무난하게 잘 사용할 수 있음**

---

### 3.3 Multilingual LLM Benchmark

#### 기존 평가의 문제점

**문제 1: 영어 중심 평가**
```
대부분의 LLM들의 성능 평가는 "영어"에서만 진행
→ 다국어 능력에 대해 평가하는 것에 한계
```

**문제 2: 벤치마크의 부재**
```
이전 Multilingual LLMs들의 성능 평가:
- "번역"과 같은 한정적인 다국어 성능만 보고
```

---

#### 최근 변화

**LLM 등장 이후**:
- **생성형 모델에서 다국어 생성 능력을 평가하는 다양한 벤치마크 등장**

**대표 벤치마크**:
- **LASER** (Meta)
- **Flores**
- **WikiMatrix**
- **CCMatrix**
- **Flores-101**
- **Flores-200**
- **NLLB 200**
- **MEGA**

---

# Multimodal LLM (멀티모달 대규모 언어 모델)

## 1. Multimodal PLMs

### 1.1 Multimodal이란?

**정의**:
- **여러 데이터 형태(이미지, 텍스트, 오디오, 비디오 등)를 처리할 수 있는 사전학습 모델**

---

#### 주요 유형

**1. Image-Text Multimodal (이미지-텍스트 멀티모달)**
```
이미지와 텍스트 데이터를 모두 처리할 수 있는 모델
```

**2. Audio-Text Multimodal (오디오-텍스트 멀티모달)**
```
오디오 신호와 텍스트를 모두 처리할 수 있는 모델
```

**3. Video-Text Multimodal (비디오-텍스트 멀티모달)**
```
비디오와 텍스트를 모두 처리할 수 있는 모델
```

---

### 1.2 Image-Text Multimodal

#### 정의
- **이미지와 텍스트 데이터를 모두 처리할 수 있는 모델**

---

#### 대표적인 Task

1. **Image2Text Retrieval** (이미지→텍스트 검색)
2. **Text2Image Retrieval** (텍스트→이미지 검색)
3. **Visual Question Answering (VQA)** (시각적 질의응답)
4. **Visual Question Generation (VQG)** (시각적 질문 생성)
5. **Image Captioning** (이미지 캡셔닝)
6. **Optical Character Recognition (OCR)** (광학 문자 인식)
7. **Multimodal Translation** (멀티모달 번역)

---

### 배경지식: Classification 유형

#### Coarse-grained Classification (거친 분류)
```
정의: 큰 범위를 분류하는 일반적인 분류 문제
예시: 개, 고양이
```

#### Fine-grained Classification (세밀한 분류)
```
정의: Coarse-grained에 비해 상대적으로 비슷한 특징들을 더 세밀하게 분류하는 컴퓨터비전 과제
예시: 개의 품종 구분 (진돗개, 시바견, 웰시코기 등)
```

---

### 배경지식: ViT (Vision Transformer)

#### Pre-training (사전학습)

**방법**:
1. **이미지를 더 작은 단위인 패치(patch)로 나눔**
2. Transformer 구조에 사전학습
3. **6억 개의 이미지와 텍스트 쌍으로 사전학습 진행**

**학습 방식**:
- Class를 예측하는 supervision으로 학습
- **BERT의 [CLS] token 역할을 하는 class token을 추가**
- MLP layer를 classification loss로 학습

---

#### Fine-tuning (미세조정)

**방법**:
1. Pre-train 단계에서 사용한 MLP layer를 제거
2. Fine-tuning에 해당하는 MLP layer를 새로 학습

---

### CLIP (Contrastive Language-Image Pre-training)

#### Motivation (동기)

**문제점**:
```
ViT, ResNet 등:
- 이미지 class별 representation learning을 진행
- 다른 task에 적응할 때마다 데이터와 Fine-tuning 필수
- Zero-shot 불가
```

**해결책**:
```
⇒ Image와 Text의 공통된 Multi-modal Embedding Space를 학습
```

---

#### 1. Contrastive Pre-training (대조 사전학습)

**방법**:
- **이미지와 텍스트를 jointly learning (공동 학습)**
- 이미지와 텍스트를 같은 Space에 사상(mapping)
- **Contrastive learning을 통해 CE loss를 사용하여 학습**

**모델 구조**:
- **Image Encoder**: ResNet 혹은 ViT 사용
- **Text Encoder**: GPT-2 구조 사용 (사전학습 모델 사용 X)

**학습 데이터**:
- Pre-train 시 **4억 개의 image with caption**을 사용하여 학습

**Contrastive Learning 방식**:
```
N개의 (이미지, 텍스트) 쌍:
- N개의 positive pair
- N² - N개의 negative pair

목표:
- Positive pair에서 cosine-similarity 최대화
- Negative pair에서 cosine-similarity 최소화
```

---

#### 2. Zero-shot Transfer - 이미지 분류

**방법**:
1. **Class label을 text prompt로 변경**
2. 주어진 이미지와 가장 유사한 텍스트를 Cosine similarity를 통해 선택

**Text prompt 예시**:
```
"a photo of {label}"
```

---

#### Zero-shot 추론 결과

**약점**:
- **간단한 Coarse-grained 분류에 약함**
- 간단한 MNIST 등의 Coarse-grained에서 ResNet 50보다 성능이 낮음

**강점**:
- **어려운 Fine-grained에서는 높은 성능**

---

### FILIP (Fine-grained Interactive Language-Image Pre-Training)

#### Motivation (동기)

**CLIP의 한계**:
```
CLIP: 이미지 전체와 텍스트 전체 사이의 Similarity를 반영 (1:1)
```

**FILIP의 개선**:
```
Patch와 token 사이의 similarity를 반영해서 학습하면 더 정확한 사전학습 가능
(patch : token)
```

---

#### Zero-shot 성능 (vs CLIP)

**이미지 분류**:
- CLIP 대비 대부분 **높은 성능**

**이미지-텍스트 검색**:
- **아주 높은 성능**

---

#### 이미지 패치와 텍스트 프롬프트 사이의 Align 비교

**CLIP**:
- 주어진 프롬프트와 어울리는 이미지 패치를 찾지 못함

**FILIP**:
- **주어진 프롬프트와 어울리는 이미지 패치를 비교적 잘 찾음**

---

### BLIP (Bootstrapping Language-Image Pre-training)

#### 특징
- **Vision-Text Multimodal**
- **기존 Vision-Text Multimodal에서 사용한 웹 데이터의 노이즈를 CapFilt 구조로 해결**

---

#### 세 가지 Loss

**1. Image-Text Contrastive Loss**
```
CLIP과 동일한 방식
```

**2. Language Modeling Loss**
```
방법: 이미지를 통해 텍스트를 생성하도록 학습
- Cross Attention을 통해 이미지 캡션 생성
```

**3. Image-Text Matching Loss**
```
방법: 이미지, 텍스트 쌍이 매칭이 잘 되었는지 예측하는 학습을 진행
```

---

#### CapFilt

**목적**:
- **웹 데이터의 캡션 노이즈를 제거**

**방법**:
1. 사람이 제작한 이미지, 텍스트 쌍으로 Seq2seq 학습
2. 학습한 모델로 웹 이미지 새로 Captioning 진행

---

#### 모델 구조

**Image Encoder**:
- ViT

**Text Encoder**:
- 사전학습된 BERT 사용

---

### 1.3 Other Multimodals (기타 멀티모달)

#### Audio-Text Multimodal (오디오-텍스트 멀티모달)

**대표적인 Task**:
- **Speech-to-Text (STT, 음성인식)**
- **Text-to-Speech (TTS, 음성합성)**

---

#### Video-Text Multimodal (비디오-텍스트 멀티모달)

**대표적인 Task**:
- **Video Captioning (비디오 캡셔닝)**
- **Video Question Answering (비디오 질의응답)**

---

#### 대표 모델

- **Whisper** (Audio-Text)
- **VideoCLIP** (Video-Text)

---

## 2. Multimodal LLMs

### 멀티모달 대규모 언어 모델

**대표 모델**:
- **Flamingo**
- **BLIP-2**
- **LLaVA** (Language and Vision Assistant)
- **Gemini** (Google)

---

# Cross-Lingual LLM (언어 간 전이 LLM)

## 1. Cross-lingual LLM 학습 전략

### 1.1 간단한 전이학습 방법

**세 가지 기본 방법**:
1. **Instruction Tuning**: 목표 언어에 대한 Instruction Tuning만 진행
2. **Further Pre-training**: 목표 언어에 대해 사전학습을 우선 진행
3. **Vocabulary Extension**: 목표 언어에 대한 토큰을 Vocabulary에 추가

---

#### Instruction Tuning (지시어 튜닝)

**정의**:
- **사전학습된 LLM**에 **목표 언어**에 대한 **Instruction Tuning을 진행**하는 방법

**방법**:
- 소스 언어로 학습된 모델이 목표 언어에 대한 Instruction Tuning 데이터를 학습
- 목표 언어에 대한 이해를 높이는 방법

---

**조건**:
```
1. 사전학습을 진행할 LLM이 목표 언어에 대해 낮은 OOV(Out of Vocabulary) rate의 vocabulary를 가지고 있어야 함
2. 소스 언어와 목표 언어의 유사도가 높아야 함
```

**장점**:
- ✅ Instruction Data만으로 손쉽게 학습 가능

**단점**:
- ❌ 성능이 낮을 수 있음

---

#### Vocabulary Extension (어휘 확장)

**정의**:
- **기존 Vocabulary에 목표 언어에 대한 토큰들을 추가하여 확장된 임베딩을 사용**하는 방법

**배경**:
```
문제점:
- 대부분의 LLM의 Vocabulary는 영어에 대해 학습된 Subword Embeddings을 가지고 있음
- 몇몇 LLM은 특정 언어에 대해 OOV Rate가 굉장히 높음

해결책:
- 모델에 대한 언어의 이해도를 높이기 위해, 목표 언어에 대한 토큰들을 추가
```

**방법**:
- **새로운 토큰 임베딩에 대한 학습을 위해, 추가적으로 Further Pre-training 혹은 Instruction Tuning을 진행**

---

**조건**:
```
무작위로 초기화된 토큰 임베딩을 학습하기 위하여 추가적인 Further Pre-training 혹은 Instruction Tuning이 필요
```

**장점**:
- ✅ 목표 언어에 대한 토큰 임베딩 구축으로, 모델의 능력 향상을 기대할 수 있음

**단점**:
- ❌ 목표 언어에 대해 잘 구축된 Vocabulary 필요
- ❌ 무작위로 초기화된 Vocabulary 학습을 위해 추가적인 학습 시간 소요

---

#### Further Pre-training (추가 사전학습)

**정의**:
- **기존 사전학습된 LLM을 다른 언어로 추가 사전학습하는 방법**

**배경**:
```
상황: 대부분의 LLM은 영어에 대해 사전학습되어 있음
```

**방법**:
1. **목표 언어에 대해 추가적인 사전학습을 진행**
2. 목표 언어에 대한 이해를 높임
3. 추가 사전학습된 LLM에 **Instruction Tuning을 진행**
4. 다른 언어에 대한 사전학습 모델을 획득

---

**조건**:
```
사전학습을 진행할 LLM이 목표 언어에 대해 낮은 OOV의 vocabulary를 가지고 있어야 함
```

**장점**:
- ✅ 목표 언어에 대한 지식을 풍부히 갖춘 LLM을 얻을 수 있음

**단점**:
- ❌ 사전학습 코퍼스 구축, 사전학습 등의 자원 소모 심함

---

### 1.2 모델 및 임베딩 학습 기반 방법

#### AMM (Adapting Monolingual Model)

**정의**:
- **목표 언어의 임베딩 레이어로 변환 후 임베딩만 Further Pre-training을 진행**

---

#### XPT (Cross-Lingual Post-Training)

**Phase 1: 언어적 차이를 이해하기 위한 학습**

**목적**:
- 기존 소스 모델로부터 **언어적 차이를 이해**하기 위한 학습 과정

**방법**:
1. 사전학습된 모델에 **ITL (Implicit Translation Layer)** 삽입
   - 언어적 차이를 학습하는 레이어
2. 소스 언어의 임베딩을 **목표 언어의 임베딩으로 교체**
3. **ITL 및 교체된 임베딩만 Further Pre-training 진행**
   - 기존 모델의 레이어는 학습하지 않음

---

**Phase 2: 완전한 목표 언어 모델로 전이**

**목적**:
- 기존 소스 모델을 완전한 목표 언어 모델로 전이하기 위한 학습 과정

**방법**:
1. 기존 모델을 포함한, ITL과 임베딩 레이어 **모두 목표 언어에 대해 Further Pre-training 수행**
2. 이 과정에서 **소스 언어 모델은 완전한 목표 언어 모델로 전이**

---

#### GPT-recycle

**정의**:
- **토큰 임베딩 초기화를 AMM과 같이 무작위 초기화를 진행하는 것이 아닌, 잘 학습된 다른 언어모델의 임베딩을 사용하는 방법**

**방법**:
- 임베딩 레이어의 차원이 맞지 않을 경우
- **Least-squares regression으로 차원 확장**

---

### 1.3 임베딩 정렬 기반 학습 전략

#### 임베딩 정렬 기반 학습 전략

**정의**:
- 토큰 임베딩을 무작위로 목표 언어에 대해 초기화하여 사용하는 대신
- **소스 언어와 목표 언어에 대한 토큰 임베딩을 유사도 기반으로 계산**
- **초기 정렬 후에 학습하는 방법**

---

#### WECHSEL (Word Embeddings Can Help initialize Subword Embeddings in a new Language)

**개념**:
- **기존 사전학습된 서브워드 임베딩과 목표 언어의 서브워드 임베딩을 계산하여 임베딩을 초기화**
- 이후 Further Pre-training을 진행

---

**6단계 프로세스**:

**1) 모델 파라미터 복사 및 토크나이저 교체**
```
- 영어 모델의 내부(임베딩이 아닌) 파라미터를 복사
- 토크나이저를 목표 언어의 토크나이저로 교체
```

**2) 양방향 단어 임베딩 사용**
```
- 영어와 목표 언어를 포함하는 다국어 단어 임베딩을 사용
- 영어 토큰과 의미적으로 유사한 목표 언어 토큰의 임베딩을 초기화
```

**3) 서브워드 임베딩 계산**
```
- 서브워드에 등장하는 n-gram의 임베딩을 합산
- Subword들의 임베딩을 계산
```

**4) 서브워드 유사성 계산**
```
- 계산된 목표 언어의 임베딩을 바탕으로
- 소스 언어와 목표 언어의 서브워드 임베딩 간 유사성을 계산
```

**5) 유사성 기반으로 목표 언어 서브워드 임베딩 초기화**
```
- 계산된 유사성을 기반으로
- 가장 유사한 k개의 소스 언어 임베딩의 가중 평균을 사용
- 목표 언어의 서브워드 임베딩을 초기화
```

**6) Further Pre-training**
```
- 초기화된 모델을 대상 언어 데이터셋에서 추가로 학습
- Freeze 없이 전체 학습
```

---

### 1.4 Adapter 기반 학습 방법

#### Adapter 기반 학습 방법

**정의**:
- **LoRA, QLoRA, Prefix-tuning, P-Tuning 등의 Adapter 기반의 학습 방법**
- 모두 **특정 Parameter만 학습**

**특징**:
- **기존 모델의 언어적 특징을 유지**하기 때문에
- **Cross-lingual 학습 방법으로 취급됨**

---

## 전체 요약

### Multilingual LLM 핵심 요약

| 구분 | 내용 |
|------|------|
| **초기 모델** | mBERT, XLM, MASS, mBART, mT5 |
| **문제점** | 영어 중심, 소수 언어 지원 부족 |
| **우수 모델** | PolyLM, BLOOM, PaLM2, GPT-4 |
| **벤치마크** | LASER, Flores-200, NLLB 200 |

---

### Multimodal LLM 핵심 요약

#### Vision-Language 모델 비교

| 모델 | 특징 | 강점 | 약점 |
|------|------|------|------|
| **ViT** | 패치 기반 Transformer | 이미지 분류 우수 | Zero-shot 불가 |
| **CLIP** | Contrastive Learning | Zero-shot 가능, Fine-grained 우수 | Coarse-grained 약함 |
| **FILIP** | Patch-Token Alignment | CLIP 대비 높은 성능 | - |
| **BLIP** | 3가지 Loss + CapFilt | 노이즈 제거 | - |

---

### Cross-Lingual 학습 전략 비교

| 방법 | 학습 대상 | 장점 | 단점 | 자원 소모 |
|------|----------|------|------|----------|
| **Instruction Tuning** | 전체 모델 | 간단함 | 성능 낮음 | 낮음 |
| **Vocabulary Extension** | 새 토큰 임베딩 | 능력 향상 | 추가 학습 필요 | 중간 |
| **Further Pre-training** | 전체 모델 | 풍부한 지식 | 자원 소모 큼 | 높음 |
| **AMM** | 임베딩만 | 효율적 | - | 중간 |
| **XPT** | ITL + 임베딩 → 전체 | 점진적 전이 | 복잡함 | 중간 |
| **WECHSEL** | 정렬된 임베딩 | 효율적 초기화 | 복잡함 | 중간 |
| **Adapter-based** | 일부 파라미터 | 언어 특징 유지 | - | 낮음 |

---

### 학습 전략 선택 가이드
```
자원이 적을 때:
→ Instruction Tuning or Adapter-based

중간 자원:
→ Vocabulary Extension or WECHSEL

자원이 충분할 때:
→ Further Pre-training or XPT

언어 유사도가 높을 때:
→ Instruction Tuning

언어 유사도가 낮을 때:
→ Further Pre-training
```

---

## 주요 개념 정리

### Multilingual (다국어)
```
정의: 여러 언어를 지원하는 모델
목적: 언어 간 공통 특성 학습, 소수 언어 지원
```

### Multimodal (멀티모달)
```
정의: 여러 데이터 형태(이미지, 텍스트, 오디오, 비디오)를 처리하는 모델
목적: 서로 다른 모달리티 간의 공통 표현 학습
```

### Cross-lingual (언어 간 전이)
```
정의: 한 언어로 학습된 모델을 다른 언어로 전이하는 방법
목적: 자원이 풍부한 언어의 지식을 소수 언어로 전이
```

---

## 기술적 개념 정리

### OOV (Out of Vocabulary)
```
정의: 어휘에 없는 단어
의미: OOV rate가 높으면 모델이 해당 언어를 잘 처리하지 못함
```

### Contrastive Learning (대조 학습)
```
정의: Positive pair는 가깝게, Negative pair는 멀게 학습
적용: CLIP, FILIP 등에서 사용
```

### Zero-shot
```
정의: 학습하지 않은 Task를 예시 없이 수행
조건: 공통 표현 공간(Common Embedding Space) 필요
```

### ITL (Implicit Translation Layer)
```
정의: 언어 간 차이를 학습하는 레이어
목적: 소스 언어와 목표 언어 간의 변환 학습
```

---

## 연구 트렌드

### Multilingual LLM
```
과거: 영어 중심, 번역만 평가
현재: 10개 이상 언어 지원, 생성 능력 평가
미래: 모든 언어 지원, 언어 중립적 특성 학습
```

### Multimodal LLM
```
과거: Image-Text만
현재: Image-Audio-Video-Text 통합
미래: 완전한 멀티모달 이해 및 생성
```

### Cross-lingual Transfer
```
과거: 단순 번역
현재: 효율적인 전이 학습 방법 개발
미래: 자동화된 언어 적응
```

---

## 핵심 Takeaway
```
🌍 Multilingual: 모든 언어를 위한 LLM

👁️ Multimodal: 모든 데이터 형태를 이해하는 LLM

🔄 Cross-lingual: 효율적인 언어 전이 방법

📊 평가: 영어 중심에서 벗어나 다양한 언어와 모달리티 평가

🚀 미래: 진정한 범용 AI를 향해
```

---

## 실전 활용 가이드

### Multilingual 모델 선택
```
영어만: GPT-4, Claude
영어 + 중국어: PaLM2
다국어 (10개 이상): BLOOM, PolyLM
```

### Multimodal 모델 선택
```
Image-Text: CLIP, BLIP-2
Audio-Text: Whisper
Video-Text: VideoCLIP
통합: Gemini, GPT-4V
```

### Cross-lingual 전략 선택
```
빠른 적응: Instruction Tuning
최고 성능: Further Pre-training
중간 방법: Vocabulary Extension + WECHSEL
```
