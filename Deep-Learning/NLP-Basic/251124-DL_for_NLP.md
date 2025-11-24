# 🌟 딥러닝 기반 자연어처리 (Deep Learning for NLP)
_딥러닝 기초 → RNN/LSTM/Attention → Transformer → 사전학습모델 → 딥러닝 기반 NLP 응용까지 전체 흐름 정리_

---

# 0. 딥러닝 기반 자연언어처리 개괄

---

# 1. 딥러닝과 자연언어처리

## 1.1 딥러닝 개요

### • 인공지능(AI)
- 인간의 다양한 지능을 컴퓨터로 수행하도록 구현  
- 주변 환경을 인식하고 목표 달성을 위한 행동 계획  
- 다양한 알고리즘 및 장치 개발

### • 기계학습(ML)
- AI 하위 분야  
- 데이터를 통해 feature를 추출하고 모델 학습  
- 목표에 대한 명시적 프로그래밍 없이 알고리즘 학습

### • 딥러닝(DL)
- ML의 하위 분야  
- 퍼셉트론을 여러 층으로 쌓은 인공신경망(ANN)  
- 대규모 데이터 기반 자동 feature 학습  
- 인간의 뇌 구조를 모방한 신경망 계층을 통해 목표 학습

---

# 2. 딥러닝 학습 방법

## 2.1 딥러닝 모델 학습 구조

- 신경망 출력은 **가중치(파라미터)** 값에 의해 결정  
- 완전연결층 FC(m→n) = m×n개의 weight + n개의 bias  
- 딥러닝 모델: 수천~수십억 개 파라미터 사용  
- 파라미터 최적화 → 다양한 입력–출력 매핑 가능  
- 모델의 학습 = 파라미터를 손실 최소화 방향으로 조정하는 과정

---

## 2.2 Forward Pass (정방향 계산)
- 입력 → 모델 통과 → 예측 생성  
- 각 신경망 레이어의 가중치와 연산에 따라 출력이 결정

## 2.3 Backward Pass (역전파)
- 예측과 정답 차이 → 손실(loss) 계산  
- 손실을 파라미터별로 편미분 → Gradient 계산  
- Gradient가 가리키는 방향으로 파라미터 업데이트  
- Chain Rule(연쇄법칙) 이용  
- 출력층 → 입력층 순서로 미분을 역전파하기 때문에 **Backpropagation**이라고 부름

---

## 2.4 손실 함수(loss function)
- 예측–정답 차이를 수치화  
- 모델의 성능 평가 지표이자 파라미터 업데이트 기준  

## 2.5 Gradient
- 손실 감소 방향, 기울기  
- 파라미터 업데이트 방향 제공  
- 데이터 전체에 대해 반복 적용 → 최적 파라미터 학습

---

# 3. 딥러닝 기반 자연어처리 기초

---

# 3.1 Sequence-to-Sequence (Seq2Seq)

입력 시퀀스 → 출력 시퀀스로 변환하는 모델  
Encoder (NLP 이해) + Decoder (NLP 생성)

### • Encoder
- 입력 문장을 **고정 길이 벡터(context vector)** 로 변환  
- 정보를 압축하여 인코딩(auto-encoding)

### • Decoder
- context vector 기반  
- auto-regressive 방식으로 출력 시퀀스 생성  

---

# 3.2 RNN (Recurrent Neural Network)

### • RNN 개념
- 시계열/언어 데이터 **순서 의존성** 반영  
- 이전 hidden state + 현재 입력 → 현재 hidden state  
- RNN의 hidden state = 메모리 역할

### • RNN 수식 구성 요소
- Wax: 입력 가중치  
- Waa: 이전 hidden state 가중치  
- Wya: 출력 가중치  
- xt: 입력  
- g1: tanh  
- g2: softmax 등 출력 함수

### • 학습
- Loss = 모든 시점의 loss 합  
- Backpropagation Through Time(BPTT): 시간 축을 따라 역전파  

### • RNN 구조 유형
- One-to-one  
- One-to-many  
- Many-to-one  
- Many-to-many  
- BiRNN(양방향 RNN)  
- Deep RNN(적층 RNN)

---

## 3.3 RNN의 장단점

### 장점
- 모든 길이의 시퀀스 입력 가능  
- 파라미터 공유 → 모델 크기 일정  
- 과거 정보 반영 가능

### 단점
- 순차 처리 → 병렬화 어렵고 속도 느림  
- long-term dependency 문제  
- 미래 정보 고려 불가  

---

# 3.4 LSTM & GRU

## Gradient Vanishing / Exploding 문제
- 긴 시퀀스에서 gradient가 0으로 수렴(소실) 또는 급증(폭주)  
- tanh 반복 곱 → gradient 소실

---

## LSTM(Long Short-Term Memory)
- RNN의 long-term dependency 문제 해결  
- Cell state + 3개의 gate 사용

### LSTM 구성 요소
| Gate | 역할 |
|------|------|
| Forget Gate | 무엇을 잊을지 결정 |
| Input Gate | 새로운 정보를 얼마나 반영할지 |
| Candidate Cell | 새로 입력될 정보 |
| Cell State | 기억을 유지하는 장기 메모리 |
| Output Gate | 다음 hidden state 생성 |

### LSTM 장점
- 오래된 정보도 유지 가능  
- gradient 소실 문제 완화  

---

## GRU(Gated Recurrent Unit)
- LSTM의 단순화 버전  
- Gate 2개: Update, Reset  
- 상태 1개: hidden state  
- 계산량 ↓, 속도 ↑  
- 그러나 long-term dependency는 LSTM보다 약함

---

## RNN / LSTM / GRU 비교

| 구분 | RNN | LSTM | GRU |
|------|-----|------|------|
| 게이트 | X | 3개 | 2개 |
| Long-term Memory | 낮음 | 매우 좋음 | 중간 |
| Gradient Vanish | 심함 | 적음 | 적음 |
| 계산 복잡도 | 낮음 | 높음 | 중간 |

---

# 4. Attention

---

## 4.1 Attention의 필요성
기존 Seq2Seq의 단일 context vector는 정보 압축 → 정보 손실 발생  
→ 각 time step마다 선택적으로 input의 특정 부분에 집중

---

## 4.2 Attention Mechanism

### 핵심 개념
- Query: 디코더의 현재 hidden state  
- Key / Value: 인코더 hidden state  
- Query–Key 간 유사도 계산 → Attention Score  
- Softmax로 확률화 → Attention distribution  
- Value와 가중합하여 context vector 생성  

---

## 4.3 Attention 함수 종류
- Dot-product  
- Bilinear  
- MLP-based attention  

---

## 4.4 Attention map
- Attention score 시각화  
- 디코더 시점마다 input 단어와의 관련성 표시  

---

# 5. Transformer

---

# 5.1 Transformer 소개

기존 RNN 기반 Seq2Seq의 한계:
- 순차 처리 → 느림  
- Long-term dependency 문제 지속  
- 병렬 처리 어려움  

Transformer 해결책:
- Self-Attention 기반  
- 병렬 처리 가능  
- Long-range dependency 해결  

---

# 5.2 Transformer Encoder 구성

## 1) Input Embedding  
- 단어를 고차원 벡터로 변환  
- 학습 가능한 embedding layer

## 2) Positional Encoding  
- RNN과 달리 순서를 학습하지 못하므로 별도로 위치 정보 추가  
- 병렬 연산 가능

## 3) Self-Attention  
입력 내의 모든 토큰이 서로의 관련성을 계산  
- Query, Key, Value 생성  
- Scaled Dot-Product Attention 수행  
- Self-Attention = 내부 토큰 간 attention  
- (Cross-attention은 Encoder–Decoder 역할에서 발생)

## 4) Multi-Head Attention  
- Self-attention을 여러 “head”로 병렬 수행  
- 다양한 의미적 패턴 학습  
- 각각의 head 출력 concat → linear projection

## 5) Residual Connection + Layer Normalization  
- Residual: 입력 + 출력 합  
- LayerNorm: 안정적 학습  

## 6) Feed Forward Network  
- 위치별 독립적 FFN  
- 비선형 변환 적용  

---

# 5.3 Transformer Decoder 구성

### Causal Attention (Masked Self-Attention)
- 미래 토큰을 참조하지 않도록 masking  
- autoregressive 구조 유지

### Encoder-Decoder Attention
- 디코더 Query  
- 인코더 Key/Value  
- 입력–출력 관계 연결

### Linear + Softmax
- vocabulary 차원으로 매핑  
- 다음 단어 확률 예측

---

# 6. 딥러닝 기반 자연어처리 응용분야

---

# 6.1 딥러닝 기반 사전학습 모델(Pretrained Models)

Transformer 기반 Pretraining 대표 모델들

---

## **BERT (Encoder-only)**
- Bidirectional Encoder  
- MLM(Masked LM)  
- NSP(Next Sentence Prediction)  
- 입력 임베딩 = Token + Segment + Position  
- 양방향 문맥 → 이해(understanding) 특화

---

## **GPT-2 (Decoder-only)**
- 단방향(Left-to-right)  
- CLM(Causal LM)  
- 생성(generation) 특화  
- Token/Segment/Position Embedding 사용

---

## **BART (Encoder–Decoder)**
- BERT + GPT 통합  
- Denoising Autoencoder  
- 강력한 Seq2Seq 모델  
- Summarization, Translation, Generation 강함

---

# 6.2 딥러닝 기반 형태소 분석 & 품사 태깅
- CNN 기반 형태소 분석  
- Character-level BiLSTM-CRF  

---

# 6.3 딥러닝 기반 의미역 분석(Semantic Role Labeling)
- 어절의 의미적 역할 분류  
- BERT → LSTM-CRF 조합 사용

---

# 6.4 딥러닝 기반 개체명 인식(NER)

NER 시스템 구조:
1) Input Representation  
   - Word embedding, Char embedding, POS, Gazetteer  
2) Context Encoder  
   - CNN, RNN, Transformer  
3) Tag Decoder  
   - Softmax, CRF, RNN  

---

# 6.5 딥러닝 기반 질의응답(QA)

### Machine Reading Comprehension  
### Dense Passage Retrieval  
### Document Reader  
### IR→Reader pipeline  

샴 네트워크 기반 QA  
- 문장 의미 유사도 기반

Attention 기반 QA  
- 질문–문서 상호작용 반영  

---

# 6.6 딥러닝 기반 기계 번역(NMT)
- End-to-end neural MT  
- Transformer MT  
- 기존 SMT 대비 품질 비약적 향상  

추출/생성 요약 모델:
- BART Summarization  
- KoBART  
- BERTSum  

---

# 6.7 딥러닝 기반 문서 요약

Pretrained summarization models:
- STEP  
- PEGASUS  

---

# 6.8 딥러닝 기반 대화모델

Dialogue System:
- TOD (Task-Oriented Dialogue)  
- ODD (Open-domain Dialogue)  

TOD-BERT 등 전문 모델 존재

---

# 6.9 딥러닝 기반 문장 생성

## RNN 기반 생성  
## Transformer Decoder 기반 생성  
- GPT 계열  
- 자연스러운 생성 특화
