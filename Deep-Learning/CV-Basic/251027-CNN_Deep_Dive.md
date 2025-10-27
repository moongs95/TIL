# CNN Deep Dive

## 01 CNN vs. 고전 컴퓨터 비전

### 1.1 고전 컴퓨터 비전

고전 컴퓨터 비전에서의 Filter

→ 특정한 목적, 사람의 수작업

- Sobel Filter: 정해진 Sobel Kernel을 통해 x 방향과 y 방향으로 변화율을 계산하여 엣지를 검출하게 되며, 학습 가능하지 않음.
- convolution 연산을 함 → 좌우 필터 연산 값의 픽셀 값의 차이가 클 수록 엣지

### 1.2 현대의 컴퓨터 비전

**학습 가능한 Filter의 등장**

- CNN = Convolutional Neural Network
- Convolution Filter: 현대에 들어서는 Convolution 연산을 통해 산출한 결과를 정답지(Ground Truth, GT)와 비교하여 오차를 줄여나가는 방식 등으로 계속 업데이트 되는 학습 가능한 필터를 많이 사용하게 됨. ⇒ 정답지만 잘 만들면 됨!
- 고전 컴퓨터 비전의 방법만으로는 성능이 좋지 않거나 해결이 불가능했던 태스크들을 할 수 있게 됨

Canny Edge : 노이즈가 심한것은 잘 못함 / 고양이, 산 잘 구별 못함 → CNN : 잘 됨

- segmentation에서도 성능 좋음

### 1.3 학습 가능한 파라미터란?

**학습 가능한 파라미터들을 가진 레이어 예시**

- Convolution Layer: Parameters = (F.in x F.in x C.in + 1-bias) x C.out

- Batch Normalization Layer : Parameters = 2 x C.in … (감마, 베타)

- 각 배치마다 계산되는 평균과 분산은 들어온 데이터에서 단순 계산이 되는 방식이라면 zero min unit variance로 normalize된 데이터를 다시 scaling shift하는 감마와 베타는 실제로 정답지와 오차를 비교하여 학습되는 파라미터
- scaling shift는 각 채널마다 연산, 감마와 베타 모두 C → 2 x C ⇒ 평균과 분산이 아닌 감마와 베타로 한정해서 이해
- 감마와 베타는 학습가능한 파라미터
- 별개로 평균과 분산은 test시 이동평균으로 사용하기 위해 따로 저장
- Fully Connected Layer : Parameters = (N.in x N.in x C.in +1) x M

- A 행렬 : 입력 채널수 행 x 출력 채널수 열

**학습 가능하지 않은 레이어 예시**

- Activation Layer : sigmoid, tanh, ReLU, Leaky ReLU, Maxout, ELU → 학습가능한 activation function이 있지만 성능 우위를 위한 것
- Pooling Layer : max-pooling, average pooling → 채널 별로 하나씩, 입력에 대한 연산만 함.

## 02 CNN Layer별 특징 탐구

### 2.1 CNN 모델의 구성

- Convolution Block: Convolution Layer(학습가능한 필터를 가짐) → Batch normalization Layer(뉴런들 값 튀는 것 방지) → Activation Layer(비선형성)
- Pooling Layer(파라미터를 사용하지 않고도 spatial 정보 취합)

### 2.2 Convolution Layer

- 네트워크가 비전 태스크를 수행하는 데에 유용한 Feature들을 학습할 수 있도록 함
- Convolution Layer를 여러개 쌓는 경우, 뒤 레이어의 결괏값 하나를 만드는데 사용되는 이미지의 범위가 넓어짐
- 뒷 레이어로 갈 수록 Receptive field가 커짐

- receptive field : 특정 convolution layer에서 연산결과를 만들때 사용한 이미지 영역의 크기, 뒤로 갈 수록 전역적인 정보가 담김
- Convolution Layer의 초반 Layer의 경우 edge와 같은 low-level feature를 주로 학습하게 되고, 후반 Layer의 경우 shape과 같은 high-level feature를 주로 학습하게 됨

- 아무리 다른 이미지라 해도 확대해서 작게 보면 별 다르지 않음 → 엣지만 보면 다른 이미지 인지 모름
- 뒤로 갈 수록 넓은 영역을 보면 차이를 느낄 수 있음

→ 학습한 feature는 어디에 저장? 어떤 형태?

32x32 → 3채널

28x28 모종의 정보 6은? → 3은 엣지 3은 채널? ⇒ 정답지와의 오차를 줄일 수 있는 정보가 자동적으로 담김 → feature map!

이런 feature map이 커질 수록 더 많은 정보가 담기니까 더 어려운 문제도 해결 가능

### 2.3 Batch Normalization

- Deep network가 잘 학습될 수 있도록 함
- Gradient flow를 개선시킴
- 더 빠르게 converge(모이다)될 수 있도록 함
- 학습 시 regularization을 한 것 같은 효과를 얻을 수 있음
- 좀 더 robust한 모델이 될 수 있도록 하는 데에 기여함 (즉, overfitting을 방지하는 데에 도움을 줌)
- 보통 Convolution Layer 다음, 그리고 Activation Layer 전에 Batch Normalization을 해줌

여러 번의 최적화 과정을 가짐. 오차가 크면 최적의 값을 찾아가는 게 힘들다.

과하게 큰 파라미터 조정도 batch norm을 하면 좀 더 쉽게 최적화 가능

### 2.4 Activation Layer

- 모델에 비선형성을 부여해 주기 위해서 사용됨
- 선형 함수의 Layer들로만 구성될 경우 여러 개를 쌓더라도 선형 함수 하나로 표현될 수 있는 모델이 될 뿐이기 때문에, 깊은 네트워크의 장점을 살릴 수 없게 됨

cf. convolution layer는 선형만 있음

**Sigmoid**

- [0, 1] 사이의 값으로 변경해 줌

→ 모든 곳에서 미분 가능, 연속적

1. Gradient 값이 kill 되는 현상이 생길 수 있음 (e.g. σ(x)의 값이 0에 가깝거나 1에 가까운 값일 경우)
2. Sigmoid를 거친 결과는 0에 centroid되어 있지 않음 (항상 양수 값만 가짐)
3. Exponential 함수를 계산해야 하므로 cost가 높음

**Tanh**

- [-1, 1] 사이의 값으로 변경해 줌
1. 여전히 gradient 값이 kill 되는 현상이 생길 수 있음
2. Tanh를 거친 결과는 0에 centroid되어 있음

**ReLU**

- 음수면 0, 양수면 입력 그대로

→ 복잡하지 않아서 효율적

1. 양수의 값을 가질 경우 gradient가 kill되지 않음 → 모델 학습 빨리, 양수일 경우 뉴런 활성화 더 많이 되어 있음
2. Computational cost가 매우 적음
3. Sigmoid나 tanh 함수보다 매우 빠르게 수렴함 (e.g. 대략 6배 빠름)
4. ReLU를 거친 결과는 zero-centroid가 아님
5. 음수값을 가질 경우 gradient가 0이므로 update 되지 않음 → 보완책이 Leaky ReLU 음수일 경우 0.1을 곱해주기 때문에 0이 아니라 update 될 수 있음

### 2.5 Pooling Layer

- Feature Map에 Spatial Aggregation을 시켜줌
    - 모델의 파라미터 수를 줄여줌
    - 더 넓은 Receptive Field를 볼 수 있게 해줌

**Max Pooling vs. Average Pooling**

- Max Pooling의 단점: 정보의 손실이 일어날 수 있음
- Average Pooling의 단점: 중요한 정보가 희석될 수 있음

## 03 CAM

모델이 이미지의 어디를 보고 판단을 하는지를 시각화하는 것이 CAM

### 3.1 Class Activation Map(CAM)

→ 모델이 어디를 보고 있는지 시각화 할 수 있는 방법을 제시, 이미지의 spatial 위치(x, y좌표) 마다 각각의 class에 대해서 모델이 중요하게 생각하고 예측하는지

- Fully Connected Layer (FC Layer)의 단점: Flatten하는 과정을 거치기 때문에 Pixel의 위치 정보를 잃게 됨 → 공간 정보를 잃게 됨

- Global Average Pooling: Flatten하는 대신 Global Average Pooling을 거친 것으로, Feature Map 하나 당 하나의 특징 변수(Fk)로 변환하게 됨.

### 3.2 CAM의 구조

- FC layer 대신 GAP을 수행하여 각 클래스로 분류될 확률에 영향을 미친 객체의 좌표 (x,y)를 추출할 수 있음

Mc→ feature map과 클래스 c로 분류될 weight를 곱하면 좌표(x,y)별 클래스 c에 대한 영향력을 계산할 수 있음

### 3.3 CAM의 결과

각 클래스가 어떤 곳을 보고 있는지 알 수 있음

**Global Average Pooling vs. Global Max Pooling**

- Global Average Pooling (GAP): 각 Feature Map에서 전체적인 특징들을 찾아내게 되어 Localization 능력이 좋음
- Global Max Pooling (GMP): 각 Feature Map 에서 가장 값이 큰 값을 추출하는 방법으로, Feature Map에서 뚜렷한 특징들만 찾아내게 되어 Localization 능력이 GAP보다는 낮다고 함

## 04 Grad-CAM

모델의 Gradient 값을 통해 어디를 보는지를 시각화한 Grad-CAM

### 4.1 Gradient-weighted CAM(Grad-CAM)

- CAM : 예측 직전에 GAP를 수행하도록 네트워크의 변경이 필요함 → 그리고 변경된 구조로 재학습 필요
- Grad-CAM : Gradient Signal을 이용하여 Feature Map을 결합하는 방식을 사용하여 기존 네트워크 구조를 그대로 사용할 수 있음

GAP가 아닌 gradient를 이용

- 만약 Grad-CAM에 Global Average Pooling을 적용시킨다면?

Grad-CAM is Generalized version of CAM

### 4.2 Grad-CAM의 결과

- 이미지와 관련 없는 class일수록 object를 집중해서 보는 것이 아니라 background와 같은 곳을 보고 있음을 알 수 있음
- 이미지에 adversarial noise가 있어서 classification을 완전히 잘못한 상황에서도 Grad-CAM의 결과는 본래의 class에 맞게 나오고 있다는 것도 알 수 있음
