# 🌫️ 확산 모델(Diffusion Models) 완전 정리

본 문서는 다음 내용을 시스템적으로 정리한다:

- 확산 확률 모델(DPM)
- DDPM (Denoising Diffusion Probabilistic Models)
- DDIM
- Diffusion + GAN
- Distillation 계열
- Consistency Model
- 조건부 확산 모델(Classifier guidance / Classifier-free guidance)

---

# 1. 확산 확률 모델(Diffusion Probabilistic Model, DPM)

## 1.1 확산 모델 개념

확산 모델은 다음 두 가지 과정으로 구성된 생성 모델이다:

1) **정방향 확산 (Forward Diffusion)**  
- 원본 데이터에 점점 노이즈를 주입  
- 끝에서는 거의 순수한 정규분포 노이즈가 됨  
- **학습할 필요 없음 (고정 프로세스)**  
- 마르코프(현재만 의존) 구조

2) **역방향 확산 (Reverse Diffusion)**  
- 노이즈를 조금씩 제거하며 원본 데이터를 복원  
- 이 과정은 **학습 필요**  
- 복잡한 조건부 분포를 근사해야 함

---

## 1.2 정방향 확산

정방향 확산의 수식:

```text
q(x_t | x_{t-1}) = N( sqrt(1 - β_t) x_{t-1}, β_t I )
```

- t = 1 … T (보통 T = 1000)
- βₜ는 점점 증가하는 스케줄
- 많은 작은 잡음 → 최종적으로 x_T ≈ N(0, I)

---

## 1.3 역방향 확산

역방향 분포:

```text
q(x_{t-1} | x_t)
```

하지만 실제 계산 불가능 → 신경망으로 근사:

```text
pθ(x_{t-1} | x_t)
```

- 작은 step일수록 정규분포로 잘 근사됨
- 신경망은 “노이즈를 제거하는 방향”으로 학습됨

---

# 2. 확산 모델의 손실 함수

## 2.1 DPM 손실의 구성

DPM의 전체 손실은 다음 세 가지로 구성된다:

- **L_T** : 마지막 단계가 표준정규분포에 가까운지 검사 (일반적으로 거의 0)
- **L_0** : x₀를 잘 복원하는지 (재구성)
- **L_{t-1}** : t → t-1 노이즈 제거 정확도

각 항은 KL divergence로 표현된다.

---

## 2.2 DDPM(2020)의 등장: 손실 단순화

DDPM의 핵심 인사이트:

- 평균 혹은 샘플을 예측하는 것이 아니라  
  **“t 시점에 더해진 노이즈 ε을 직접 예측”**  
  하는 형태로 손실을 완전히 단순화한 것.

정방향 확산 공식:

```text
x_t = sqrt(alphā_t) x_0 + sqrt(1-alphā_t) ε
```

따라서 ε을 직접 예측하는 loss:

```text
L_simple = E || ε - εθ(x_t, t) ||^2
```

장점:

- 노이즈 예측 문제는 분포 형태가 일정함 → 학습 안정
- 매우 단순한 MSE 형태 → 최적화 용이
- 생성 품질 향상

---

# 3. DDPM 구조

## 3.1 모델 구조

- UNet 기반
- Residual block + Down/Up sampling
- 중간 해상도에서 Self-Attention
- time embedding: Sinusoidal + 두 개의 FC layer

## 3.2 생성 과정

1. x_T ∼ N(0, I) 샘플링
2. t = T, …, 1 반복:
   - εθ(x_t, t)을 예측
   - 아래 식으로 x_{t-1} 생성:

```text
x_{t-1} = 1/sqrt(alpha_t) ( x_t - (β_t/sqrt(1-alphā_t)) εθ ) + σ_t z
(σ_t는 DDPM에서 noise variance)
```

---

# 4. DDPM의 한계

## 4.1 세 가지 한계점

1) 생성 속도 매우 느림  
- 이미지 하나 생성에 1000 스텝 필요

2) 무조건적 모델 (Unconditional)  
- 조건을 반영하는 구조가 원래 없음

3) 품질–다양성 트레이드오프 조절 어려움

---

# 5. DDIM (Denoising Diffusion Implicit Models)

## 5.1 목적

- **학습은 DDPM과 동일하게 유지**
- **생성 과정만 빠르게 (sampling acceleration)**

즉:

- 학습은 1000 step으로 함
- 생성은 100, 50, 20 step만으로도 수행

---

## 5.2 핵심 아이디어

- “마르코프 체인을 만족할 필요가 없다”
- 역방향 확산을 deterministic path로 재구성 가능
- variance(σₜ)를 0으로 줄여서 더 빠르게 생성 가능

DDIM 생성 식은 다음과 같다:

```text
x_{t-1} = sqrt(alphā_{t-1}) x_0 + sqrt(1 - alphā_{t-1}) εθ
```

- x₀는 εθ로 역추정
- 추가적인 노이즈(σ\_t z)를 0으로 설정 → deterministic sampling

---

## 5.3 장점

- 1000 → 20 step으로 생성 속도 획기적 개선
- latent interpolation 가능 (GAN처럼 보간 가능)

---

# 6. Diffusion + GAN : DDGAN

DDPM에서는 t → t-1 분포 q(x_{t-1} | x_t)가  
**정규분포로 충분히 근사 가능한 경우에만 동작이 쉽다.**

t가 0에 가까워질수록 분포는 정규분포보다 훨씬 복잡해짐.

### DDGAN(2022) 아이디어:

- 적은 step (예: T ≤ 8)에서도 학습하기 위해
- GAN을 이용해 q(x_{t-1} | x_t) 를 직접 학습
- Generator: xt → xt−1
- Discriminator: xt, xt−1 분포 진위 판별

장점:

- 매우 빠른 생성 속도 (few-step diffusion)
- DDPM의 안정성 + GAN의 sharpness 결합

---

# 7. Progressive Distillation (2022)

## 7.1 핵심 개념

- teacher diffusion model (1000 steps)
- 한 번 distill → 500 steps 모델
- 다시 distill → 250 steps
- 반복 → 1~16 step refinement 모델

즉:

**“한 번의 역확산을 두 번의 역확산 과정으로 근사하도록 학습”**

장점:

- sampling step 극적 축소
- 품질 유지하면서 속도 향상

---

# 8. Consistency Model (2023)

## 8.1 개념

- “어떤 time step t에서도 결과 x₀가 항상 동일하게 나오도록” 학습
- 시간에 상관없이 같은 output 생성
- 따라서 few-step 또는 1-step generation 가능

## 8.2 Latent Consistency Model

- 개념을 latent space까지 확장
- Stable Diffusion 같은 latent diffusion에서 활용 가능
- 1~8 step ultra fast generation 가능

---

# 9. 조건부 확산 모델 (Conditional Diffusion)

확산 모델은 원래 Unconditional 모델.  
조건을 반영하기 위해 두 가지 방식이 있음:

---

# 9.1 Classifier Guidance (2021)

1) 사전학습된 분류기 pϕ(y | x_t, t) 필요  
2) 분류기의 gradient를 이용해, 모델이 y 클래스 방향으로 이동하도록 유도  
3) scale(s)를 조절하여 조건의 강도 조절 가능

장점:

- 매우 강한 조건부 생성 가능

단점:

- 분류기 추가 학습 필요
- 다양성 감소 (강한 guidance 시 mode collapse 유사 현상 발생)

---

# 9.2 Classifier-Free Guidance (2021)

### 핵심 아이디어:

- **조건부 모델 + 무조건부 모델을 함께 학습**
- 조건을 랜덤 확률(예: 10~20%)로 dropout
- 생성 시 두 모델의 예측을 가중합:

```text
ε_guided = (1+w) ε_conditional - w ε_unconditional
```

- w가 guidance scale  
→ 높을수록 조건 반영 강해지고 품질 높아짐  
→ 낮을수록 다양성 증가

장점:

- 분류기 불필요
- 현재 대부분의 diffusion 모델이 이 구조 사용  
  (Stable Diffusion, Imagen, DALL·E-2 등)

---

# 10. 전체 요약

## (1) 확산 모델 핵심 흐름
- 데이터 → 1000 단계로 노이즈 증가 (정방향)
- 노이즈 → 노이즈 제거하며 데이터 복원 (역방향)
- 학습은 노이즈 예측 MSE

## (2) 주요 모델
- **DDPM**: 기본 구조, 매우 느림  
- **DDIM**: sampling 가속 (1000 → 20 step)  
- **DDGAN**: GAN 결합, few-step 생성  
- **Progressive Distillation**: teacher-to-student로 step 절반씩 축소  
- **Consistency Model**: 1-step 생성까지 가능  

## (3) 조건부 생성
- **Classifier Guidance**: 분류기 필요, 강한 조건  
- **Classifier-Free Guidance**: 분류기 불필요, 가장 널리 사용

## (4) 왜 확산 모델이 대세인가?
- 매우 높은 품질  
- 안정적 학습(GAN 대비)  
- 다중 모드 유지(Diversity 높음)  
- 조건부 생성에서 매우 강력 (텍스트-이미지 등)
