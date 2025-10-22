# 모니터링을 위한 TensorBoard와 WandB

1. **목적**

흔히 사용되는 TensorBoard와 WandB라는 두 가지 툴을 사용합니다. 모니터링을 통해 학습이 제대로 이루어지고 있는지 확인하고, 문제가 발생했을 때 이를 빠르게 파악하여 디버깅을 진행할 수 있음. 추가적으로 딥러닝 학습이 진행될 때, 성능이 향상되거나 저하되는 시점을 모니터링을 통해 파악할 수 있음

2. **목표**
- TensorBoard로 loss, metric(e.g. accuracy)을 로깅할 수 있음
- WandB로 loss, metric(e.g. accuracy)을 로깅할 수 있음
- WandB Sweep을 통해 하이퍼 파라미터 튜닝을 할 수 있음

## 1-1 TensorBoard

TensorBoard는 TensorFlow의 공식 시각화 툴킷. 개발이 지속되며 TensorBoard가 PyTorch에서도 사용될 수 있도록 확장. TensorBoard는 학습 과정에서의 metric(loss, accuracy 등) 변화를 트래킹하고, 모델의 구조를 그래프로 표현, 모델의 weight & bias에 대한 히스토그램을 쉽게 시각화할 수 있도록 지원

### TensorBoard의 주요 기능

- **Scalars**: 스칼라 metric(e.g. loss, accuracy)을 epoch에 따라 표시
- **Graphs**: 모델의 계산 그래프를 시각화. 모델의 구조와 입력값의 차원 변화를 이해하는 데 도움
- **Histograms**: 모델의 각 레이어에 위치한 weight와 bias를 히스토그램으로 나타낼 수 있음. 히스토그램을 통해 weight, bias의 분포를 변화를 이해하는 데 유용
- **Image Visualization**: 이미지를 시각화. 모델의 입력으로 사용되는 이미지를 시각화하는 데에 사용할 수 있음
- **Embedding Visualization**: 고차원 임베딩을 2D, 3D 공간에서 시각화할 수 있음. 분류 문제를 예로 들자면, 같은 class의 이미지 임베딩들이 2D, 3D 공간에서 군집(cluster)을 형성 → 모델이 이미지의 임베딩을 적절히 학습했다고 볼 수 있음

📚 참고할만한 자료:

- [TensorBoard - PyTorch 공식 문서](https://www.google.com/url?q=https%3A%2F%2Fpytorch.org%2Fdocs%2Fstable%2Ftensorboard.html)
- [PyTorch로 TensorBoard 사용하기 - PyTorch 공식 문서](https://www.google.com/url?q=https%3A%2F%2Ftutorials.pytorch.kr%2Frecipes%2Frecipes%2Ftensorboard_with_pytorch.html)

### tensorboard 실행 방법

1. 터미널에서 실행하는 경우 `pip install tensorboard`를 통해 tensorboard가 설치되고 나면 터미널에서 tensorboard를 실행

`tensorboard --logdir=[log-directory-path]` 여기서 [log-directory-path]에 writer를 통해 저장되는 로그의 위치를 작성

2. IPython에서 실행하는 경우 `!pip install tensorboard`를 통해 tensorboard가 설치되고 나면 IPython(e.g. colab, jupyter notebook)에서 tensorboard를 실행

`%load_ext tensorboard`

`tensorboard --logdir [log-directory-path]`

여기서 '%load_ext tensorboard'는 IPython 환경에서 확장 프로그램인 tensorboard를 사용할 수 있도록 하는 매직 커맨드

❗tensorboard에서 저장된 로그 파일을 반영하는 데에 업로드하는 주기가 존재. 만약 셸 실행 후, 바로 반영이 되지 않는다면 잠깐 기다렸다가 다시 셸을 실행해주면 반영됨

## 2-1 WandB 소개

WandB는 머신러닝 실험을 트래킹하고 시각화하며 결과를 공유할 수 있는 툴. WandB는 PyTorch뿐 아니라 TensorFlow, Keras 등의 주요 딥러닝 프레임워크와도 호환되며, 협업하는 팀과 모델의 모니터링 결과 및 시각화 자료를 공유할 수 있음

### WandB의 주요 기능

- 실험 관리: WandB를 사용하면 모델의 각 학습에서 생성되는 로그를 트래킹하고 관리할 수 있음
- 시각화: WandB는 학습 과정에서 생성되는 metric(e.g. loss, accuracy)을 실시간으로 시각화하는 기능을 제공. 모델의 weight, bias, gradient 등을 히스토그램으로 시각화할 수 있음.
- 하이퍼 파라미터 최적화: WandB의 sweep 기능을 사용하면 하이퍼 파라미터를 최적화하는 데 도움. 이를 통해 다양한 하이퍼 파라미터 설정을 자동으로 탐색하고, 이 중에서 최고의 성능을 기록한 모델을 확인할 수 있음

추가적으로 WandB는 로컬에서 기록된 파일을 모니터링하는 TensorBoard와는 달리, 웹에서 관리되기때문에 여러 서버를 사용해서 학습을 진행하는 경우 하나의 웹 페이지에서 실험들을 확인할 수 있는 장점을 가짐.

📚 참고할만한 자료:

- [WandB란? - 강력한 MLOps Tool](https://www.google.com/url?q=https%3A%2F%2Fpebpung.github.io%2Fwandb%2F2021%2F10%2F06%2FWandB-1.html)
- [WandB의 다양한 시각화방법](https://www.google.com/url?q=https%3A%2F%2Fpebpung.github.io%2Fwandb%2F2021%2F10%2F17%2FWandB-3.html)
