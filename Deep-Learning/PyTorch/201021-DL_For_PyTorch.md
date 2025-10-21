# 01 PyTorch 작동 구조

PyTorch의 핵심이 되는 클래스와 관계

## 1.1 Deep Learning Key Components

**딥러닝의 학습 단계**

Data → Model → Output → Loss → Optimization

- 딥러닝 모델 구현에 필요한 요소들을 PyTorch를 통해 편리하게 사용

Data → torch.utils.data.Dataset, torch.utils.data.DataLoader

Model → torch.nn.Module

Loss Function → torch.nn, torch.nn.functional

Optimization → torch.optim

## 1.2 PyTorch 클래스 간 관계

Data [Dataset → Index → DataLoader]

Model [torch.nn.Module] → parameters

Output

Loss [torch.nn, torch.nn.functional]

Optimization [torch.optim] → parameters

# 02 데이터

Dataset과 DataLoader를 조합하여 데이터를 손쉽게 로드하고 처리

## 2.1 Dataset & DataLoader의 결과

**Dataset과 DataLoader를 사용하여 데이터 로드**
- `Dataset`과 `DataLoader`를 사용하면, 데이터 집합에서 미니 배치 크기의 데이터를 반환

→ 미니 배치(mini-batch) : 전체 데이터 집합을 더 작은 부분집합으로 분할한 일부 데이터 batch_size = n

## 2.2 Dataset

**단일 데이터를 처리하여 반환하는 작업을 수행하는 역할**

- Dataset은 단일 데이터를 모델의 입력으로 사용할 수 있는 형태(tensor)로 변환하는 작업을 수행
- PyTorch에는 이미지 데이터를 다루는 ‘ImageFolder’, ‘CIFAR10’, ‘MNIST’ 등과 같이 흔히 사용되는 데이터 셋들에 대한 Dataset 구현체들이 이미 제공되고 있어, 편리하게 사용할 수 있음

## 2.3 Custom Dataset

**대부분의 경우, 직접 데이터 셋을 구축**

- PyTorch에서 제공하는 구현체인 `Dataset`은 제한적. 이때, custom dataset을 구현하여 자신의 데이터를 사용한 `Dataset`을 만들 수 있음.
- Custom dataset 구현을 위해서는 `Dataset` 클래스를 상속하여 custom dataset 클래스를 만들어야 함. 이때 아래 세 개의 메서드를 꼭 작성!
    - __init__: `Dataset` 객체가 생성될 때 한 번만 실행. 주로 사용할
    데이터 셋을 불러오고 필요한 변수를 선언. 전처리 실행
    - __getitem__: 주어진 인덱스에 해당하는 단일 데이터를 불러오고
    반환.
    
    → 주어진 인덱스(idx) : PyTorch의 `Dataset`은 `DataLoader`와 함께 사용. `DataLoader`에서는 데이터 셋의 데이터를 로드하는 순서를 의미하는 인덱스를 `Dataset`에 인자로 주어, 데이터 셋의 위치에 해당하는 데이터를 가져옴
    
    - __len__: 데이터 셋의 데이터 개수를 반환. → dataloader에서 필요 ex. 이미지 개수

```python
from torch.utils.data import Dataset

class CustomDataset(Dataset):
	def __init__(self):
		pass
	
	def __getitem__(self, idx):
		pass
	
	def __len__(self):
		pass
```

**Custom dataset 구현 시 주의 사항**

- 데이터 타입 : PyTorch는 데이터를 `torch.tensor` 객체로 다루므로, 데이터는 tensor로 변환되어야 함. 따라서 `__getitem__` 메서드에서 반환하는 데이터는 tensor 형태로 변경하여 반환해야 함
    
    → list, tuple, dictionary로 반환할 수도 있지만 list, tuple의 원소가 tensor여야 하며, dictionary는 value가 tensor여야 함
    
- 데이터 차원 : `Dataset`은 `DataLoader`와 함께 사용, `DataLoader`에서 데이터들을 미니 배치로 묶어(stack) 주는 역할. 이때, 반환되는 모든 데이터의 차원의 크기는 같아야 함 → 미니 배치로 묶어주기 위해서, 패딩을 사용할 수 있음
    
    ex. 모든 이미지는 같은 높이(height), 너비(width)와 채널(channel)을 가짐. → cf. 채널(channel)은 이미지의 색상 정보를 담고 있음. 일반적으로, RGB의 경우 3 채널, 흑백 이미지의 경우 1 채널
    ex. 모든 (텍스트를 포함한) 시퀀스는 같은 길이(max_len)를 가짐
    

## 2.4 DataLoader

**데이터를 미니 배치로 묶어서 반환하는 역할**

- `DataLoader`는 인자로 주어진 `Dataset`을 이용하여, 데이터 셋의 단일 데이터들을 정해진 개수만큼 모아 미니 배치(mini-batch)를 구성하는 역할
- `DataLoader`의 인자로 `Dataset`은 필수이며, 그 외의 추가 인자들이 존재
    - **batch_size** [int, default = 1]: 미니 배치의 크기를 나타냄
    - **shuffle** [bool, default = False]: epoch마다 데이터의 순서가 섞이는 여부
    - **num_workers** [int, default = 0]: 데이터 로딩에 사용하는 서브 프로세스 개수 → 높아질 수록 속도는 빨라지지만 메모리 사용량이 많아짐
    - **drop_last** [bool, default = False]: 마지막 미니 배치의 데이터 수가 미니 배치 크기보다 작은 경우, 데이터를 버릴지 말지를 나타냄 → 수가 딱 떨어지지 않을 경우

# 03 모델

PyTorch를 활용한 모델 구현에 필요한 구조

## 3.1 PyTorch에서 제공하는 모델

**PyTorch는 다양한 모델을 제공**

- Torchvision
    - Torchvision 라이브러리는 이미지 분석에 특화된 다양한 모델을 제공
    - Torchvision 문서에서 불러올 수 있는 여러 가지 모델의 목록을 확인할 수 있음
    - ResNet, VGG, AlexNet, EfficientNet, ViT 등 널리 알려진 모델을 편리하게 사용할 수 있음

- PyTorch Hub
    - PyTorch Hub는 CV, audio, generative, NLP 도메인의 모델들이 공개
    - PyTorch Hub 홈페이지에서 torchvision 라이브러리와 마찬가지로 불러올 수 있는 모델의 목록을 알 수 있음

**편리하게 모델 불러오기**

- Torchvision: `torchvision.models.[model 이름]()`를 활용하면 손쉽게 모델을 불러올 수 있음
    
    ```python
    import torchvision
    
    model = torchvision.models.resnet50()
    ```
    

- PyTorch Hub: `torch.hub.load()`로 모델을 불러올 수 있음
    - 모델마다 `torch.hub.load()`로 전달하는 인자가 다름. 원하는 모델을 PyTorch Hub에서 클릭하여 불러오는 코드를 확인할 수 있음
    
    ```python
    import torch
    
    model = torch.hub.load('pytorch/vision', 'resnet50')
    ```
    

## 3.2 Custom Model의 필요성

**PyTorch에 공개된 모델은 제한적**

- 딥러닝 분야는 빠르게 발전하고 있으며, 새로운 모델이 지속해서 연구 및 발표되고 있음
- 논문에 공개된 모델은 주로 GitHub 등의 코드 공유 플랫폼에만 공개되는 것이 대부분
- 새로운 모델을 빠르게 접하고 상황에 맞게 변형해서 사용하기 위해서는, PyTorch에서 모델을 어떻게 정의하고 사용하는지 이해하는 것이 필요함.

## 3.3 Custom Model

**Custom model의 기본 구조**

- PyTorch에서 모델은 일반적으로 `torch.nn.Module` 클래스를
상속받아 정의
- Custom model을 정의하기 위해서는 아래 두 가지 메서드를 꼭
작성해야 함.
    - __init__:  `super().__init__()`을 통해 부모 클래스 (nn.Module)를 상속 및 초기화한 후, 모델의 레이어와 파라미터를 초기화
    
    → super().__init__(): 부모 클래스(nn.Module)를 초기화하여 nn.Module의 기능을 사용할 수 있음. 이를 통해, 입력값에 대한 연산을 진행하거나, 선언한 모델의 parameter에 접근할 수 있음.
    
    - forward: 입력 데이터(dataset, dataloader로 받은 값)에 대한 연산을 정의
    
    ```python
    class CustomModel(nn.Module):
    	def __init__(self):
    		super().__init__()
    		self.encoder = nn.Linear(10, 2)
    		self.decoder = nn.Linear(2, 10)
    	
    	def forward(self, x):
    		out = self.encoder(x)
    		out = self.decoder(out)
    		return out
    	
    model = CustomModel()
    ```
    

# 04 역전파와 최적화

학습에 필요한 기본 구조와 PyTorch의 자동 미분 엔진인 AutoGrad대해 알아봄

## 4.1 학습의 기본 구조

**PyTorch에서 사용되는 훈련 과정의 일반적인 형태**

1. **optimizer.zero_grad()**: 이전 gradient를 ‘0’으로 설정

→ PyTorch는 기본적으로 gradient를 누적하여 사용. 만약 이전 gradient를 ‘0’으로 초기화하지 않는다면, gradient가 누적되어 데이터가 계속 중복된 채 학습에 사용됨.

1. **output = model(data)**: 모델을 사용하여 입력값(데이터)에 대해 연산
2.  **loss = loss_function(output, label)**: loss 값 계산
3. **loss.backward()**: loss에 대한 gradient 계산 → 이때, AutoGrad를 통해 자동으로 gradient 계산
4. **optimizer.step()**: 계산된 gradient를 사용하여 각 파라미터를 업데이트

```python
for epoch in range(num_epochs):
	for data, label in train_dataloader:
		optimizer.zero_grad()
		
		output = model(data)
		
		loss = loss_function(output, label)
		
		loss.backward()
		
		optimizer.step()
```

## 4.2 AutoGrad

**loss.backward()는 AutoGrad를 기반**

- AutoGrad는 tensor의 **연산에 대한 미분을 자동으로 계산**하기 위해, 내부적으로 computational graph를 생성
    - Computational graph: 수학적 계산을 노드(node)와 엣지(edge)의 그래프로 표현한 것. 그래프를 통해 연산의 흐름이 기록됨
    - 노드: 수학적 연산을 나타냄. 예를 들어 덧셈, 곱셈, 뺄셈 등의 기본적인 연산을 나타낼 수 있음
    - 엣지: 연산의 입력값 또는 출력값을 나타냄

- computational graph와 chain rule을 이용하여 gradient 계산을 자동으로 해줌. 이에 따라 프로그래머는 미분식을 일일이 구현하지 않아도 됨

# 05 추론과 평가

딥러닝 모델의 학습이 완료되었다면 테스트 데이터 셋에 대한 모델의 성능을 평가해야 함 → 추론과 평가

## 5.1 Inference

**학습한 모델을 이용하여, 입력 데이터에 대한 예측 결과를 내놓는 과정**

- 일반적으로 inference 시에는 `model.eval()`과 `torch.no_grad()`를 함께 사용
- **model.eval()**: 모델을 evaluation 모드로 전환. 이는 모델의 특정 레이어들(dropout, batchnorm → 학습에서만 사용, 추론에선 꺼줌)이 학습 과정과 추론 과정에서 다르게 작동해야 하기 때문
- **torch.no_grad()**: AutoGrad 기능을 비활성화. 추론 과정에서는 gradient 계산이 필요하지 않으므로, 이를 통해 메모리 사용량을 줄이고 계산 속도를 향상시킬 수 있음

```python
model.eval()
with torch.no_grad():
	for data in test_dataloader:
		pred = model(data)
```

## 5.2 Evaluation

**모델의 성능을 평가하는 과정**

- Inference 과정에서 도출한 예측 결과와 실제 라벨을 비교하여 모델의 성능을 평가
- 태스크에 맞는 metric을 선정하여 numpy array로 변환하여 외부 라이브러리를 사용하거나, PyTorch를 사용해 직접 구현하여 성능을 평가할 수 있음 → scikit-learn 사용 or PyTorch 구현

```python
# scikit-learn
import numpy as np
from sklearn.metrics import accuracy_score

model.eval()

preds = np.array([])
labels = np.array([])
with torch.no_grad():
	for data, label in test_dataloader:
		pred = model(data)
		
		pred = pred.detach().cpu().numpy()
		label = label.detach().cpu().numpy()
		
		preds = np.append(preds, pred)
		labels = np.append(labels, label)
	
	accuracy = accuracy_score(labels, preds)
```

```python
# PyTorch
model.eval()
correct = 0
total_length = len(test_dataloader)
with torch.no_grad():
	for data, label in test_dataloader:
		pred = model(data)
		
		correct += (pred.argmax(dim=1)==label).sum()
		
	accuracy = correct / total_length
```
