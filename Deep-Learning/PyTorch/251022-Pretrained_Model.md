# 전이 학습

## 1.1 Pretrained Model

- Pretrained model은 대규모 데이터셋을 기반으로 학습된 모델로, 학습한 task에 대한 일반적인 지식을 갖고 있음
- 최근 GPT, PALM, Stable-Diffusion 등 대규모 데이터로 학습된 pretrained model이 등장하면서 중요성이 대두되고 있음

## 1.2 전이 학습이란?

- 사전 학습된 모델 (pretrained model)의 지식을 다른 task에 활용하는 것
- 모델이 이미 학습한 일반적인 지식을 기반으로 더 빠르고 효과적이게 새로운 지식을 학습할 수 있음
## 1.3 Fine-Tuning이란?

- 전이 학습의 한 방법
- Pretrained model을 그대로 혹은 layers를 추가한 후 새로운 작업에 맞는 데이터로 모델을 추가로 더 훈련시키는 방법

## 1.4 Domain Adaptation이란?

- 전이 학습의 한 방법
- A 라는 도메인에서 학습한 모델을 B라는 도메인으로 전이하여 도메인 간의 차이를 극복하는 것이 목적
    - 도메인이란 데이터가 속하는 분포 (e.g. 도메인 A : 실제 사진, 도메인 B : 애니메이션)

→ 도메인 간 관계성을 기반으로

## 1.5 유사한 다른 학습 방법들

- Multi-task learning : 하나의 모델을 사용하여 여러 개의 관련된 작업을 동시에 학습하면서 공통으로 사용되는 특징을 공유하는 학습 방식

ex. 이미지의 feature를 뽑아내는 CNN layer는 그대로, 고양이/강아지, 승용차/트럭/버스 → 여러개의 classifier를 두고 학습

- Zero-shot learning : 기존에 학습되지 않은 새로운 클래스나 작업에 대해 예측을 수행하는 기술 (e.g. CLIP) 완전히 다른 task를 학습한 모델 → 예측
- One/few-shot learning : 하나 또는 몇 개의 훈련 예시를 기반으로 결과를 예측하는 학습 방식

## 1.6 전이 학습 전략

### 도메인이 비슷할 때, dataset 크기에 따른 전략

- 비교적 작을 때 : 마지막 classifier만 추가 학습 (나머지 freeze)
    
    ∵ 데이터셋의 크기가 비교적 작기 때문에, 기존의 학습한 일반적인 지식을 전달하는데 집중
    
- 비교적 클 때 : classifier 뿐만 아니라, 다른 일부 layers도 추가 학습
    
    ∵ 기존의 학습한 일반적인 지식을 유지하며, 몇 개의 layer만을 추가 학습시켜 specific한 새로운 데이터셋에 대한 지식을 학습
    

### 도메인이 매우 다를 때, dataset 크기에 따른 전략

- 꽤 클 때 : 꽤 많은 layers를 학습해야 함.
    
    ∵ 도메인이 매우 다를 때, pretrained model이 이미 가지고 있는 지식을 꽤 많이 수정해야 하기 때문
    
- dataset의 크기가 매우 작을 때 : 학습이 어려움
    
    ∵ 도메인도 다르고, 데이터도 적으면 모델에서 지식을 추출하기 어렵기 때문
    
### Learning rate 전략

- Pretrained model의 일반적인 지식을 크게 업데이트 하지 않기 위해 작은 learning rate으로 학습
    
    → 전이학습하고자하는 데이터셋에 오버피팅이 되는 걸 막기 위해 적게 업데이트
    
    ※ 단, 마지막 FC Layer 만 업데이트 하는 경우 learning rate에 성능이 크게 영향을 받지 않음
    

# 02 Pretrained Model Community

 Transfer learning을 위한 pretrained 모델의 커뮤니티 → 어디서 가져오는지?

## 2.1 Pretrained Model Community의 필요성

- 최근 대규모 데이터셋을 사전 학습한 모델들이 발전
- 사전 학습된 대규모 모델을 쉽게 커스터마이징 (customizing) 해서 활용하고자 하는 수요 증대
- 이를 위한, pretrained model community 의 필요성 대두

## 2.2 Timm for CV

- Timm (Pytorch Image Model)은 computer vision (CV) 분야에서 사용하는 사전 학습 모델 라이브러리
- 2021년 paper with codes 에서 가장 인기있는 라이브러리 선정
- 현재 모델은 사전 학습된 가중치가 있는 모델은 총 1,163개 제공 (2023.7월 기준)
- Official Site : [timm](https://github.com/huggingface/pytorch-image-models)

### Timm 라이브러리 사용법

- timm.list_models() 로 제공되는 모델 리스트를 볼 수 있음
- timm.create_model(“model 이름”, pretrained = True) 로 사전 학습된 모델의 weight를 불러올 수 있음

## 2.3 HuggingFace for NLP, CV, …

- 오픈 소스 라이브러리 및 여러 도구 (demo, dataset)를 지원하는 커뮤니티
- 초기엔 natural language processing (NLP) 위주였지만, 최근 computer vision,
multi-modal, audio 등 다양한 분야의 pretrained 모델 라이브러리 제공
- 243,069 개의 모델과 46,033 개의 데이터셋 제공 (2023.07 기준) → Timm보다 많음
- Official site : [huggingface](https://huggingface.co/)

### Hugging Face 사용법

- 다양한 라이브러리와 다양한 모델이 있어 사용하고자 하는 모델을 찾아야함 (Hugging Face Docs)

- 찾은 모델의 예시를 참고하여 pip로 설치 (e.g. pip install transformers)
