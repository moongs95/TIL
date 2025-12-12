# 문맥기반 언어지식 표현 체계 이론

## 1. 초기의 사전학습 언어 모델

### 사전학습과 미세조정

#### 사전학습 (Pretrain)
- **목표**: unlabeled text corpora로부터 유용한 language representation을 학습
- 대용량 데이터를 얻을 수 있음
- 사전학습 모델은 언어를 잘 이해했기 때문에, downstream task에 대해 라벨링된 데이터를 추가로 학습하여 좋은 성능 획득 가능

**비유**:
- 글을 모르는 사람이 수능 국어를 공부 → 오랜 시간 소요, 학습 효율 낮음
- 사전에 글을 배운 사람이 수능 국어를 공부 → 빠른 학습, 높은 효율

#### 사전학습의 동기
- **라벨링된 데이터는 수가 부족하고 구축에 많은 시간과 비용 소모**
- 라벨링되지 않은 데이터는 인터넷에서 쉽게 획득 가능 (위키피디아, 뉴스 등)
- 라벨링되지 않은 데이터에 라벨을 추가하여 라벨링 데이터로 변환
- ⇒ **준지도학습(Semi-supervised Learning) / 비지도학습(Unsupervised Learning)**

---

### ELMo (Embeddings from Language Models)

#### 개요
- Pre-trained word representation을 얻기 위한 사전학습 모델
- **문제점**: 기존 단어 벡터는 동음이의어를 같은 벡터로 취급
  - 예: "사과" (과일) vs "사과" (사죄) → 같은 벡터

#### 해결 방법
- **동적 임베딩(Dynamic Embedding)**: 사전학습된 Bi-LSTM 사용
- 문맥에 따라 매번 다른 단어 임베딩 획득

#### 학습 과정
```
Forward LSTM 학습 + Backward LSTM 학습 = 최종 목적함수
```

#### 효과
- 모든 Task에 간단히 ELMo를 추가하면 기존 모델 대비 높은 성능 획득

---

### GPT-1 (Generative Pre-trained Transformer)

#### 특징
- **Unlabeled text corpora에 대해 Causal Language Modeling (CLM) 수행**
- **Transformer의 Decoder 구조만 사용 (Decoder-only)**
- **Auto-regressive 방식**
- Down-stream에 대한 Fine-Tuning으로 성능 향상
- 모델 구조의 작은 수정만으로 효과적인 Transfer Learning 수행

#### 사전학습: Causal Language Modeling (CLM)
- 문장의 이전 단어들을 기반으로 다음 단어를 예측
- Masked Self-Attention을 통해 구현
- **단방향(Unidirectional)** 모델

#### 미세조정 (Fine-tuning)
- 사전학습 후 **Task별로 모델 구조를 수정**하여 지도학습 진행
- **단점**: 모델 구조를 변경해야 함 (1:1 관계)
- 당시 12개의 Down-stream task 중 9개에서 SOTA 달성

---

### BERT (Bidirectional Encoder Representations from Transformer)

#### 특징
- **Unlabeled text corpora에 대해 MLM 및 NSP 수행**
- **Transformer의 Encoder 구조만 사용 (Encoder-only)**
- **Auto-encoding 방식**
- Down-stream에 대한 Fine-Tuning으로 성능 향상
- BERT 이후 다양한 사전학습 방법 및 구조 개선 연구 진행

#### 사전학습

**Task 1: Masked Language Modeling (MLM)**
- 문장 내 일부 토큰을 [MASK]로 교체
- 앞뒤 문맥을 기반으로 [MASK] 예측
- 전체 토큰 중 **15%를 [MASK]로 변경**
- **실제 문맥 이해 가능**

**Task 2: Next Sentence Prediction (NSP)**
- 두 문장이 연속된 문장인지 예측

#### BERT의 임베딩
입력은 3가지 임베딩의 합:
1. **Token embeddings**: 각 토큰에 대한 WordPiece 임베딩 벡터
2. **Segment embeddings**: sentence pair를 구분하는 정보
3. **Position embeddings**: 방향성 정보 제공

#### BERT의 Special Tokens
- **[CLS]** (Classification Token): 입력 첫번째 토큰, 전체 token sequence의 맥락이 반영된 벡터 출력
- **[SEP]** (Separator Token): 문장 쌍을 구분

---

## 2. 고급 언어 모델링 기법

### Encoder 기반 언어 모델

#### Encoder-only models (auto-encoding models)

**적합한 Task**:
- 문장 분류 (Sentence Classification)
- 개체명 인식 (Named Entity Recognition)
- 추출형 질의응답 (Extractive Question Answering)
- **자연어 이해(NLU; Natural Language Understanding) 과제에 적합**

**특징**:
- 모델이 입력 시퀀스 전체에 접근 가능
- 문맥 학습 방법이 핵심
- BERT가 MLM으로 Encoder-only 사전학습 모델의 시작을 열음

**대표 모델**: BERT, RoBERTa, ALBERT, DistilBERT, ELECTRA, XLNet, SpanBERT, DeBERTa, XLM

---

### XLNet (eXtended Language NETwork)

#### BERT의 문제점
- **MLM을 사용해 순차적인 언어 이해를 모델링하는 데 제한**

#### XLNet의 개선
- **순열 기반 언어 모델링(Permutation Language Modeling, PLM) 도입**
- 다양한 단어 순서를 고려하여 양방향 컨텍스트를 효율적으로 학습
- **자동 회귀(Auto-regressive) 특성과 자동 인코딩(Auto-encoding) 장점 결합**

#### Permutation Language Modeling (PLM)
- 토큰을 예측할 때 permutation 시퀀스 고려
- 재배열하고 원래 순서대로 예측
- **Mask를 사용하지 않아 자연스럽게 언어 이해**
- **양방향 context 고려** → AR 단점 극복
- **Masking 제거** → AE 단점 극복

---

### RoBERTa (Robustly Optimized BERT Pretraining Approach)

#### 특징
- **BERT의 hyper-parameter 및 학습 데이터 사이즈 등을 조절하여 최적화된 BERT 제시**
- **BERT의 구조적 변화 없이 모델 성능 개선** (크기만 키움)

#### 주요 변경사항
- 학습시간, Batch size, Max sequence length, Train data 증가
- **Next Sentence Prediction (NSP) 제거**
- **Dynamic masking 도입**

#### Dynamic Masking
- 동일한 데이터에 대해 매번 다른 위치에 마스킹 적용
- 모델이 다양한 패턴 학습 가능

---

### ELECTRA (Efficiently Learning an Encoder that Classifies Token Replacements Accurately)

#### 특징
- **GAN과 유사한 구조**: Generator + Discriminator
- **작은 모델인 Generator와 실제 모델인 Discriminator를 사용하여 효율적 학습**

#### 구조
- **Generator**: 입력 텍스트의 일부 토큰을 마스킹하고 예측
- **Discriminator**: 각 토큰이 실제 텍스트인지, Generator가 생성한 가짜 토큰인지 판별

#### 핵심: Replaced Token Detection (RTD)
- 모든 토큰에 대해 **진위 여부를 예측**
- BERT는 15%의 [MASK] 토큰만 학습 vs ELECTRA는 모든 토큰 학습
- 모델 크기, 데이터, 리소스가 동일한 조건에서 BERT 성능 능가
- **RoBERTa/XLNet 대비 1/4의 계산량만으로 비슷한 성능**

#### 기존 BERT의 단점 해결
1. **비일치 문제**: [MASK] 토큰은 사전학습에만 나타나고 미세조정에는 없음 → 해결
2. **비효율적 사전학습**: 토큰의 15%에서만 loss 계산 → 모든 토큰에서 계산

---

### ALBERT (A Lite BERT)

#### 목표
- **모델 크기를 줄이고 성능을 높이는 사전학습 모델 개발**

#### 문제점
- 메모리 문제 (OOM; Out Of Memory)
- 훈련 시간 증가
- Model Degradation (큰 모델이 오히려 낮은 성능)

#### 주요 기법

**1. Cross-layer Parameter Sharing**
- **모든 레이어에서 동일한 가중치를 재사용**
- 모델 크기 감소 및 학습 파라미터 수 감소

**2. Sentence-Order Prediction (SOP)**
- NSP → SOP로 변경
- 주어진 두 문장이 실제로 이어지는지 → **문장이 원래의 순서대로 주어졌는지**

**3. Factorized Embedding Parameterization**
- 큰 단어 임베딩을 **두 개의 작은 행렬로 분해**
- 기존 파라미터 `V×H`를 `V×E + E×H`로 줄임

---

### SpanBERT

#### 특징
- BERT의 MLM을 확장하여 **Span Masking** 도입
- 길이가 다른 연속적인 텍스트 스팬을 마스킹

#### Span Masking
- 시퀀스의 15%가 마스킹되도록 설정
- Span의 길이를 geometric distribution으로 선택
- 랜덤하게 span의 시작 위치 선택

#### Span-boundary Objective (SBO)
- 모델이 마스크된 스팬의 경계 토큰을 예측
- 스팬의 첫 번째와 마지막 토큰에 대한 정보 제공
- 스팬의 양 끝에 위치하는 토큰들이 서로 밀접한 관계를 가지도록 학습

#### 효과
- **질의응답(Question Answering)과 핵심 구 추출(Coreference Resolution)에서 뛰어난 성능**

---

### DistilBERT (Distilled BERT)

#### 목표
- **크기와 복잡성은 줄이면서 원래 BERT와 유사한 성능 유지**

#### 지식증류 (Knowledge Distillation)
- Teacher 모델(큰 BERT)로부터 지식을 추출하여 Student 모델(작은 모델)로 전달
- **BERT 대비 약 40% 작지만, 원래 BERT의 97% 성능 달성**

#### 손실 함수

**1. Distillation Loss (Teacher-Student Cross Entropy)**
- Teacher 모델의 소프트 타깃(softened probability distribution)을 Student가 모방
- Teacher와 Student의 출력 간 Cross Entropy 계산
```
Loss = -Σ t_i * log(s_i)
- t_i: teacher 모델의 클래스 i에 대한 예측 확률
- s_i: student 모델의 예측 확률
```

**2. MLM Loss (Student Masked Language Modeling Loss)**
- Student 모델도 BERT와 유사하게 MLM 수행
- 실제 토큰과 Student 예측 토큰 간의 Cross Entropy Loss
- 기존 BERT의 MLM 능력 모방

**3. Cosine Embedding Loss (Teacher-Student Cosine Embedding Loss)**
- Teacher와 Student의 출력 임베딩 벡터 간 방향 일치
- Cosine similarity를 최대화
- **Student가 단순히 확률 분포를 모방하는 것을 넘어 벡터 공간에서 비슷한 의미 구조 형성**

#### 성능
- BERT-base를 Teacher로 사용
- 파라미터 수: 180M → 110M
- 대부분 GLUE Task에서 BERT와 비견되는 성능 유지

---

### DeBERTa (Decoding-enhanced BERT with disentangled attention)

#### BERT의 문제점
- 상대적인 토큰의 위치 계산에 문제
- Position encoding 방식의 한계

#### DeBERTa의 개선
- **Disentangled attention mechanism** 도입
- **Enhanced mask decoder (EMD)** 사전학습 방법

#### Disentangled Attention
- **토큰 간의 콘텐츠(content)와 위치(position) 정보를 분리하여 처리**
- 상대적인 위치 정보를 반영하기 위해 relative position embeddings 사용

**상호작용 고려**:
1. **Content-to-Content (C2C)**: 단어의 의미적 맥락 이해 (기존 BERT의 self-attention과 유사)
2. **Content-to-Position (C2P)**: 단어의 내용과 위치 간의 관계 학습 (단어 위치에 따른 의미 정보)
3. **Position-to-Content (P2C)**: 특정 위치에서 어떤 단어가 등장할 가능성이 높은지 예측
4. **Position-to-Position (P2P)**: 위치 정보 간의 관계 (중요도 낮음, 고려 안함)

**기존 BERT와의 차이**:
- BERT: Content Vector에 Position Embedding을 단순히 더함 → C2C와 C2P만 고려
- DeBERTa: P2C를 추가로 학습

#### Enhanced Mask Decoder (EMD)
- 기존 BERT는 absolute position을 미리 예측
- DeBERTa는 softmax 이전에 absolute position embedding을 더하여 예측
- 더 정밀한 마스킹된 토큰 예측

---

### XLM (Cross-lingual Language Model)

#### 특징
- **다양한 언어를 모델링하기 위한 다국어 언어 모델**
- **MLM과 TLM(Translation Language Model)을 사용하여 사전학습**
- 언어 중립적인 특징을 학습하여 소수 언어(low-resource language) 또는 번역 작업에서 우수한 성능

#### Translation Language Modeling (TLM)
- 기존 비지도학습 사전학습과 달리 **지도학습 데이터인 병렬 데이터셋 사용**
- 소스 문장과 타깃 문장을 한 입력 데이터에 합쳐서 구성
- Cross-linguality 증가 목적

#### 효과
- MLM과 TLM을 함께 사용했을 때 모든 언어에서 좋은 성능
- 예: Nepali를 단독으로 학습하는 것보다 English, Hindi와 함께 사용했을 때 PPL이 가장 낮음
- **TLM이 언어의 중립적 특징을 학습함**

---

## 3. Decoder 기반 언어 모델

### Decoder-only models (auto-regressive models)

#### 적합한 Task
- 챗봇, 음악 생성 등 **유창성이 필요한 자연어 생성(NLG; Natural Language Generation) 과제**

#### 특징
- **Causal Language Modeling**으로 학습
- Masked Language Modeling으로 미래 시점의 단어들을 가리는 auto-regressive 방법 채택
- 사전학습 방법보다 **모델의 크기와 고퀄리티의 데이터 학습이 관건**

**대표 모델**: GPT, GPT-2, GPT-3, LaMDA, CTRL, Transformer XL

---

### GPT-2

#### 특징
- OpenAI가 개발한 언어 예측 모델
- **딥러닝 기반의 자연어 생성에 사용**
- GPT-1과 동일하나 모델 및 학습 데이터 크기와 약간의 모델 구조 변경
- **비지도학습만으로 NLP task를 해결할 수 있는 General Language Model에 대한 첫 연구**

---

### GPT-3

#### 특징
- GPT-2의 후속 모델
- **더 큰 모델과 더 많은 확장된 데이터셋 사용**
- **초기 LLM (Large Language Model)**
- **175B 파라미터** (당시 공개된 모델 중 압도적 크기, 현재도 매우 큰 규모)

#### 주요 성과
- 다양한 작업에 대해 **미세 조정 없이** 높은 성능 달성
- **Few-shot** 또는 **Zero-shot** 추론
- **In-context Learning의 시초**

---

## 4. Encoder-Decoder 기반 언어 모델

### Encoder-decoder models (sequence-to-sequence models)

#### 적합한 Task
- 번역, 요약, 생성기반 질의응답(generative question answering)
- **입력 문장을 이해하고 생성하는 자연어 이해 및 생성이 모두 필요한 과제**

#### 특징
- 입력 시퀀스를 이해하고 출력 시퀀스를 생성하는 능력 모두 필요
- 두 가지 측면을 모두 고려하는 사전학습 방법이 관건

**대표 모델**: BART, mBART, Marian, T5, Meena

---

### BART (Bidirectional and Auto-Regressive Transformer)

#### 배경
- **BERT**: Encoder 구조 → NLU Tasks에 유리하지만 NLG Tasks에 부적합
- **GPT**: Decoder 구조 → NLG Tasks에 유리하지만 양방향 Context 참조 불가, NLU Tasks에 부적합
- **해결**: Encoder-Decoder (Seq2Seq) 구조에 어울리는 Pre-training 기법 실험

#### 사전학습: Denoising Auto-encoding
텍스트에 노이즈를 더하고, 노이즈를 복구

**Denoising 방법**:
1. **Token Masking**: 토큰을 Masking하고 복구
2. **Token Deletion**: 토큰을 랜덤으로 삭제하고 복구
3. **Token Infilling**: 연속된 여러 개의 토큰 스팬을 masking하고 복구 (길이도 복구)
4. **Sentence Permutation**: 문장을 랜덤하게 섞고 복구 → **성능 향상의 핵심**
5. **Document Rotation**: 하나의 토큰을 랜덤으로 선택하고 문서를 섞어 해당 토큰이 시작 지점 찾기

**최적 조합**: Text Infilling + Sentence Shuffling

#### 미세조정
- **분류 태스크**: Decoder의 마지막 토큰 Hidden states를 사용하여 Classifier 학습
- **번역 태스크**: Randomly Initialized Encoder 사용 (단일 영어 모델이기 때문)

#### 성능
- NLU Task에서 당시 SoTA인 RoBERTa와 필적하는 성능
- **Generation Task에서 가장 높은 성능**

---

### MASS (Masked Sequence to Sequence Pre-training)

#### 특징
- **BERT와 Seq2Seq 학습 사이의 간극을 메우는 접근법**
- BERT의 MLM을 Seq2Seq으로 확장

#### 방법
1. 일정 길이의 연속적인 토큰 시퀀스가 입력 문장에서 마스킹된 후 인코더에 입력
2. 디코더에서 마스킹된 부분을 나머지 문장 정보를 바탕으로 예측하도록 사전학습

#### 목적
- 문장의 연속된 일부분을 마스킹하고, 나머지 부분을 사용하여 해당 부분 예측
- 문맥 이해 향상 및 시퀀스 생성 능력 강화

---

### T5 (Text-to-Text Transfer Transformer) - Google

#### 배경
- 기존 PLM은 Downstream Task에 대해 미세조정 시 **Task별로 서로 다른 레이어를 각각 만들고 학습**해야 함
- **해결**: NLP Task를 하나의 통일된 구조로 푸는 Text-to-Text Transfer 방법 제안

#### 특징
- 동일한 모델 구조 사용
- 미세조정을 위한 **Prefix 및 Task별 형식에 맞는 Text 전처리만** 수행
- 다양한 Downstream task의 input format을 **Text Sentence로 변환**

**예시**:
- CoLA, SST2, STSB, QNLI task 정보를 prefix로 제공

#### 사전학습 실험 결과
- **Encoder-Decoder 구조가 Decoder-only보다 효율적**
- **Objective**: MLM > Denoising > Language Modeling (CLM)
- **Masking rate는 15%가 가장 적절**

**최종 사전학습 설정**:
- Objective: MLM (Replace spans)
- Masking rate: 15%
- Span length: 3

#### 주요 성과
- 모델의 사이즈가 커질수록 높은 성능 달성
- **Encoder-Decoder 구조에서 최초로 모델과 데이터를 대규모로 키우는 Scale Up 연구**
- GPT-3와 달리 **Encoder-Decoder 구조가 더 높은 성능**을 나타냄을 강조

---

## 5. Scale Down 및 Scale Up

### 모델 Scale Down & Scale Up 정의

#### Language Model Scale Down
- 사전학습 모델의 크기를 줄이거나 유지하면서 모델의 성능을 높이는 모든 연구
- 예: ALBERT, 지식 증류(DistilBERT)

#### Language Model Scale Up
- 언어모델과 데이터의 크기를 키워서 모델의 성능을 급격히 높이는 모든 연구
- 예: LLM

---

### Scale Down

#### 딥러닝 모델 크기 증가에 따른 문제점

**1. 메모리 제한**
- 점점 커지는 배치 크기로 인한 메모리 제한
- 대형 언어 모델의 학습과 사용 시 메모리 문제 심각

**2. 학습/추론 속도**
- 모델 크기 증가로 학습과 추론 시간 증가

**3. 성능 저하**
- 큰 모델은 과적합 위험
- 방지를 위해 더 많은 양질의 데이터 필요

**4. 실용적 문제**
- 고가의 GPU 서버 필요
- 모바일이나 간단한 서비스 환경에서 사용 제한

⇒ **모델의 크기를 줄이는 Scale Down 연구 촉발**

#### 대표적인 사전학습 모델
- ALBERT
- DistilBERT
- TinyBERT
- MobileBERT
- Q-BERT
- Q8BERT

---

### Scale Up

#### 딥러닝 모델 크기 증가가 주는 이점

**1. 성능 향상**
- 모델 크기를 키우면 처리 능력과 정확도 상승

**2. 높은 성능**
- 큰 모델은 더 많은 데이터를 학습 가능
- 복잡한 패턴과 관계를 더 잘 이해하고 반영

**3. 다양한 Task 수행**
- 다양한 NLP Task에 걸쳐 뛰어난 범용성
- 예: ChatGPT, BARD, HyperCLOVA

**4. 작은 데이터로 일반화**
- 인간과 유사하게 **Zero-shot, Few-shot** 수행 가능

**5. 지식 통합**
- 대규모 모델은 방대한 정보를 내재화
- 풍부한 지식으로 다양한 곳에 사용 가능

⇒ **모델의 크기를 늘리는 Scale Up 연구 촉발**

---

### Scaling Laws for Neural Language Models

#### 핵심 원칙
- **LM의 성능은 모델의 파라미터 수, 데이터 사이즈, 계산량에 의존**
- **법칙**: 모델 사이즈가 8배 증가할 때 데이터가 약 5배 증가하면 성능 향상 보장

---

### 대표적인 사전학습 모델

#### No Instruction Tuning
- GPT-2, GPT-3
- T5
- MT5
- Polyglot, MegatronLM, BST

#### Instruction Tuning
- InstructGPT, ChatGPT, GPT-4
- Alpaca, Vicuna
- LLaMA, LLaMA2
- Pythia, Mistral

---

## 전체 정리 및 비교

### 모델 아키텍처별 특징

| 아키텍처 | 대표 모델 | 특징 | 적합한 Task |
|---------|---------|------|------------|
| **Encoder-only** | BERT, RoBERTa, ALBERT, ELECTRA, DeBERTa | 양방향 문맥 이해 | NLU (분류, NER, QA) |
| **Decoder-only** | GPT, GPT-2, GPT-3 | 단방향 생성 | NLG (텍스트 생성, 챗봇) |
| **Encoder-Decoder** | BART, T5, MASS | 이해+생성 | 번역, 요약, 생성형 QA |

### 주요 사전학습 기법

| 기법 | 설명 | 대표 모델 |
|-----|------|----------|
| **MLM** | 토큰 마스킹 후 예측 | BERT, RoBERTa |
| **CLM** | 다음 단어 예측 | GPT 시리즈 |
| **PLM** | 순열 기반 예측 | XLNet |
| **RTD** | 진위 토큰 판별 | ELECTRA |
| **Denoising** | 노이즈 복구 | BART |
| **Span Masking** | 연속 토큰 마스킹 | SpanBERT |
| **TLM** | 다국어 병렬 학습 | XLM |

### 효율성 개선 기법

| 기법 | 설명 | 대표 모델 |
|-----|------|----------|
| **지식 증류** | Teacher → Student 지식 전달 | DistilBERT |
| **Parameter Sharing** | 레이어 간 가중치 공유 | ALBERT |
| **Dynamic Masking** | 매번 다른 위치 마스킹 | RoBERTa |
| **Disentangled Attention** | Content와 Position 분리 | DeBERTa |

---

## 참고사항

### 발전 과정
```
초기: Word2Vec, GloVe (정적 임베딩)
  ↓
문맥 기반: ELMo, CoVe (동적 임베딩)
  ↓
Transformer: GPT-1, BERT (사전학습 + 미세조정)
  ↓
개선: RoBERTa, ELECTRA, ALBERT (효율성 개선)
  ↓
Scale Up: GPT-3, T5 (대규모 모델)
  ↓
최신: ChatGPT, GPT-4 (Instruction Tuning)
```

### 핵심 트렌드
1. **정적 → 동적 임베딩**: 문맥에 따라 변하는 표현
2. **단방향 → 양방향**: 전체 문맥 이해
3. **Task별 모델 → 통합 모델**: Text-to-Text Transfer
4. **작은 모델 → 대규모 모델**: Scale Up
5. **Fine-tuning → Few-shot/Zero-shot**: In-context Learning
