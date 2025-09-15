# 심화 머신러닝 모델

## GBM

- Bagging : 부트스트랩을 통해 표본을 여러번 뽑아 모델을 학습시키고 결과를 집계하는 앙상블 기법
- Boosting : 성능이 약한 모델의 예측값에 대한 오차를 이용해 모델을 더욱 최적값으로 보완하며 성능을 높이는 방법

### Boosting Algorithms

- AdaBoost(Adaptive Boosting) : 이전 모델이 틀리게 예측한 값에 가중치를 부여하여, 다음 모델의 조정에 활용
- GBM(Gradient Boosting Machine) : 정답과 예측값의 차이를 통해 데이터에 가중치를 두어 다음 모델이 조정되었던 이전의 Adaboost와 는 다르게 정답과 이전 모델의 예측값으로 Gradient를 계산하여 다음 모델을 조정하는 Boosting 알고리즘

### Gradient Descent

- 오차함수에서 해당 지점 접선의 기울기를 이용한 경사하강법으로 해결
- 접선의 기울기는 y변화량을 x의 변화량으로 나눈것을 의미, 오차함수의 미분을 통해 계산

### Overfitting

- 학습 데이터셋으로 학습한 모델의 예측값을 통한 잔차가 0이 되며, 학습세트에 과하게 적합(overfitting)되는 문제 발생
- 과적합 완화시켜 주는 regularization 방법 : subsampling, shrinkage, early stopping

## LightGBM

- 대회나 현업에서 주로 사용
- 훈련 속도, 효율성과 메모리 사용량을 줄이면서 성능을 높인 Gradient Boosting Machine
- GBM보다 대규모 데이터 처리 및 학습에 적합

### Propose

- GOSS : Gradient-based One-Side Sampling -> Gradient를 기준으로 학습 데이터를 down sampling
- EFB : Exclusive Feature Bundling -> 입력 feature 수를 줄이는 방법
- 두 방법 모두 전체 데이터를 사용하는데에서 발생하는 시간/연산적인 비용을 효율적으로 개선

### Usage

- 파라미터 100개 이상 있음
- 자주 사용하는 parameters : boosting, data_sampling_strategy, objective
- overfitting 관련 parameters : max_depth, num_leaves, num_leaves, min_data_in_leaf
- control device : device_type
