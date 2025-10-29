# CV Backbone Overview

## 01 Why CV?

### 1.1 CV로 할 수 있는 일
- Tesla Autopilot  
- Tesla Optimus  
- Medical AI  
- Environmental AI  
- NeRF (Neural Radiance Field)

---

## 02 Why CNN?

### 2.1 Why CNN?
**MLP (Multi Layer Perceptron)**  
- Input layer → hidden layers → output layer로 구성  
- Input layer의 neuron 개수 = feature 수  
- Tabular data 학습에 최적화  

**MLP in CV**  
- 이미지를 flatten해야 입력 가능 → 이미지의 지역 정보(locality) 손실

**이미지의 Locality 특성**  
- Spatial locality: 같은 물체라도 크기 다름  
- Positional invariance: 같은 물체라도 위치 다름  

**Convolution Filter**  
- 이미지를 flatten하지 않고 연산 가능  
- Object 구조와 주변 정보를 함께 학습  
- 같은 필터를 전체 이미지에 적용하여 위치 불변성 확보  

---

## 03 Chapter Overview

### 3.1 Chapter Overview
**챕터 방향**
- Transformer 이전/이후의 CV backbone 이해  

**세부 커리큘럼**
- CNN backbone: AlexNet, VGGNet, ResNet, EfficientNet  
- Transformer backbone: ViT, Swin  

**CNN의 개념**
- 이미지의 locality 특성을 반영하는 신경망  
- Convolutional layer를 쌓아 feature를 추출  
- MLP의 flatten 한계를 극복  

**ImageNet ILSVRC**
- 2010년 시작된 이미지 분류 대회  
- 2012년 AlexNet으로 CNN 대세화  
- 2015년부터 인간보다 낮은 오차율 달성  

**주요 CNN Backbone**
- **AlexNet (2012)**: GPU 기반 최초의 CNN  
- **VGG (2014)**: 단순하지만 깊은 네트워크의 중요성 제시  
- **ResNet (2015)**: Gradient vanishing 문제 해결, 152 layers  
- **EfficientNet (2019)**: depth·width·resolution의 균형적 확장  

**CNN의 한계점**
- Locality는 확보했으나, 장거리 의존성(long-range dependency) 파악 어려움  
- Self-attention 기반 Transformer로 해결  

**Transformer의 등장**
- NLP에서 long-range dependency 문제 해결  
- Self-attention으로 feature 중요도 학습 가능  

**From MLP → CNN → Transformer**
- MLP: locality 상실  
- CNN: locality 확보  
- Transformer: 관계성 및 중요도 학습  

---

# Backbone 이해하기: CNN

## 01 CNN의 기본구조 1

### 1.1 Convolution Filter

**Filter**
- 이미지 처리용 행렬 (kernel/mask)
- Edge detection, blurring 등에 사용  
- Sliding window로 전체 이미지에 적용  

**Convolution 연산**
- 이미지와 필터 간의 합성곱 연산  
- 결과를 **feature map (activation map)**이라 함  
- CNN에서는 학습 가능한 filter를 사용  

---

## 02 CNN의 기본구조 2

### 2.1 Convolution Filter 활용

**Channel**
- Grayscale: 1채널  
- RGB 이미지: 3채널  
- 예: 32×32×3 이미지에 5×5×3 필터 적용 → feature map 생성  

**Feature Map 크기 변화**
- Convolution 연산 시 크기 감소  
- Stride, Padding으로 조절 가능  

**Stride**
- Sliding window 이동 간격  

**Padding**
- 이미지 주변을 0으로 채움  

**Pooling**
- Parameter 없이 feature map 축소  
- MaxPooling: 최대값 선택  
- AvgPooling: 평균값 선택  

**Feature Map 크기 계산식**
- Input: W, H  
- Filter: F  
- Padding: P  
- Stride: S  
- Output:

```text
W_out = (W - F + 2P)/S + 1
H_out = (H - F + 2P)/S + 1
```


---

## 03 CNN Backbone 소개

### 3.1 CNN 기본구조
- Convolution layer로 feature 추출  
- feature map 크기 ↓, receptive field ↑  
- 마지막 feature map을 flatten 후 FC layer로 분류  

---

### 3.2 AlexNet
- **2012 ILSVRC 우승**
- CNN 최초의 GPU 기반 모델  
- 활성화 함수: **ReLU(x) = max(0, x)**  
- 비선형 패턴 학습 가능, 연산 효율 높음  
- **Dropout** 사용: 일부 뉴런 비활성화로 과적합 방지  

---

### 3.3 VGG
- **2014 ILSVRC 준우승**
- 단순한 구조지만 깊은 네트워크의 중요성 강조  
- **VGG-16 / VGG-19**
- 3×3 convolution filter만 사용  
- 깊게 쌓을수록 receptive field 확장  
- AlexNet과의 비교:
- AlexNet: 다양한 필터 크기 (11×11, 5×5 등)
- VGG: 오직 3×3 conv 사용 → 파라미터 수 감소, 효율적 학습  

**예시 코드**
```python
# Block 1
nn.Conv2d(3, 64, kernel_size=3, padding=1),
nn.ReLU(),
nn.Conv2d(64, 64, kernel_size=3, padding=1),
nn.ReLU(),
nn.MaxPool2d(kernel_size=2, stride=2),

# Block 2
nn.Conv2d(64, 128, kernel_size=3, padding=1),
nn.ReLU(),
nn.Conv2d(128, 128, kernel_size=3, padding=1),
nn.ReLU(),
nn.MaxPool2d(kernel_size=2, stride=2),

# Fully Connected
nn.Linear(512 * 7 * 7, 4096),
nn.ReLU(True),
nn.Dropout(),
nn.Linear(4096, 4096),
nn.ReLU(True),
nn.Dropout(),
nn.Linear(4096, num_classes),
```

### 3.4 ResNet

#### Introduction
- 깊은 네트워크에서 발생하는 **gradient vanishing problem** 해결  
- **Identity shortcut (skip connection)** 사용  
- AlexNet (8 layers), VGG (19 layers)에 비해 최대 **152 layers** 구성 가능  

#### Residual Block
- 입력: x  
- 연산: F(x)  
- 출력: **F(x) + x**  
- 역전파 시 gradient 소실 방지  

#### Variants
- ResNet-18, ResNet-34, ResNet-50, ResNet-101, ResNet-152  

#### 결과
- **더 깊은 네트워크일수록 에러율 감소**  

---

### 3.5 EfficientNet

#### Motivation
- ResNet 이후 모델들은 성능 향상 ↔ 파라미터 증가 ↔ 속도 저하  
- **효율성과 정확도 간의 trade-off 문제** 해결 목표  

#### Scaling 방법
- **Width Scaling**: 채널 수 증가 → 세밀한 특징 탐지  
- **Depth Scaling**: layer 수 증가 → 고수준 feature 학습  
- **Resolution Scaling**: 입력 이미지 크기 증가 → 세밀한 정보 확보  

#### Compound Scaling
- Depth(ɑ), Width(β), Resolution(𝛄)을 **균형적으로 확장**  
- Scale factor ϕ=1일 때:  
  - ɑ=1.2  
  - β=1.1  
  - 𝛄=1.15  
- 이때 모델을 **EfficientNet-B0**  
- ϕ를 증가시키며 **B1~B7** 모델로 확장  

#### Observation
- Scale up 시 **성능 향상 폭은 점차 감소**  
- **최적의 (ɑ, β, 𝛄) 조합 존재**  

#### 결과
- 기존 모델 대비 **파라미터 수는 적지만 정확도 유지**  
- **정확도와 효율성을 모두 잡은 구조**

---

✅ **요약**

| Model | 특징 | 핵심 아이디어 |
|--------|--------|----------------|
| **AlexNet** | 최초의 CNN 기반 GPU 모델 | ReLU, Dropout |
| **VGG** | 단순하지만 깊은 구조 | 3×3 필터 반복 |
| **ResNet** | 깊은 네트워크 안정화 | Skip connection |
| **EfficientNet** | 효율적 확장 | Compound scaling (depth, width, resolution) |
