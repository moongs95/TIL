# 디버깅

## Custom Dataset 구현 시 에러

### `__len__` 메서드에서의 에러

Custom Dataset을 구현하며 `__len__` 메서드에서는 필수적으로 데이터의 총 개수를 반환해야 함. 하드 코딩을 한다면 코드의 재사용성이 낮아짐

- `__len__` 반환 값이 데이터 수보다 적은 경우: 데이터 로더에서 반환하는 값만큼의 데이터를 사용하게 돼 모든 데이터를 사용하지 못함.
- `__len__` 반환 값이 데이터 수보다 많은 경우: 현재 가진 데이터의 최대 index보다 큰 값을 데이터 로더가 불러올 경우, 해당 index의 데이터를 찾지 못해 IndexError가 발생

📚 구글 검색 키워드: `pytorch custom dataset 인덱스 에러`

### `__getitem__` 메서드에서의 에러

위의 에러 상황과 같은 맥락으로 Custom Dataset 구현 시 IndexError는 자주 발생하는 에러 중 하나.  `__getitem__` 메서드 작성 시에도 주어진 데이터 수보다 초과하는 인덱스에 접근한다면, IndexError가 발생

### `__getitem__`에서 데이터 타입을 제대로 변환하지 않은 경우

TypeError는 PyTorch의 특정 레이어나 함수에서 요구하는 데이터 타입과 입력 데이터의 타입이 일치 하지 않을 때 주로 발생. 예를 들어 `nn.Embedding` 레이어는 입력으로 long 타입의 tensor를 요구하는데, float 타입의 tensor를 입력하면 type 문제로 인한 `RuntimeError`가 발생합니다. → 직접 dtype을 명시해 주어야 함.

📚 구글 검색 키워드: nn.Embedding Runtime Error

### Dimension Error

일반적으로 PyTorch에서 CNN 레이어는 입력 데이터의 차원을 B × C × H × W(B: 미니 배치 크기, C: 채널 수, H: 높이, W: 너비)로 입력(배치가 아닌 경우, C × H × W도 가능) 만약 이 차원과 일치하지 않는 데이터를 입력한다면, `Dimension Error`가 발생

## Custom Model 구현 시 에러

### Dimension mismatch error

mismatch error는 네트워크의 한 layer에서 다음 layer로 데이터를 전달할 때 입력 데이터의 차원과 계층이 기대하는 차원이 일치하지 않을 때 발생. 주로 잘못된 계층 구성 또는 데이터 전처리로 인해 발생.

```python
class CNN(nn.Module):
    def __init__(self, num_classes, dropout_ratio):
        super(CNN,self).__init__()
        self.num_classes = num_classes

        self.layer = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=5),  # [1,28,28] -> [16,24,24]
            nn.ReLU(),  # ReLU 활성화 함수 적용
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5), # [16,24,24] -> [32,20,20]
            nn.ReLU(),  # ReLU 활성화 함수 적용
            nn.MaxPool2d(kernel_size=2), # [32,20,20] -> [32,10,10]
            nn.Dropout(dropout_ratio),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5), # [32,10,10] -> [64,6,6]
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2), # 크기를 1/2로 줄입니다. [64,6,6] -> [64,3,3]
            nn.Dropout(dropout_ratio),
        )

        self.fc_layer = nn.Linear(64*5*5, self.num_classes) # [64*3*3] 차원을 입력으로 받아야 하나, 잘못된 입력 구성
        self.softmax = nn.LogSoftmax(dim = 1)
```

⇒ 직접 layer가 쌓일 때마다 차원이 어떻게 변하는지 작성해 두면 좋음

### Tensor manipulation

Dimension mismatch error와 같은 맥락으로 특정 레이어 통과 후 데이터의 차원을 고려하여 적절하게 조작해줘야 하는 경우가 많음. 예시로 Global Average Pooling을 사용하면 B × C × H × W의 입력 tensor는 B × C × 1 × 1로 변환.

이 경우, 다음 layer인 fully connected layer와 연산하기 위해서는 적절하게 tensor의 차원을 조작해줘야 함. 그렇지 않을 경우 dimension mismatch error가 발생 → flatten, view로 일차원으로 만들어 줘야 함.

## 학습 및 평가 시 에러

→ OOM 에러가 많이 남

### CUDA RAM out of memory

GPU의 메모리는 한정적이기에 모델을 학습할 때, GPU 메모리 사용량에 주의하며 학습 코드를 작성해야 함. 딥러닝 모델을 학습할 때, GPU RAM을 사용하는 경우 3가지

- 미니 배치 데이터
- 모델의 파라미터
- 역전파 수행을 위한 각 레이어의 출력 결과물

CUDA RAM out of memory 에러가 발생했을 경우, 대표적인 해결 방법

1. **batch_size 감소**: 미니 배치의 크기를 줄이면, 미니 배치 데이터 및 각 레이어의 출력 결과물의 메모리 사용량 또한 줄어듦
2. **torch.cuda.empty_cache 메서드 호출**: PyTorch에서 CUDA RAM 캐시를 비우는 메서드. PyTorch는 CUDA를 사용하여 GPU 연산을 수행하는데, 이 과정에서 메모리 관리를 효율적으로 하기 위해 일부 CUDA RAM을 캐싱함. `torch.cuda.empty_cache` 메서드를 호출하면 캐싱된 데이터를 비우게 되며 이를 통해 CUDA RAM을 확보할 수 있음.

📚 구글 검색 키워드: cuda out of memory 해결

### `detach`, `cpu`

PyTorch의 tensor는 기본적으로 gradient를 계산하고 역전파를 위한 정보를 가지고 있음. 이는 GPU 메모리에 추가적인 부담을 주며, 이 tensor를 NumPy 배열로 변환하려고 하면 에러가 발생.

이를 해결하기 위해 'detach()'를 호출하여 gradient를 기록하지 않아야 함. 또한, tensor가 GPU에 있을 경우, CPU로 옮긴 후에 NumPy 배열로 변환

## 흔한 실수 사례

1. **random seed를 고정하지 않고 하이퍼 파라미터 튜닝**: 딥러닝 모델의 결과는 초기화와 같은 random 요소에 크게 영향을 받음. 모델의 학습이 매번 동일한 조건에서 시작되도록 하기 위해, 실험의 재현성을 보장하는 데 중요한 역할을 하는 random seed를 설정해야 함.
2. **`optim.zero_grad()`를 하지 않는 경우**: PyTorch에서는 기본적으로 gradient가 누적되도록 설정되어 있음. 따라서 각 배치에서 역전파를 진행하기 전에 명시적으로 gradient를 0으로 설정하여 데이터가 누적되어 학습에 사용되지 않도록 해야 함.
3. **evaluation 단계에서 `model.eval()`을 하지 않은 경우**: BatchNorm이나 Dropout 같은 일부 레이어는 훈련 모드와 평가 모드에서 다르게 동작함. 딥러닝 모델을 구현하다 보면, 학습 코드와 평가 코드를 나누어 두는 경우가 일반적인데, 평가 코드에서 모델을 로드하기만 한다면 BatchNorm, Dropout 등의 일부 레이어는 정상적으로 작동하지 않음. 그래서 평가 시에는 `model.eval()`을 꼭 호출하여 평가 모드로 전환하는 것이 중요!
