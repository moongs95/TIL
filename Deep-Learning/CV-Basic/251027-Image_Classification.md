# Image Classification

## 01 Image Classification

### 1.1 Image Classification이란?

- Image Classification: 컴퓨터 비전 분야에서 대중적인 task
- Architecture: Backbone (CNN) + Classification head (FC Layer)

**Logits & Softmax**

- Logits: 각 클래스에 대한 예측을 수치(실수값)로 나타내는 중간 단계
- Softmax 함수는 실수 전체의 범위를 가지는 logits을 지수 함수를 사용하여 클래스 간의 상대적 확률 (0 ~ 1 사이의 값) 계산

→ 지수함수로 normalize 해줌

- Data-driven 방식으로 큰 성공을 거둔 컴퓨터 비전 태스크 중 하나
- 기존 rule기반으로 어려웠던 것(사람이 직접 rule을 정하고 logic을 짬 - 세밀하게 하기 어려움)이 딥러닝 기반(데이터에 따라서 알아서 학습)으로 손쉽게 수행

→ 데이터를 어떻게 모을 것인가? 어떤 형태 데이터을 모을 것인가?가 중요해짐

### 1.2 Image Classification Dataset

- Dataset: (image, class) pair로 구성

https://datahacker.rs/008-dataloaders-with-pytorch/

**MNIST**

- 0부터 9까지 10개의 클래스 이루어진 숫자 모음
- 28 x 28 grayscale 이미지 → RGB가 아니라 규모가 작음
- 60k 학습 데이터
- 10k 테스트 데이터

→ small scale dataset

**CIFAR10**

- 10개의 클래스 이루어진 사물 및 동물 모음
- 32 x 32 RGB 이미지 → mnist보다 큼
- 50k 학습 데이터
- 10k 테스트 데이터

→ 여전히 small scale DS

**ImageNet**

- 1000개의 클래스 이루어진 사물 및 동물 모음
- 평균 469x387 RGB 이미지
- 전처리 이후, 일반적으로 256x256 RGB 이미지로 통일
- 최대 ~1.2M 학습 데이터
- 100k 테스트 데이터

→ 대표적으로 사용, Large scale DS, 여러 라이브러리에서 많이 사용

### 1.3 Training Process

다량의 데이터가 있다고 전제

**Preprocessing** : 데이터 augmentation 사용, 회전, resize 등 사용

**Model 출력**

- 학습 안정성을 증대시키는 방법: Batch Normalization(입력데이터의 평균과 분산 계산), Dropout(뉴런 제외 확률 설정)
- Softmax Classifier의 목적: 입력에 대한 클래스별 확률 분포 생성 및 모델을 학습시키는 데 사용

**Loss**

- Loss function: 실제 class와 예측한 class의 차이를 줄이기 위해 사용
- Cross-entropy loss를 이용해 loss function을 정의, 역전파로 weight 업데이트 학습

### 1.4 Test Process

test data 셋이 있다고 전제

**Preprocessing** : train과 크게 다르지 않지만 test 할 때 마다 다른 방식으로 이미지가 전처리 되면 안되기 때문에 학습 때 랜덤성이 있는 걸 사용했다면 test 때는 고정

**Model 출력**

- 효과적 모델 사용법: Batch Normalization(학습 시 구한 평균과 분산 running mean 이용), Dropout(뉴런 전체 이용) 사용 안 함
- Softmax classifier의 목적: 새로운 입력 데이터에 대한 클래스별 확률을 예측

**Prediction**

- Prediction: 학습된 Model의 결과물로, 해당 이미지가 어떤 클래스인지 예측
- Softmax Classifier의 output 중 가장 큰 값

### 1.5 Metric

- 모델이 잘 학습되었는지 판별하기 위해, 정량적인 평가로 Accuracy와 Precision Metric을 이용
