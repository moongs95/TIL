# Large Language Model의 근간 이론들

## 1. In-Context Learning

### 1.1 Fine Tuning과의 차이점

#### Fine Tuning
- 대규모 코퍼스로 사전학습 후 적은 규모의 specific한 데이터셋에 대해 fine tuning
- **일반화된 task가 아닌, 일부 task에 대해서 능력을 집중적으로 향상**

#### Fine Tuning vs In-Context Learning

| 구분 | Fine Tuning | In-Context Learning |
|------|------------|---------------------|
| **파라미터 업데이트** | w update 하면서 gradient update | w update 없음 |
| **학습 방식** | 데이터셋으로 학습 | zero, one, few-shot 사용 |
| **입력** | 특정 task 데이터 | 지시사항 (+ 예시) |
| **출력** | task에 특화된 모델 | 바로 답 출력 |

---

### 1.2 N-shot Learning

#### In-Context Learning의 개념
- **원하는 task에 대한 간단한 설명을 함께 Input**
- 학습 과정에서 다양한 스킬과 패턴인식 능력을 키움
- **Inference 단계에서 원하는 task에 빠르게 적응**

---

#### Zero-Shot Learning

**정의**:
- **예시를 전혀 보지 않고 모델 업데이트 없이 새로운 태스크를 수행**

**특징**:
- Unsupervised multitask learners
- 독해, 번역, 요약, Q&A 등에 대해 zero-shot 능력이 꽤 있음
- **Zero-shot인데도 특정 태스크는 기존의 SOTA 모델들을 능가**

**예시**:
```
입력: "다음 문장을 영어로 번역하세요: 안녕하세요"
모델: "Hello" (예시 없이 바로 번역)
```

---

#### One-Shot Learning

**정의**:
- **단 한 개의 예시와, task에 대한 자연어 지시문이 제공**

**특징**:
- **이 방법이 사람이 소통하는 방법과 가장 흡사한 방법**

**예시**:
```
입력: 
"다음과 같이 번역하세요:
예시: '안녕' → 'Hello'
이제 번역: '고마워'"

모델: "Thank you"
```

---

#### Few-Shot Learning

**정의**:
- **모델은 추론 시 단 몇 개의 예시만을 참고해서 정답을 생성**

**특징**:
- 문맥과 원하는 답의 예시들이 주어짐
- 마지막으로 단 한 개의 문맥이 주어지면, 모델은 답을 생성
- **Task-specific한 데이터에 대한 필요를 크게 줄여줌** (즉, 몇 개 없어도 됨)
- **새로운 task에 효율적으로 빠르게 적응**

**예시**:
```
입력:
"다음과 같이 번역하세요:
예시1: '안녕' → 'Hello'
예시2: '고마워' → 'Thank you'
예시3: '잘 가' → 'Goodbye'
이제 번역: '사랑해'"

모델: "I love you"
```

---

#### 성능 비교
```
모델에 주어지는 예시의 수가 증가할수록 성능이 증가

Zero-shot < One-shot < Few-shot
```

---

#### In-Context Prompt의 중요성

**Chain of Thought Prompting**:
- **인간의 사고 흐름을 프롬프트에 녹임**
- 단순히 답만 제시하는 것이 아니라 추론 과정도 함께 제시

**예시**:
```
기존 방식:
Q: 15 + 27은?
A: 42

Chain of Thought:
Q: 15 + 27은?
A: 먼저 5 + 7 = 12, 1을 올림
   그 다음 1 + 2 + 1 = 4
   따라서 답은 42입니다.
```

---

## 2. How to build ChatGPT?

### 2.1 ChatGPT란?

#### 기본 특징
- **무의식적인 데이터 생성이 아닌, 모델에게 피드백을 주기 위한 데이터 생성**
- 사람의 지시를 반영하는 **"Instruction Tuning"**
- 피드백을 반영하는 **"Reinforcement Learning"**으로 구성

#### 성과
- **5일만에 사용자수 100만명 돌파**
- 생산성 향상

---

#### 기존 Chatbot과의 차이

**기존 Chatbot**:
- 적어도 4-5개 이상의 AI 모델들의 조합으로 구성
- 각 기능마다 별도 모델 필요

**ChatGPT의 Multi-Tasking**:
- ChatGPT는 chatbot에서 요구한 태스크를 **하나의 모델로 수행 가능**
- 이 외에도 훨씬 많은 태스크를 수행 가능
- **하나의 모델이지만, 하나의 서비스로도 볼 수 있음 (LLM as a Service)**
- 멀티태스킹, 학습뿐만 아니라 **추론 시에도 엄청난 Infra 관련 투자/경험/기술이 필요**

---

#### ChatGPT의 활용

**중요한 질문**:
- 어떤 태스크까지도 ChatGPT가 잘할까?
- ChatGPT API를 활용한 수많은 서비스들이 나올 것
- **ChatGPT의 역량 분석 필요 (Prompt Discovering)**

**ChatGPT Plugin**:
- Chat Interface로 어떤 서비스든 해보겠다는 의지
- ChatGPT 현재의 단점을 보완
- 외부 plugin 연동

---

#### 그래서.. ChatGPT란?

**핵심 구성**:
- **GPT-3.5를 파인튜닝한 모델**
- **InstructGPT의 "sibling model"**로, 학습 방식이 유사

**학습 데이터**:
1. **Demonstration data**: 데이터를 대화형으로 변환
2. **보상 모델(Reward model, RM)**: 유저의 선호도에 대한 모델
3. **강화학습(Reinforcement learning, RL)**: 보상 모델을 활용해 ChatGPT 업데이트

**요약**:
```
ChatGPT = Supervised Fine Tuning + RLHF
```

---

### 2.2 ChatGPT의 학습방법

#### Instruction Tuning의 필요성

**기존 언어모델의 문제**:
- 일반적인 언어모델은 다음 토큰을 예측하거나, 일부 태스크를 수행하는 것에 초점
- **사람의 지시에 따르지 못함**

**Instruction Tuning**:
- **사람의 명령(Instruction)을 따르도록 요구를 수행하도록 모델을 Fine Tuning하는 방식**
- 명령에 대한 파인튜닝과 강화학습을 하면 사용자의 의도를 더 잘 파악하고 답변
- InstructGPT(2022년 1월)의 실험 방식을 가미

---

#### Step 1: SFT (Supervised Fine Tuning)

**목표**:
- 예제 데이터 수집 후 supervised policy를 학습
- **SFT 모델 확보**

**과정**:
1. **데이터셋 구성**:
   - GPT가 주어진 지시문대로 행동하도록 가르치기 위한 데이터셋 생성
   - 지시 프롬프트와 그에 대한 결과물로 이루어진 데이터셋 정의
   - **Demonstration dataset: 13K prompts**

2. **라벨링 과정**:
   - 프롬프트 데이터셋으로부터 지시 prompt를 샘플링
   - 예: "8살 아이에게 달 착륙을 설명해보시오"
   - 라벨러는 프롬프트에 적합한 행동을 예시로 라벨링
   - 예: "몇몇 사람들이 달에 갔답니다 ~~"

3. **Fine-tuning**:
   - 이 데이터셋을 GPT-3에 대해 Fine-tuning
   - **SFT (supervised fine-tuning) 모델 생성**

**결과**:
- 지시문을 따르는 점에 있어 이 모델은 이미 GPT-3보다 성능이 우수
- 하지만 완벽하게 원하는 방식으로 작동하지는 않음

---

#### Step 2: Reward Model 학습

**목표**:
- **결과물에 대한 사람의 선호도 데이터를 학습**
- SFT로 생성된 결과물에 대해 사람의 선호도를 반영할 수 있는 Reward Model 학습

**데이터셋**:
- **Comparison dataset: 33K 개의 프롬프트**
- Reward Model 학습에 적합하게 구성

**구성**:
1. 프롬프트
2. 그에 따른 결과물들 (4-9개)
3. 그 결과에 대한 선호도 순위

**학습 목표**:
- 프롬프트가 주어질 때
- **Reward Model은 결과물들에 대해 사람의 선호도를 예측하는 방법을 학습**

---

#### Step 3: RLHF (Reinforcement Learning from Human Feedback)

**목표**:
- **강화학습을 사용해 Reward Model에 대해 policy를 최적화**
- Step1의 SFT 모델을 Step2의 보상모델을 사용해 강화학습을 통해 추가 fine-tuning

**알고리즘**:
- **Proximal Policy Optimization (PPO)**
- Reward Model을 보상함수로 사용하여 정책을 최적화
- InstructGPT가 사람의 피드백을 얻는 방법

---

#### PPO를 통한 fine-tuning 과정

**단계**:
1. **GPT는 프롬프트를 보고, 그에 대한 결과 문장들을 생성**
2. **생성된 문장들을 Reward Model이 평가하여 reward(보상)를 계산**
3. **보상 값이 GPT에게 주어지고 모델은 보상을 최대화하는 방향으로 정책을 업데이트**
   - 즉, 사람이 원하는 문장을 생성하는 방향으로 학습

**결과**:
- **사람의 지시에 따르면서, 유용하고 안전한 문장을 생성하도록 최적화**

---

#### RLHF로 윤리 완화
- 편향되거나 유해한 콘텐츠 생성 억제
- 사람의 가치관과 정렬

---

#### 결국 ChatGPT는...

**전체 과정 요약**:
1. **먼저 지시문에 따라 결과를 완성하는 초기 모델, SFT 모델을 완성**
2. **사람의 feedback을 모사하는 보상 모델(Reward model)을 확보**
3. **이를 통해 SFT 모델이 사람이 더 선호하는 결과를 추론하도록 강화학습을 진행**
```
ChatGPT = SFT → Reward Model → RLHF
```

---

### 2.3 ChatGPT 활용법

#### Persona Injection
- 특정 페르소나(역할)를 부여하여 응답 스타일 조정
- 예: "당신은 친절한 선생님입니다"

---

#### ChatGPT의 올바른 사용법: 프롬프트 구성

**4가지 구성 요소**:
1. **지시사항**: 모델이 수행해야 할 작업
2. **참고 데이터**: 맥락이나 배경 정보
3. **출력 지도**: 원하는 출력 형식
4. **사용자 입력데이터**: 실제 질문이나 데이터

---

#### 프롬프트 작성 원칙

**1. 짧고, 간결하고, 확실하게**
```
나쁜 예: "음... 혹시 가능하다면 이 텍스트를 요약해주실 수 있나요?"
좋은 예: "다음 텍스트를 3문장으로 요약하세요."
```

**2. 출력물도 형태 지정**
```
예시: "결과를 JSON 형식으로 출력하세요."
예시: "답변을 bullet point로 작성하세요."
```

**3. 길어지면 구역 지정**
```
예시:
"""
[지시사항]
다음 텍스트를 요약하세요.

[텍스트]
여기에 긴 텍스트...

[출력 형식]
- 핵심 내용 3가지
- 각 항목은 한 문장으로
"""
```

**4. 복잡하면 구역 지정**
```
### Task ###
### Context ###
### Examples ###
### Output Format ###
```

**5. 예시 들기**
- Few-shot Learning 활용
- 구체적인 예시 제공

---

#### 3Cs Framework

프롬프트 작성 시 고려사항:
1. **Clear (명확함)**: 명확한 지시
2. **Concise (간결함)**: 불필요한 정보 제거
3. **Complete (완전함)**: 필요한 모든 정보 포함

---

## 3. Parameter Efficient Fine Tuning (PEFT)

### 3.1 PEFT 소개

#### Full Fine Tuning의 문제점

**Full fine tuning of LLMs is challenging**:
- GPU나 하드웨어적으로 부족
- 시판 그래픽카드로 모델 전체를 fine tuning하는 것은 불가능
- Fine tuning된 모델은 이전의 사전학습된 모델과 똑같은 크기
- Fine tuning된 모델을 저장하고 사용하는 것 또한 (시간, 경제적으로) 비용이 많이 듦

---

#### Why PEFT?

**PEFT의 등장 배경**:
- 모델이 점점 커짐에 따라 발생하는 문제들 해결
- **PEFT(parameter-efficient fine tuning)은 이 두 가지의 문제를 해결하고자 등장**

---

#### Parameter Efficient Fine Tuning (PEFT)

**정의**:
- **사전 훈련된 언어 모델을 특정 작업이나 상황에 적용할 때, 가중치의 일부만 업데이트하는 파인 튜닝 방법**

**특징**:
- **일부만 fine tuning하므로 연산량이 대폭 감소**
- Fine tuning 할 때 발생하는 문제점 중 하나인 **catastrophic forgetting 완화**
- 적은 데이터에서 fine tuning 할 때나 도메인 밖의 데이터를 일반화할 때 더욱 좋은 성능

**효과**:
- **적은 수의 파라미터를 학습하는 것만으로 모델 전체를 fine tuning 하는 것과 유사한 효과**

---

#### PEFT의 장점

1. **Optimization of Resources (자원 최적화)**
   - 적은 계산 자원으로 학습 가능

2. **Mastery over Catastrophic Forgetting (파국적 망각 극복)**
   - 기존 지식을 잊지 않음

3. **Superiority in Data-Sparse Environments (데이터 부족 환경에서 우수)**
   - 적은 데이터로도 효과적

4. **Easy Portability and Deployment (쉬운 이식성과 배포)**
   - 작은 파라미터만 저장하면 됨

5. **Matching Performance with Economized Tuning (경제적 튜닝으로 성능 유지)**
   - 비용 대비 높은 성능

---

#### PEFT 프로세스
```
Initial Training Phase (초기 학습 단계)
  ↓
Customized Dataset Assembly (맞춤형 데이터셋 구성)
  ↓
Detection of Key Parameters (핵심 파라미터 탐지)
  ↓
Segment Selection (구간 선택)
  ↓
Fine-adjustment Process (미세 조정 과정)
  ↓
Performance Assessment (성능 평가)
  ↓
Progressive Refinement (점진적 개선)
```

---

### 3.2 PEFT 방법론

#### Pretrain, Prompt, Predict: A New Paradigm for NLP

**패러다임 변화**:
```
기존: Pretrain → Fine-tune → Predict
새로운: Pretrain → Prompt → Predict
```

---

#### Prompt란?

**일반적인 정의**:
- 프롬프트는 언어모델에 전달하는 질문이나 요청
- 사용자가 응답을 유도한다는 의미

**분류**:
- **Template을 사람이 문자 그대로 해석할 수 있는지에 따라 구분**

1. **Discrete Prompts (= Hard Prompt)**
   - 사람이 읽을 수 있는 자연어 프롬프트
   - 예: "다음 문장을 번역하세요:"

2. **Continuous Prompts (= Soft Prompt)**
   - 임베딩 공간에서 학습되는 연속적인 벡터
   - 사람이 직접 읽을 수 없음

**Prompt Learning**:
- 이러한 프롬프트(prompt)를 사용해 PLMs를 조정하는 방법

---

#### Prefix-Tuning

**개념**:
- **연속적인 태스크 특화 벡터(continuous task-specific vector = prefix)를 활용해 언어모델을 최적화하는 방법**

**방법**:
- LM 고정하고 각 layer의 input 앞에 task-specific vectors를 붙여 tuning
- 각 Task에 대하여 parameter를 tuning시켜 task마다 적합한 task-specific vectors를 도출

**효과**:
- **하나의 언어모델로 여러 개의 태스크를 처리할 수 있음 (prefix를 학습)**

---

#### Prefix-Tuning vs Fine-Tuning

**차이점**:
```
Fine-Tuning:
- 전체 모델 파라미터 업데이트
- 모델 크기만큼 저장 공간 필요

Prefix-Tuning:
- 각 Task에 대한 task-specific vectors(Prefix)를 계산하는 parameter만 fine-tuning
- 전체 모델을 fine-tuning 및 저장하는 방식에 비해 overhead 감소
```

**성능**:
- Table-to-text, summarization 등의 task에 대해 평가
- **Prefix-Tuning 모델이 Fine-tuning, Adapter를 적용한 조건보다 더 적은 파라미터를 학습하면서 더 높거나 유사한 성능을 달성**

---

#### Prompt Tuning

**개념**:
- **전체 파라미터를 튜닝하는 대신, 입력 프롬프트 임베딩만 학습하는 방법**
- 즉, 모델에 입력되는 프롬프트에 해당하는 weight만을 학습

**방법**:
- PLMs를 freeze하고 입력 텍스트에 추가되는 downstream task당 k개의 토큰만을 학습

**성능**:
- T5에 적용 시 GPT-3의 few-shot prompt design보다 우수
- **Prompt Tuning 사용 시, Domain Adaptation에 용이**
- 서로 다른 데이터로 학습, 평가 시에도 성능이 보존

---

#### P-Tuning

**개념**:
- **PLMs의 전체 weight를 fine-tuning하지 않고, continuous prompt embeddings만 tuning하는 방법**

**방법**:
- LM의 입력부에 **Prompt Encoder(Bi-LSTM)**를 두어 나온 출력 값을 Prompt의 Token Embedding으로 사용
- Task와 관련된 anchor tokens을 추가하여 성능 개선 (anchor token 값은 고정)
- **언어모델의 구조와 상관없이 적용 가능**

**성능**:
- NLU Task에서 GPT style model로 BERT style model보다 더 낫거나 비슷한 성능
- P-tuning 방식을 적용하여 SuperGLUE 벤치마크 측정 결과:
  - AE, AR 방식 모두 모든 세팅(fully-supervised & few-shot setting)에서 기존 fine-tuning 방식 대비 성능 개선
  - **특히 AR 방식의 성능 개선 폭이 더 크게 나타남**

---

#### LoRA (Low Rank Adaptation)

**개념**:
- **미세조정으로 달라지는 네트워크의 가중치를 근사할 두 개의 작은 행렬을 학습시키는 방법**
- 사전에 학습된 가중치 freeze
- Dense layer 변화에 따라 저차원의 분해 행렬을 최적화
- 앞뒤로 소규모 어댑터 추가

**방법**:
- **Pre-trained weight를 고정한 상태로 유지하며, dense layer 변화에 대한 rank decomposition matrices를 최적화**
- Low rank feed-forward adapter layer를 기존 output과 더하는 방식
- Adapter Layer만을 학습
- **기존 파라미터에 더해지는 형태이므로 추론 시간이 늘어나지 않음**

**효율성**:
- GPT-3의 경우 175B의 파라미터 가운데 **0.01%의 파라미터 개수만 이용**할 정도로 높은 효율성
- 작은 rank 값을 설정해도 성능이 유지
- **Huggingface에서 제공하는 peft 라이브러리를 통해 쉽게 사용 가능**

---

#### Quantization (양자화)

**목적**:
- **Training Time을 줄이는 게 아닌, Inference Time을 줄이는 것이 주 목적**

**개념**:
- **모델의 파라미터를 lower bit로 표현함으로써 계산과 메모리 access 속도를 높이는 경량화 기법**
- 보통 32비트 부동소수점 연산을 8비트 정수로 변환하는 방식 사용
- Pytorch, Tensorflow의 default data type = fp32

---

#### 양자화와 분위수

**양자화**:
- **실수 → 정수**
- 데이터를 더 적은 비트로 표현

**분위수**:
- 분위에 해당 값을 매핑
- 통계적 특성 보존
- raw data 읽는 속도 향상

---

#### 신경망에 적용

**방법**:
1. **신경망의 가중치와 활성화 함수 출력을 더 작은 비트 수로 표현하도록 변환**
2. 신경망의 파라미터 값은 평균이 0인 정규분포를 따르는 것이 알려져 있음
3. Block 안에서, [-1, 1]이 되도록 정규화 (최대 절댓값이 1이 되도록)
4. 이후 제시된 분위수에 맞게 양자화

---

#### QLoRA (Quantized Low Rank Adapters)

**개념**:
- **Q + LoRA**
- 4-bit Quantized language model into LoRA
- **기존 사전학습 모델의 weight는 양자화로 저장하고, LoRA에 의해 더해지는 weight는 그대로 16-bit finetuning을 유지**

**특징**:
- 사전학습 모델을 4-bit로 quantize하는 high-precision 방법
- **QLoRA를 사용하면 16-bit fine-tuning 성능을 유지하면서 단일 48GB GPU에서 650억 매개변수 모델을 fine tuning 가능**

**사용**:
- Huggingface에서 제공하는 transformers 라이브러리로 로드 가능
- peft 라이브러리와 연계를 통해 QLoRA 적용 가능

---

#### IA³ (Infused Adapter by Inhibiting and Amplifying Inner Activations)

**개념**:
- **Self-Attention, Cross-Attention에서의 Key, Value 값을 rescale해주는 벡터 추가**
- **Position-wise feed-forward network의 값에 rescale을 해주는 벡터를 추가**해서 모델을 튜닝하는 기법

**LoRA와의 차이**:
```
LoRA: Hidden state에 새로운 값을 더해주는 기법
IA³: Key, Value를 rescale하는 기법
```

**성능**:
- **기존에 공개된 LoRA보다 적은 파라미터를 사용하면서 높은 성능**

---

#### LLaMA Adapter

**개념**:
- **LLaMA 모델을 instruction 모델로 효율적으로 미세 조정하기 위한 방법**

**방법**:
- 학습 가능한 프롬프트 토큰을 상위 Transformer 레이어의 입력 텍스트 토큰 앞에 추가해 학습
- **1.2M의 적은 파라미터 수**로 각 어댑터를 유연하게 삽입하여 다양한 지식을 부여

**Multi-modal Conditioning**:
- Visual encoder(e.g. CLIP)를 통해 각 scale의 feature를 추출
- 학습 가능한 projection 적용
- 비전과 언어를 결합한 멀티모달 학습 가능

---

## 전체 요약

### 핵심 개념 비교

| 개념 | 설명 | 특징 |
|------|------|------|
| **In-Context Learning** | 예시를 통해 학습 없이 추론 | 파라미터 업데이트 없음 |
| **Fine-Tuning** | 특정 Task를 위한 전체 학습 | 모든 파라미터 업데이트 |
| **PEFT** | 일부 파라미터만 학습 | 효율적이고 경제적 |

---

### N-shot Learning 비교
```
Zero-shot: 예시 0개
  ↓ 성능 향상
One-shot: 예시 1개
  ↓ 성능 향상
Few-shot: 예시 2-10개
```

---

### ChatGPT 학습 과정
```
1. SFT (Supervised Fine Tuning)
   - 13K demonstration data로 학습
   - 기본 지시 수행 능력 확보
   ↓
2. Reward Model 학습
   - 33K comparison data로 학습
   - 사람의 선호도 학습
   ↓
3. RLHF (PPO)
   - Reward Model을 보상 함수로 사용
   - 사람이 선호하는 답변 생성하도록 최적화
```

---

### PEFT 방법론 비교

| 방법 | 학습 대상 | 특징 | 파라미터 수 |
|------|----------|------|-----------|
| **Prefix-Tuning** | Task-specific vectors | 각 레이어 입력 앞에 추가 | 중간 |
| **Prompt Tuning** | 프롬프트 임베딩만 | 가장 간단 | 적음 |
| **P-Tuning** | Prompt Encoder | Bi-LSTM 사용 | 중간 |
| **LoRA** | 저차원 분해 행렬 | 가장 효율적 | 매우 적음 (0.01%) |
| **QLoRA** | 양자화 + LoRA | 메모리 효율 최고 | 매우 적음 |
| **IA³** | Rescale 벡터 | LoRA보다 적은 파라미터 | 매우 적음 |

---

### 효율성 비교
```
Full Fine-Tuning: ████████████████████ (100%)
Prefix-Tuning:    ████                 (20%)
LoRA:             ██                   (10%)
QLoRA:            █                    (5%)
IA³:              █                    (5%)
```

---

### 주요 트레이드오프

#### 1. 학습 방식
```
Full Fine-Tuning:
✅ 최고 성능 가능
❌ 높은 비용, 느린 속도

PEFT:
✅ 낮은 비용, 빠른 속도
✅ Catastrophic Forgetting 방지
⚠️ 약간의 성능 저하 가능 (하지만 거의 비슷)
```

#### 2. 추론 방식
```
Fine-Tuning:
✅ 특정 Task 최적화
❌ 일반화 능력 상실

In-Context Learning:
✅ 일반화 능력 유지
✅ 파라미터 업데이트 불필요
⚠️ 프롬프트 설계 중요
```

---

### 실전 활용 가이드

#### ChatGPT 프롬프트 작성
```
1. 명확한 지시사항
2. 적절한 맥락 제공
3. 출력 형식 지정
4. Few-shot 예시 활용
5. 3Cs Framework 적용 (Clear, Concise, Complete)
```

#### PEFT 방법 선택
```
메모리가 충분한 경우: LoRA
메모리가 부족한 경우: QLoRA
가장 적은 파라미터: IA³
멀티태스크: Prefix-Tuning
가장 간단한 방법: Prompt Tuning
```

---

### 미래 방향

**In-Context Learning**:
- Zero-shot 성능 지속 향상
- Chain of Thought 고도화
- 더 복잡한 추론 능력

**RLHF**:
- 더 정교한 보상 모델
- 다양한 가치관 반영
- 윤리적 AI 구현

**PEFT**:
- 더 효율적인 방법론 개발
- 멀티모달 지원 강화
- 실시간 학습 가능

---

## 핵심 Takeaway
```
💡 In-Context Learning: 학습 없이도 강력한 성능

🎯 ChatGPT: SFT + Reward Model + RLHF

⚡ PEFT: 적은 비용으로 높은 성능

🔧 LoRA/QLoRA: 가장 효율적인 Fine-tuning

📝 Prompt Engineering: LLM 활용의 핵심

🚀 미래: 더 효율적이고 강력한 방법론 등장 예상
```
