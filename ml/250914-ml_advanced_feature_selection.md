# 변수 선택

- 학습에 필요한 변수를 중요도에 따라 선택하는 과정

## 대표적인 변수선택의 3가지 접근법

### Filter methods

- 변수들 간 통계적 관계를 기반으로 변수의 중요도 설정, 빠름
- 상관관계, 분산 기반 방법, 카이제곱 기반

### Wrapper methods

- 실제 머신러닝 모델의 성능을 기반으로 변수 중요도 설정, 최적 변수 조합, 느림
- Forward selection, Backward elimination

### Embedded methods

- 모델 훈련 과정에서 스스로 변수의 중요도 설정
- feature importance(지니계수, 엔트로피), regularizer 기반(L1, L2)

## 그 외 접근법

### Permutation Importance

- 검증 데이터셋의 feature를 하나하나 shuffle하며 성능 변화 관찰
- 만약 해당 feature가 중요한 역할을 한다면 모델 성능이 크게 하락

### Target permutation

- shuffle된 target 변수 모델을 학습, feature importance와 actual feature importance 비교해 변수 선택
- 진행 과정
1. Null importance 도출
2. Original importance 도출
3. 1과 2에서 구한 importance를 비교해 실제로 중요한 변수를 선택 가능

### Adversarial validation

- 학습 데이터셋과 검증 데이터셋이 얼마나 유사한지 판단하는 방법
- 학습 target 값은 1로, 검증은 0으로 지정후 Binary classification 모델링
