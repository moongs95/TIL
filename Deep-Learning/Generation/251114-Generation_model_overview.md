# 📘 생성모델의 개요 (Generative Models Overview)

---

# 1. 생성 모델이란?

생성 모델(Generative Models)은 **주어진 데이터의 확률분포를 학습하여 새로운 데이터를 생성할 수 있는 모델**이다.

- 데이터 X, 또는 (X, Y)의 **joint / marginal / conditional 분포**를 학습
- 학습한 분포를 기반으로 새로운 샘플 생성 가능
- 데이터가 **저차원의 잠재공간(latent space)**에서 생성되었다는 가정을 활용

---

# 2. 고전 생성 모델 (2013년 이전)

## ■ Gaussian Mixture Model (GMM)
- 여러 개의 정규분포를 혼합해 전체 분포를 근사
- 각 가우시안의 평균·분산·가중치를 조정하여 데이터 히스토그램에 맞춤
- 간단하고 직관적이지만 고차원에서는 비효율적

## ■ Restricted Boltzmann Machine (RBM)
- 에너지 기반 모델(Energy-based Model)
- 볼츠만 분포 기반: 에너지가 낮을수록 확률이 높음
- Contrastive Divergence로 최적화

## ■ Deep Belief Network (DBN)
- RBM을 여러 층으로 쌓아 학습
- 1층씩 순차적으로 학습하며 깊은 구조 구성
- 초기 딥러닝 발전에 중요한 역할을 했으나 현재는 거의 사용되지 않음

## ■ Autoregressive Models
- “현재의 픽셀/값은 이전까지의 값에 의존”
- 마르코프 가정 기반
- PixelRNN, PixelCNN으로 발전

---

# 3. 딥러닝 기반 생성 모델의 등장 (2014년 이후)

AlexNet(2012) 이후 딥러닝이 폭발적으로 발전하며 생성 모델도 급격히 확장됨.  
이 시기 두 가지 모델이 핵심: **VAE · GAN**

---

# 4. Variational Autoencoder (VAE)

## ■ 특징
- 학습 안정적
- 샘플링 빠름
- 잠재공간 조작 용이 (interpolation, latent arithmetic)
- 단점: 생성 이미지가 다소 흐림(blur)

## ■ 발전
- Hierarchical VAE
- Adversarial Autoencoder (AAE)
- VQ-VAE (디스크리트 코드북 사용 → 선명한 생성)
- 대규모 모델의 등장과 함께 고해상도 생성까지 가능해짐

---

# 5. Generative Adversarial Networks (GAN)

## ■ 구조
- Generator(G) vs Discriminator(D)의 적대적 학습
- 분포를 직접 정의하지 않아도 됨
- 매우 선명한(high-fidelity) 이미지 생성 가능

## ■ 문제점
- 학습 불안정
- 모드 붕괴(mode collapse)

## ■ 발전
- DCGAN  
- WGAN / WGAN-GP  
- Progressive GAN  
- StyleGAN, StyleGAN2, StyleGAN3  
  → 라텐트 공간 벡터 연산으로 속성 조작 가능

## ■ 성능
- HD 이미지, 얼굴 생성, 스타일 변환 등에서 뛰어난 성능

---

# 6. Normalizing Flow

- 역변환 가능한 구조로 정확한 likelihood 계산 가능
- 하지만 구조적 제약으로 인해 대규모 이미지 생성 모델로는 덜 사용됨

---

# 7. Diffusion Models (확산 모델)

## ■ 초기(2015)
- 비평형 열역학 기반 아이디어
- 초창기 결과물은 매우 낮은 질 (노이즈 수준)
- GAN/VAE보다 주목도 낮음

## ■ 재부상(2020 이후)
Diffusion 모델 성능이 폭발적으로 향상:

- GAN과 비슷하거나 더 뛰어난 품질
- ImageNet, CIFAR-10에서 최고 수준의 FID/IS 기록
- 안정적 학습

## ■ 발전 & 대중화
- DDPM → DDIM → Improved Diffusion  
- Latent Diffusion → **Stable Diffusion**의 탄생  
- DreamBooth: 3~5장만으로 특정 아이덴티티 생성  
- 다양한 조건부 생성(Text-to-Image, Layout-to-Image 등)에서 강력

---

# 8. 생성 모델의 학습: 최대 가능도 추정(MLE)

생성 모델은 실제 데이터 분포 \(P_\text{data}\)와 모델 분포 \(P_\theta\)를 가깝게 만드는 것이 목적.

## ■ Likelihood & Log-likelihood
관측 데이터 \(x_1, x_2, …\)가 있을 때  
모델의 파라미터 θ를 찾는 방법:

- Likelihood:  
  \( L(\theta) = \prod_i P_\theta(x_i) \)
- Log-likelihood:  
  \( \log L(\theta) = \sum_i \log P_\theta(x_i) \)

최대 가능도 추정(MLE):  
\[
\theta^\* = \arg\max_\theta \sum \log P_\theta(x)
\]

---

# 9. KL Divergence와 생성 모델

## ■ KL Divergence 정의
\[
D_{KL}(P||Q) = \sum P(x) \log \frac{P(x)}{Q(x)}
\]

**특징**
- 항상 0 이상
- 두 분포가 동일하면 0
- 대칭성 없음 → 정식 거리(metric)가 아님  
  그러나 분포 차이를 측정하는 직관적 도구로 활용

## ■ KL 최소화 = Log-likelihood 최대화
수식 전개:

\[
D_{KL}(P||Q_\theta) = \sum P(x)[\log P(x) - \log Q_\theta(x)]
\]

앞 항은 θ와 무관  
→ KL 최소화는 **log-likelihood 최대화**와 동치

## ■ KL의 한계
- KL 계산을 위해 실제 데이터 분포 \(P_\text{data}\)가 필요
- 하지만 우리는 실제 분포를 모르기 때문에 생성 모델을 학습하는 것  
→ **근본적 모순 발생**

따라서 실제 분포 대신 **관측 샘플로 학습하는 다양한 기법**이 필요  
(VAE의 ELBO, GAN의 미니맥스, Diffusion의 노이즈 모델링 등)

---

# 10. 판별 모델 vs 생성 모델

## ■ 판별 모델 (Discriminative)
- \(p(Y|X)\)를 직접 모델링
- 분류, 경계 판단, 이상치 탐지에 적합

## ■ 생성 모델 (Generative)
- \(p(X, Y)\), 또는 \(p(X)\), 또는 \(p(X|Y)\)를 모델링
- 데이터 생성, 복원, 변환에 사용

---

# 11. 생성 모델의 주요 활용 사례

## ■ 이미지/영상
- 초해상도(Super-resolution)
- 사진 복원
- AI 프로필 생성
- Webtoon 자동 채색
- 상품 이미지 생성
- 가상 피팅(virtual try-on)
- 영상 스타일 변환
- Dance transfer
- Lip-sync / AI 더빙
- Text-to-Image (Midjourney, Stable Diffusion)
- Text-to-Video (Runway Gen-2)

## ■ 오디오/음성
- 음성 합성
- 음악 생성
- 비디오-오디오 동기화

## ■ 기타
- Layout-to-Image
- 3D 생성
- X-to-X 변환 전반

---

# 12. 생성 모델의 최근 트렌드 요약

| 모델 | 특징 | 강점 |
|------|-------|--------|
| **VAE** | 확률모델 기반, 잠재공간 구조적 | 빠른 샘플링, 안정적 |
| **GAN** | 적대적 학습 구조 | 매우 선명한 이미지 |
| **Diffusion** | 노이즈 제거 과정 기반 | 현재 가장 강력한 품질/안정성 |
| **Autoregressive** | 순차 생성 | 텍스트·오디오에서 최강 (GPT 등) |

---

# 13. 결론

생성 모델은  
통계적 모델(GMM) → 에너지 기반 모델(RBM/DBN) → VAE/GAN → Diffusion  
으로 **지속적으로 발전**해왔다.

오늘날 생성 모델은 이미지·영상·음성·3D·텍스트 등 다양한 분야의 핵심 기술이며,  
AI 서비스 구현 및 연구에서 필수적인 영역으로 자리 잡았다.


