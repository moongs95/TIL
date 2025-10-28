# Semantic Segmentation

## 01 Semantic Segmentation

### 1.1 Semantic Segmentation이란?

- Semantic segmentation: Pixel-wise로 각각의 Class를 예측하여 물체 Category 별로 분할
- Category: 각 픽셀의 Label 예측
- Architecture: CNN Backbone (Encoder) + Decoder(클래스 별 확률 예측)

모든 픽셀별로 클래스 확률값 구함! → 세밀하게 분할 가능, 세밀한 이미지 이해

**Object Detection vs Semantic Segmentation**

→ Object Detection : BBox 안에 강아지가 아닌 픽셀들 존재, 배경 객체 검출 어려움

→ Semantic Segmentation : 정밀한 연산 가능

### 1.2 Semantic Segmentation 예시

- 자율주행 : 도로, 사람, 나무, 건물 등 여러 다른 배경 객체들도 검출할 수 있음
- 의료 영상 진단 : 의료 이미지 정밀한 분석 필요, 정상조직, 비정상조직 분류 해야함

### 1.3 Semantic Segmentation Dataset

**KITTI**

- 차량 주행중 촬영된 자동차 및 사물 이미지 데이터
- Semantic Label이 있는 200개의 Train Set과 200개의 Test Set으로 구성

**Cityscape**

- 도시 거리 장면 이미지 데이터
- 50개의 도시의 다양한 시간/계절/날씨를 촬영한 장면 내의 30개의 물체(Class)
- Classes: Group 기준 Flat road, Human, Vehicle, Construction, Object, Nature, Sky, Void 등
- 5,000장의 이미지 Annotation (Fine-annotation 기준)

→ admin 필요, 권한 얻어야 함, 자유롭게 사용하기 어려움

**Pascal VOC (Visual Object Classes)**

- 시각 객체 클래스 인식을 위한 20개의 사물 클래스 이미지 데이터
- 2012년 데이터 기준 11,530개의 이미지와 6,929개의 Segmentation Annotation

### 1.4 성능 평가 방법

**Intersection-over-Union (IoU)**

- Pixel-wise IoU 사용
- segmentation map : Ground Truth, Predictions 픽셀 별로 시각화
- IoU = Area of Intersection / Area of Union = TP / TP+FP+FN

### 1.5 Segmentation의 종류

Semantic Segmentation vs Instance Segmentation(객체별 분할이 목표, 배경은 구별 못함) vs Panoptic Segmentation(앞 선 두가지의 병합)

# Semantic Segmentation using CNNs

## 01 Semantic Segmentation using CNNs

### 1.1 Semantic Segmentation 구조

- Semantic Segmentation의 Backbone+Decoder는 다양한 방식으로 구성 가능

- backbone과 decoder의 다양한 옵션들 존재
- backbone을 지나면 원본이미지랑 점점 달라짐 → 작아지는 feature map을 decoder를 통해 어떻게 크게 만드는지

### 1.2 Semantic Segmentation에 CNN 이용하기

**Sliding Window**

- 이미지 전체에 대한 클래스 예측을 sliding window 픽셀 하나하나 마다 그 픽셀 주변에도 크기를 두고 가운데 값으로 클래스 예측

문제점

- 픽셀 주변의 정보밖에 고려하지 못함
- 많은 패치가 중복되는 영역을 처리하기 때문에 계산 비용 증가

**Size Preserving Convolutional Layers**

- 기존 cnn인데 사이즈가 줄어드는게 아니라 padding과 stride 조절을 통해 유지되게 쌓자! → 중복 연산 없어짐

문제점

- 패딩을 많이 사용해야함 → 크기는 유지 되지만 상당 수 부분이 실제 이미지와의 정보는 없음, 결국 지역적인 부분만 가지고 예측을 하게 됨
- Receptive field가 여전히 제한적

**Downsampling + Upsampling**

- 기존 CNN을 통해 spatial 크기가 줄어들면서 충분히 feature가 뽑아지면 입력과 같은 크기에 맞춰 upsampling을 시행

장점

- 큰 Receptive Field를 가짐

## 02 FCN for Semantic Segmentation

Semantic Segmentation 문제의 기본적인 CNN 모델인 FCN

### 2.1 FCN 구조

**FCN (Fully Convolutional Networks)**

- 기존에는 CNN을 지난 작아진 spatial 한 feature map을 가지고 FC에 넣어서 예측을 수행 → 이미 작아져버린 feature map에 대해서 원래 크기로 복원할 수 없기 때문에 이미지 전체에 대한 전반적인 예측값(pixel 단위로 디테일하고 세밀한 예측값이 아니라 coarse한 예측값) ex. 전체 이미지 보고 분류

⇒ FC layer를 다른 형태로 변형하여 픽셀 단위(dense한 prediction)의 예측을 만드는 구조

**Convolution (Downsampling)**

- Backbone (Convolution Layers)를 통해 Features 추출 → 입력의 크기를 줄임
- 뒷 레이어로 갈 수록 Receptive Field가 커진다!

**Deconvolution (Upsampling)**

- Feature Map을 확장하여 입력 이미지와 동일한 크기의 Segmentation Map 생성 → 입력의 크기를 키움

ex. 3x3(padding) → 5x5

Deconvolution Layer의 역할

- Stride (S): Filter를 얼마만큼의 간격으로 움직이는 지를 나타냄

output size = ((N-1)xS) + F

- N: input의 크기
- F: filter의 크기
- S: stride의 크기
- O: output의 크기

**Skip Connection**

- Upsampling의 결과와 Backbone의 중간 Layer에서 나오는 Feature Map과 결합 → 최종 결과

### 2.2 Training Process

**Preprocessing** : resize, normalization

**Model**

1. FCN 모델을 초기화
2. 가중치(Weight) 무작위 설정

각 픽셀 위치마다의 클래스별 확률을 추천 할 수 있도록 학습

**Loss**

- Loss Function: Pixel-wise Softmax Cross-Entropy Loss
- 각 픽셀마다 모델이 예측한 클래스 확률 분포와 실제 레이블의 차이 계산
- Cross-Entropy Loss를 계산

### 2.3 Test Process

**Preprocessing** : 학습과 동일, 랜덤성 고정

**Model**

1. 학습된 가중치(weight) 사용
2. 각 픽셀에 대한 클래스 확률 분포 예측

**Prediction**

- Prediction: 입력 이미지를 사용하여 segmentation map 생성
- Segmentation map은 이미지와 동일한 크기 가짐
- 각 픽셀에 예측된 클래스 레이블이 할당

### 2.4 Experiments

FCN-8s, SDS, Ground Truth를 비교했을 때 → 전반적으로 세밀하게 GT에 맞춰서 클래스 분류하지만 더 크게(FP) 더 작게(FN) 분류

# Improving Semantic Segmentation using CNNs

CNN 개선

## 01 U-Net

Semantic Segmentation에서 보편적으로 사용하는 U-Net

### 1.1 U-Net 이란?

- MICCAI 2015에 출판된 논문으로, 바이오메디컬 이미징 분야에서 사용하다 보편화 됨
- U-Net의 이름은 U자 모양의 아키텍처에서 유래

**Encoder(Backbone)**

- 입력 이미지를 Downsampling
- 이미지의 공간 정보를 계층적으로 추상화 및 중요한 Feature 추출
- spatial 크기가 작아지면서 receptive field가 커짐, 이에 따라 앞 CNN layer와 뒤 CNN layer의 학습 특징이 달라짐

**Decoder**

- Encoder가 추출한 Feature를 Upsampling
- Upsampling하여 Segmentation Map 생성

→ 여러 단계로 구성되어 있는 것이 특징!

- 점점 fine grained하게 단계별로 변화
- feature map의 크기가 작으면 세부적 디테일 표현하기 어려움 → feature map 크기가 커지면서 더 표현을 잘 할 수 있음

**Skip Connection**

→ 중요한 역할!

- Encoder와 Decoder 간의 정보 전달
- Decoder에서 Upsampling된 Feature와 동일한 해상도의 Encoder Feature를 결합

→ 디코더의 전 단계에서 upsampling해서 만들어 준 feature map과 인코더가 downsampling하면서 추출한 feature들의 채널을 구분해서 입력으로 넣어주고 있음 ⇒ 구조적 변형 가함

- 명시적으로 인코더에서 온 feature map과 디코더에서 온 feature map의 채널이 분리가 됨으로써 다르게 사용할 수 있게 구조적으로 도움

**FCN vs U-Net**

- FCN (Fully Convolutional Network), U-Net 모두 Segmentation 수행
- 차이점 : U-Net은 Encoder와 Decoder 사이에 Skip connection 존재하며, 중간 Layer 정보 계층적으로 전달
- FCN은 skip-connection을 더해주고, U-Net은 채널을 추가해줌

### 1.2 Training Process

**Preprocessing**

**Model**

1. U-Net 모델을 초기화
2. 가중치(Weight) 무작위 설정
3. 입력과 같은 크기

**Loss**

- Pixel-wise cross entropy loss: Backbone이 각 픽셀 별로 예측한 확률 분포와 실제 클래스 간의 차이 측정
- 예측 확률과 실제 클래스 레이블 간의 거리를 최소화하도록 학습에 사용

### 1.3 Test Process

**Preprocessing**

**Model**

1. 학습된 가중치(Weight) 사용
2. 각 픽셀에 대한 클래스 확률 분포 예측

**Prediction**

- Prediction: 모델 결과를 사용하여 segmentation map 생성
- Segmentation map은 이미지와 동일한 크기 가짐
- 각 픽셀에 예측된 클래스 레이블이 할당

### 1.4 Experiments

- 당시에 성능이 다른 모델에 비해 월등히 높았음
