# 📘 생성 모델 평가 지표의 필요성 및 주요 지표 정리

---

# 1. 생성 모델 평가 지표의 필요성

## 1.1 판별 모델의 평가 지표

판별 모델은 **정답(Ground Truth)**가 존재하므로 평가가 쉽다.

### ■ 분류(Classification)
- Accuracy 사용
- 클래스 불균형 시 Accuracy 부적합 → Precision / Recall / F1-score 사용

### ■ 회귀(Regression)
- MSE(평균 제곱 오차)  
- MAE(평균 절대 오차)  
- 값 범위에 민감할 경우: R², 상관계수 등 사용

---

## 1.2 생성 모델 평가의 어려움

생성 모델은 **정답이 없기 때문에** 평가가 어렵다.

### ■ 주요 어려움
- GT가 없어 직접 비교 불가
- 훈련 데이터를 정답으로 쓰면 “복제”(overfitting) 위험
- 사람 판단이 개입 → 주관성 문제
- AMT 등을 통한 인간 평가 비용·시간 소모
- **객관적인 지표 필요**

### ■ 평가 기준
- **품질(Fidelity)**
- **다양성(Diversity)**

### ■ 대표 평가 지표
- Inception Score (IS)
- Fréchet Inception Distance (FID)
- Improved Precision & Recall
- Conditional Accuracy
- LPIPS
- CLIP Score

---

# 2. Inception Score (IS)

## 2.1 IS의 목적
- 이미지 **예리함(Sharpness)**  
- 이미지 **다양성(Diversity)**  
두 항목을 동시에 평가.

## 2.2 IS 계산 방식

### ■ 개념
- 예리한 이미지: 분류기 예측 확률이 하나의 클래스에 몰림 → **낮은 엔트로피**
- 다양한 이미지: 전체 샘플의 예측 클래스 분포가 고르게 나타남 → **높은 엔트로피**

### ■ IS = Sharpness × Diversity

## 2.3 IS의 한계
1. ImageNet 클래스에 없는 데이터는 평가 불가  
2. Mode Collapse에 취약 (한 이미지만 반복 생성해도 점수 높게 나옴)  
3. 확률 기반 공격(gradient attack)에 취약  
4. 원 데이터와 비교하지 않아 품질 저하 탐지가 어렵다

---

# 3. Fréchet Inception Distance (FID)

## 3.1 FID의 목적
- **생성 이미지 vs 실제 이미지**  
  두 분포의 특징 벡터를 비교하여 품질·다양성을 동시에 평가  
- 낮을수록 좋음

## 3.2 FID 계산 방식
- Inception v3의 **특징 벡터** 사용  
- 실제 데이터/생성 데이터 모두 정규분포로 가정  
- 두 정규분포 간 **Fréchet Distance** 계산

## 3.3 FID의 한계
- Fidelity와 Diversity를 **분리해서 평가할 수 없음**
  - 어떤 모델이 품질을 높였는지
  - 어떤 모델이 다양성을 높였는지 판단하기 어려움

---

# 4. Improved Precision & Recall (P&R)

FID의 한계를 보완하기 위해 등장한 지표.  
각각 **Fidelity / Diversity**를 별도로 측정 가능.

## 4.1 정의

### ■ Precision (충실도 / 품질)
- 생성된 데이터 중 **실제 데이터 분포 근처에 존재하는 비율**

### ■ Recall (다양성)
- 실제 데이터 중 **생성 데이터 분포 근처에 포함되는 비율**

## 4.2 "근처(Close to)" 정의
- k-NN을 사용해 반경(r) 내에 있으면 근처라고 정의

## 4.3 Improved Precision
- 실제 데이터 근방에 포함된 생성 데이터 / 생성 데이터 전체

## 4.4 Improved Recall
- 생성 데이터 근방에 포함된 실제 데이터 / 실제 데이터 전체

## 4.5 한계
- 이상치(outlier)에 민감
- 샘플링에 따라 점수 변동성 큼
- 계산량 많음
- 반경 k 등 매개변수에 민감

## 4.6 개선 방안
- Density / Coverage 개념 추가  
  → 이상치에 덜 민감하고 계산 효율 증가

---

# 5. 조건부 생성 모델 평가 지표

일반 생성 모델은 p(X)를 학습하므로 조건을 평가하지 않는다.  
조건부 생성 모델은 **p(X|Y)** 를 학습하므로 “조건을 얼마나 반영했는가?”가 중요.

## 5.1 조건부 생성 모델 평가 필요성
- IS, FID는 조건을 고려하지 않음  
- 조건에 맞지 않는 이미지도 품질만 좋으면 점수가 높을 수 있음 → 부적절

---

# 6. 조건부 생성 모델 전용 평가 지표

## 6.1 Intra-FID
- **각 클래스별 실제 데이터 vs 해당 조건으로 생성된 데이터** FID 계산
- 클래스별 차이를 더 정확하게 반영

## 6.2 사전훈련 분류기 Accuracy
- 생성된 이미지의 조건(Y)을 맞추는지 확인
- 단점: 분류기 자체의 성능에 크게 의존

## 6.3 CAS (Classification Accuracy Score)
- 생성된 이미지로 새로운 분류기를 학습하여 정확도 측정
- 특정 생성 모델의 품질을 더 세밀하게 반영  
- 단점: 생성 모델마다 분류기를 다시 학습해야 함

## 6.4 LPIPS (Learned Perceptual Image Patch Similarity)
- 이미지 간 **지각적 유사도** 측정
- 낮을수록 원본과 다름 → **더 다양하게 생성했다**는 의미  
- 변환/스타일 작업에서 다양성 지표로 많이 활용

## 6.5 CLIP Score
- Text–Image 관계를 학습한 CLIP 모델 사용  
- 생성된 이미지가 **텍스트 조건을 잘 반영했는지 평가**  
- Text-to-Image 평가에서 사실상 표준

---

# 7. 요약

### ■ 생성 모델 평가가 까다로운 이유
- 정답(GT) 없음  
- 사람 평가(주관성) 의존  
- 품질(Fidelity)와 다양성(Diversity) 동시에 고려해야 함

### ■ 주요 지표
- **IS**: 품질+다양성. 단점 많음  
- **FID**: 이미지 분포 비교, 신뢰성 높음  
- **Improved Precision & Recall**: 품질/다양성 분리 평가  
- **Intra FID / Accuracy / CAS / LPIPS / CLIP Score**: 조건부 생성 평가

### ■ 결론
생성 모델 평가는 단일 지표로 결정하기 어렵고,  
각 모델 특성에 따라 **복수의 지표를 함께 사용**해야 한다.


