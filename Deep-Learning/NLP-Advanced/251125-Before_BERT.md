# 🌟 BERT 이전 자연어처리 총정리 (Seq2Seq → RNN → Attention → Transformer)

---

# 1. Intro

BERT 이전까지 NLP의 주류였던 모델들(Seq2Seq, RNN, Attention, Transformer)을 전체적으로 정리한 내용이다.  
딥러닝 기반 NLP의 핵심 개념들이 어떻게 발전해왔는지 한눈에 이해할 수 있도록 구성하였다.

---

# 2. Seq2Seq

## 2.1 기계번역(NMT: Neural Machine Translation)
- 입력된 언어 문장을 다른 언어로 번역하는 Task  
- 자연어 → 숫자 형태의 컴퓨터 언어로 변환 후 처리  
  - 자연어 예: “이순신 장군은 우리나라의 영웅이다.”  
  - 컴퓨터 언어 예: `[2, 10661, 2073, 7339, 2079, 7073, 28674, 3]`

---

## 2.2 Encoder
- 자연어(텍스트)를 컴퓨터가 이해할 수 있는 벡터로 변환하는 장치  
- 입력 시퀀스를 **고정 길이 벡터(Context vector)** 로 변환  

## 2.3 Decoder
- Context vector를 입력받아 다시 자연어로 변환  
- 하나씩 토큰을 생성하는 구조(auto-regressive)

---

## 2.4 Seq2Seq 구조 핵심
- Encoder + Decoder  
- Encoder는 입력 문장을 벡터로 압축, Decoder는 이를 이용해 번역 결과 생성  
- 초기 Seq2Seq는 **고정 길이 벡터** 하나에 모든 정보를 저장 → 정보 손실 문제 발생  

---

# 3. RNN

## 3.1 RNN(Recurrent Neural Network)
- 현재 시점(t)의 계산이 이전 시점(t-1)의 hidden state를 기반으로 이루어지는 구조  
- 시퀀스 데이터를 처리하기 위한 대표 모델  
- "Recurrent(재귀적)" 구조를 사용하여 시간 순서 흐름 유지  

---

## 3.2 RNN 입력/출력 구조 종류

구조 | 설명 | 예시
---|---|---
One-to-One | 입력 1 → 출력 1 | 이미지 분류
One-to-Many | 입력 1 → 출력 여러 개 | 텍스트 생성, 음악 생성
Many-to-One | 입력 여러 개 → 출력 1 | 감성 분석, 언어 모델링
Many-to-Many(Tx=Ty) | 입력=출력 길이 동일 | 개체명 인식(NER)
Many-to-Many(Tx≠Ty) | 입력≠출력 길이 | 기계번역(NMT)

---

## 3.3 RNN 장단점

### 장점
- 시퀀스 데이터의 **순서적 특성** 학습 가능  
- 매 시점마다 이전 정보를 활용하여 **문맥 기억**  
- 입력·출력 길이가 달라도 처리 가능 → 유연함  

### 단점
- 시퀀스가 길어질수록 장기 정보를 잊는 **장기 의존성 문제(Long-term dependency)**  
- 이전 단계 계산 결과를 기다려야 하므로 **병렬처리 불가 → 느림**  
- **Gradient Vanishing / Exploding** 문제 발생  

---

# 4. LSTM & GRU

## 4.1 LSTM(Long Short-Term Memory)
- RNN의 장기 의존성 문제 해결을 위해 등장  
- 핵심 아이디어: **Cell State** + **Gate(Forget/Input/Output)**  
- 각 시점마다 어떤 정보를 기억/삭제할지 Gate가 조절  
- Gradient Vanishing 문제를 크게 완화  

---

## 4.2 GRU(Gated Recurrent Unit)
- LSTM을 더 단순화한 버전  
- Gate 2개(Update, Reset) / State 1개만 사용  
- 계산 효율성은 높지만, 장기 의존성에서는 LSTM보다 약함  

---

# 5. Attention

## 5.1 등장 배경
- Seq2Seq(RNN 기반) 구조는 **모든 정보를 Context Vector 하나에 압축** → 정보 손실  
- 문장이 길어질수록 성능 저하  
- 사람은 문장을 읽을 때 중요한 부분에 "집중"한다 → 이를 모델에 적용  

---

## 5.2 RNN + Attention 구조
- Decoder는 매 시점마다 Encoder의 각 Hidden State와 **유사도(score)** 를 계산  
- “어디를 참고해야 하는지” 스스로 학습  
- 디코더가 시점마다 다른 부분을 집중(Attend)할 수 있어 품질 향상  

---

# 6. Transformer

## 6.1 Transformer의 등장
- “Attention is All You Need”(2017)  
- RNN을 완전히 제거  
- 핵심 요소:
  - Seq2Seq 구조 유지  
  - **Self-Attention**  
  - **Multi-Head Attention**  
  - **Positional Encoding**  
  - 병렬 계산 가능 → 속도 혁신  

---

# 6.2 Self-Attention

### Self-Attention 정의
- 같은 문장("Self") 내 토큰들이 서로에게 Attention을 수행  
- 기존 Attention이 인코더↔디코더 간이라면,  
  Self-Attention은 입력 내부의 단어들끼리 관계를 학습

---

## 6.3 Self-Attention 계산 과정

1. 입력 X에 대해 학습 가능한 가중치 Wq, Wk, Wv를 곱해  
   **Query, Key, Value** 생성  
2. Query와 Key의 내적(dot product)으로 **attention score** 계산  
3. score를 scaling → softmax → attention 확률 분포 생성  
4. attention probs × Value 를 곱해 가중합 벡터 생성  
5. 이 벡터가 해당 위치의 새로운 hidden representation이 됨  

→ 이 과정이 모든 토큰에 대해 이루어짐

---

# 6.4 Multi-Head Attention

- Self-Attention을 여러 개의 head에서 **병렬** 수행  
- 서로 다른 Attention 관점을 학습  
- 마지막에 concatenate하여 종합 representation 생성  
- hidden_size가 num_heads로 정확히 나누어 떨어져야 함  

---

# 6.5 Positional Encoding

- Transformer는 RNN처럼 순서를 자연스럽게 반영하지 못함  
- 그래서 **sin/cos 기반 주기함수**로 위치 정보를 추가  
- Input Embedding에 더해서 위치 정보를 주입  
- 순서를 학습하도록 보완  

---

# 📌 핵심 요약

- RNN → 장기 의존성 문제  
- LSTM/GRU → 게이트로 해결  
- Attention → 필요한 정보를 선택적으로 집중  
- Transformer → RNN 제거 + 완전 병렬화 + Self-Attention 기반  
- BERT 이전 구조의 모든 핵심 흐름이 이 라인업에 포함됨
