# 파이토치 라이트닝

## 01 PyTorch Lightning 소개

### 1.1 PyTorch Lightning

#### PyTorch Lightning 배경

- 구현하는 코드의 양이 늘어나며 코드의 복잡성이 증가하고 이에 따라 다양한 요소들이 복잡하게 얽힘.
    - 데이터 전처리
    - 모델 구조
    - 학습 및 평가 루프
    - 결과 시각화
    
    → 이런 요소들은 서로 강한 관계성, 한 부분을 변경하면 다른 부분에도 영향을 미침.
    
    ex. 데이터 전처리 수정 → 모델 input shape 변경, 모델 구조도 변경되어야 할 수 있음
    
- PyTorch Lightning은 PyTorch에 대한 high-level 인터페이스를 제공하는 오픈소스 라이브러리
- High-level 인터페이스 : 복잡한 시스템이나 프로그램을 사용자에게 더 단순하고 이해하기 쉽게 만들어주는 인터페이스
- 딥러닝 모델 구축의 코드 템플릿으로써 기능을 하여 코드를 작성할 때 좀 더 정돈되고 간결화된 코드를 작성할 수 있음

→ 코드 템플릿 : 특정 프로그래밍 작업을 간소화하거나 반복적인 코드 작성을 줄이기 위해 미리 정의된 코드 블록이나 구조를 의미 ⇒ 집중할 부분에 집중할 수 있도록!

### 1.2 주요 특징

#### 코드의 추상화 및 하드웨어 호출 자동화

코드의 추상화 : 복잡한 로직을 간단한 인터페이스 뒤에 숨기는 것을 의미. 이를 통해 프로그래머는 내부 로직에 대해 신경쓰지 않고, 필요한 기능을 쉽게 사용할 수 있음

- 기존 PyTorch는 model, optimizer, training loop 등을 전부 따로따로 구현
- PyTorch Lightning은 LightningModule 클래스 안에 모든 것을 한 번에 구현하게 되어 있음
- 클래스 내부의 메서드명은 모두 PyTorch Lightning에서 요구하는 대로 똑같이 써야 하며, 그 목적에 맞게 코딩해야 함
- 추가로 PyTorch Lightning에서는 학습에 필요한 하드웨어(CPU, GPU)를 **자동**으로 호출하여 사용해 줌.
    - PyTorch 코드에서의 `.to(device)`와 같은 하드웨어 호출 코드를 따로 작성할 필요가 없음
    - 기본적으로 PyTorch Lightning에서는 사용할 수 있는 GPU가 있다면, GPU를 우선으로 사용
    

#### 다양한 콜백 함수와 로깅

콜백 함수 예시: early stopping

- PyTorch Lightning에서는 다양한 내장(built-in) 콜백 함수를 지원하며, 이를 사용해 딥러닝 학습과 연관된 특정 기능을 편리하게 사용할 수 있음
    - 초기 학습률(learning rate)을 자동으로 찾아주거나, 조기 종료(early stop)의 기능을 한 줄의 코드를 추가하여 구현
    - 다양한 로깅 도구를 지원하여 로깅해야하는 값을 편리하게 기록하고 TensorBoard, WandB 등 모니터링 툴을 쉽게 사용할 수 있음

#### 16-bit precision

→ quantization(양자화) : 모델 파라미터를 lower bit로 표현함으로써 계산과 메모리  access 속도를 높이는 경량화 기법

- 최근 딥러닝 연구에 사용되는 모델의 크기는 대체로 큰 경향성. 이럴 경우, 모델 전체를 GPU에 로드하여 학습하고 사용하기에 제한될 수 있음
    - ChatGPT 모델의 경우, 15억 개의 파라미터 수
    - 일반적으로 딥러닝 모델에서 실수를 표현하는 비트 수는 32-bit인데, 이를 줄여 모델의 계산 속도 향상과 메모리 사용량을 줄이고자 한 아이디어가 16-bit precision
    - PyTorch Lightning에서는 16-bit precision과 같은 복잡한 기능 또한 옵션으로 추가하여 편리하게 사용할 수 있음

## 02 LightningModule

### 2.1 LightningModule 소개

- PyTorch Lightning을 사용하기 위해서는 LightningModule 클래스를 상속받아 모델의 구조, 손실 함수, 학습 및 평가 방법과 최적화 알고리즘을 클래스에 선언
- 모델 구조와 학습 로직을 함께 클래스로 선언하여, 코드의 구조를 더욱 명확하게 만들고 코드의 재사용성을 향상

#### LightningModule 구성

- __init__: 초기화를 담당하는 메서드로 모델의 레이어를 초기화. 학습 및 평가 과정에서 사용되는 손실 함수, 메트릭을 선언
- forward: 모델을 통해 데이터가 연산 되는 과정을 정의
- configure_optimizers: 최적화 알고리즘과 학습률 스케줄러를 정의하고 반환. 반환할 때는 `return [optimizer], [scheduler]` 형식과 같이 순서를 맞춰야 함. 학습률 스케줄러는 생략해도 무방.

→ 학습률 스케줄러(learning rate scheduler) : 학습률 스케줄러는 딥러닝 모델을 학습하는 동안 학습률을 동적으로 조정하는 역할. 초기에는 큰 학습률을 사용하여 빠르게 모델의 최적 파라미터에 근접한 후, 점차 학습률을 줄여서 파라미터가 미세하게 조정되도록 스케줄링할 수 있음.

- training_step: 학습 데이터 셋의 미니 배치에 대해 손실을 반환하는 과정을 정의. 모델 학습과 관련된 `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`과 같은 코드를 작성하지 않아도 됨. → 내부적으로 실행

[공통]: 모델 평가와 관련된 코드인 `model.eval()`, `with torch.no_grad()`와 같은 코드를 작성하지 않아도 됨.(내부적으로 처리)

- validation_step: validation set의 미니 배치에 대한 모델의 성능(손실, 메트릭)을 확인하는 과정을 정의
- test_step: test set의 미니 배치에 대한 모델의 성능(손실, 메트릭)을 확인하는 과정을 정의
- predict_step: 추론해야 하는 데이터 셋의 미니 배치에 대한 예측 과정을 정의. 입력에 대한 모델의 예측값을 반환하거나 확률값을 반환하는 과정을 작성할 수 있음.

→ 모델 평가, inference에 사용되는 코드 3가지

```python
class Classifier(pl.LightningModule):
	def __init__(self):
		super().__init__()
		self.model = nn.Sequentual(
				...
		)
	
	def forward(self, x):
		pass
	
	def training_step(self, batch, batch_idx):
		pass
	
	def validation_step(self, batch, batch_idx):
		pass
	
	def test_step(self, batch, batch_idx):
		pass
	
	def predict_step(self, batch, batch_idx):
		pass
	
	def configure_optimizers(self):
		pass
```

## 03 Trainer

### 3.1 Trainer 소개

- Trainer는 LightningModule의 메서드를 이용해 모델 학습을 실행하는 클래스, `trainer.fit`을 실행시키면 LightningModule의 `training_step`, `validation_step` 메서드를 사용해 학습 → 반복적, 내부적으로 불러옴
- 콜백 함수를 적절한 시점에 호출하거나 로깅 도구를 통해 학습 과정을 기록하는 과정도 자동으로 관리
    - Trainer에서 Logger(e.g. TensorBoardLogger, WandBLogger ..)와 연동할 수 있음.

```python
model = Classifier(num_classes = 10, dropout_ratio = 0.2) # CIFAR10이라 class가 10

trainer = Trainer(
							max_epochs = 100,
							accelerator = 'auto',
							callbacks = [callbacks.EarlyStopping(monitor = 'valid_loss', mode = 'min')],
							logger = CSVLogger(save_dir = "./csv_logger", name = 'test')
)
train.fit(model, train_dataloader, valid_dataloader)
```

- 분산 학습 환경과 같이 복잡한 환경에서도 학습 환경을 자동으로 관리
    - 하나의 PC에서 GPU가 여러 개를 사용(`nn.DataParallel`)하거나, GPU가 있는 PC 여러 개를 사용(`nn.DistributedDataParallel`)해서 PyTorch 학습 코드를 작성할 때는 학습 환경 세팅을 구성하는 것이 매우 복잡 → 자동 관리 강점
- 학습 루프를 자동으로 관리하여, 에폭이나 데이터 로더와 관련된 반복문을 따로 명시하지 않아도 됨.

### 3.2 Trainer의 메서드

- **.fit()**: LightningModule(model)과 train_dataloader, val_dataloader를 인자로 받아, 학습을 진행
    - 이때, LightningModule의 `training_step`, `validation_step`, `configure_optimizers` 메서드를 호출하여 학습을 수행

→ 한 줄로 간단하게

- **.validate()**:  LightningModule과 val_dataloader를 인자로 받아 validation set에 대한 평가를 진행
    - 내부적으로 `validation_step`을 호출. `validate` 메서드가 완료되면, validation set에 대한 메트릭이 출력
- **.test()**: LightningModule과 test_dataloader를 인자로 받아 test set에 대한 평가를 진행
    - 내부적으로 `test_step`을 호출. `test` 메서드가 완료되면, test set에 대한 메트릭이 출력
- **.predict()**: LightningModule과 추론해야 하는 dataloader를 인자로 받아 모델의 결괏값을 반환받음.
    - 내부적으로 `predict_step`을 호출
