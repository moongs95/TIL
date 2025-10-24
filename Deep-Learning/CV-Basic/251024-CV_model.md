# 컴퓨터 비전 모델 구조

## 01 Backbone의 의미

### 1.1 Visual Feature란?

**Visual Feature**

눈으로 감지할 수 있는 정보들

**Visual Feature in Computer Vision**

- Visual Feature: 컴퓨터 비전의 태스크(classification, detection, segmentation, …)를 해결할 때 필요한 이미지의 특성을 담고 있는 정보들

ex. 코끼리 특징 : 긴 코, 상아, 큰 귀, 회색빛 피부, …

→ 어떻게 컴퓨터에게 이해?

### 1.2 Backbone의 역할

- Backbone은 이미지에서 중요한 Feature를 추출(extract)할 수 있도록 훈련됨
- 즉 Backbone의 역할은 **주어진 비전 태스크를 잘 수행할 수 있는 압축된 Visual Feature를 산출**하는 것

### 1.3 Backbone의 구조

- Layer: Input 이미지에서 Feature(points, edges, shapes, …)를 추출하기 위한 연산을 하는 층
- Backbone은 여러 개의 Layer로 이루어져 있고, 이를 통해 다양한 Level의 Feature를 추출할 수 있음

→ 앞 선 레이어의 엣지나 feature들을 사용해서 feature 추출

## 02 모델의 구성

### 2.1 Decoder의 역할

→ backbone과 결합, feature를 추출하는 것만으론 태스크를 완성할 수 없음

- 모델의 쓰임새에 따라 다양한 비전 태스크가 존재함
- 따라서 **Decoder는 압축된 Feature를 목표하는 태스크의 출력 형태로 만드는 과정을 수행**함 → 각각의 문제에 맞는 결과를 낼 수 있는 decoder가 필요

(Classification) 이미지에 있는 물체는 뭐야?

(Detection) 노란색 자동차와 빨간색 자동차의 위치를 박스로 표시해줘

(Segmentation) 노란색 자동차에 해당하는 픽셀을 표시해줘

→ 어떤 문제냐에 따라 다양한 decoder를 사용

### 2.2 (번외) Encoder의 역할

→ backbone에서 뽑은 visual feature들을 decoder에 넘겨 주기 전에 한 번 더 가공하는 과정

- 일부 모델들의 경우 Backbone 이후에 Encoder를 도입하여 Feature와 Image Patch들 사이의 관계를 학습시키기도 함

## 03 Decoder의 역할

→ 비전 태스크를 수행하기 위해 Decoder의 구조를 바꾸면 되는 것을 이해

### 3.1 모델의 전체 구조

Backbone + (Optional) Encoder + Decoder

Input Image → 이미지에서 Feature를 추출한 뒤 압축하는 역할(backbone) → 압축된 Feature를 활용하여 비전 태스크 형태로 출력하는 역할(decoder)

### 3.2 Task에 따른 Decoder의 결과

**Classification**

ex.  ‘강아지’, ‘고양이', ‘호랑이', ‘사자'를 포함하고 있는 데이터로 학습한 classification 모델의 경우

decoder : 4가지 클래스 중 어느 클래스에 가까운지 점수 또는 확률을 출력하는 역할

- Fully Connected Layer (FC Layer): 한 layer가 다음 layer와 완전히 연결되어 있는 layer로, 이미지 분류 모델에서 Decoder의 역할로 사용됨

- backbone에서 나온 이미지(BxCxWxH) tensor → FC(decoder) (BxC)로 변경 (Bx # of class)로 추출

B : batch size, C : Channel 공간적 위치에서 추가적 정보를 가지고 있음, 이미지 RGB 채널보다 큰 경우가 대부분, W : 너비, H : 높이

- Softmax: 입력 받은 값을 모두 [0,1] 사이로 정규화 시켜주는 함수를 말함. 이를 통해 Decoder의 출력물을 각 클래스에 해당할 확률로 나타낼 수 있게 됨.

→ 확률값 출력

**Detection**

ex.  ‘강아지’와 ‘고양이'를 탐지할 수 있는 데이터로 학습한 detection 모델의 경우

decoder : 강아지의 위치를 박스로, 클래스별로 확률을 출력해주는 역할

→ 위치값과 어떤 class인지 알려줌

**Segmentation**

ex.  ‘강아지’와 ‘고양이'의 영역을 알 수 있는 데이터로 학습한 segmentation 모델의 경우

decoder : 강아지 혹은 고양이에 해당하는 영역을 픽셀 단위로 출력해 주는 역할

- Backbone은 입력 이미지에서 유의미한 Feature를 추출한 뒤 압축하는 역할이므로, 태스크 종류가 다르더라도 동일한 Backbone을 사용할 수 있음.
- Decoder의 경우에는 최종 결과를 출력해주는 역할이므로, 비전 태스크가 바뀐다면 올바른 형태로 결과를 산출할 수 있도록 디코더 구조를 변경시켜 주어야 함

→ task와 decoder는 같이 변경되어야 하는 존재
