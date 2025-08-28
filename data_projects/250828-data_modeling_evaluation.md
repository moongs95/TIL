# Data Modeling & Evaluation


## 모델링을 위한 데이터 사전 준비

- 모델이 이해할 수 있는 데이터 형태로 가공
- 학습과 예측을 위한 train/test set 분할(필요시 validation)
- 숫자로 이루어진 형태의 data만 인식가능하기에 문자형 변수 인코딩 필요
- 원핫 인코딩과 라벨 인코딩이 있음


## Model Selection

- 학습할 Model들을 list-up하는 과정
- 분석하고자 하는 데이터의 특성이 모두 다르므로 완벽한 알고리즘은 없음
- Data by Data
- Regression : ridge, lasso, elastic net, randomforest, lightGBM
- Classification : logistic regression, randomforest, lightGBM


## 모델링 및 성능 비교

- Model Selection 단계에서 선정한 모델들을 학습하고 성능을 기록
- 동일한 Data set, 동일한 환경, 동일한 지표로 비교
- Regression : MAE, MSE, RMSE, R-squared
- Classification : precision, recall, f1-score, auc, auroc


## Model Evaluation

- Hyper-parameter tuning 전 전체 모델 성능 비교함
- 과적합과 성능 두마리 토끼를 잘 잡을 수 있게 Hyper-parameter tuning을 해야함
