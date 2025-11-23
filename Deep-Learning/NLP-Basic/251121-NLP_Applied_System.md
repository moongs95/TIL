# 📘 자연어처리의 다양한 응용 시스템 (NLP Applications)

---

# 1. 자연어이해(NLU) 기반 하위 분야

---

## ## 형태소 분석기

### 형태소 분석
문자열을 이루는 **형태소·어근·접두사·접미사·품사** 등 다양한 언어적 속성 구조를 파악하는 작업

### 품사 태깅
형태소 분석 결과의 각 형태소에 **품사 태그를 부여**하는 과정

### 접근 방법
- **규칙 기반**: 전문가가 문장 분석 후 규칙 정의  
- **통계 기반**: 가능한 모든 형태소 후보 생성 → 확률 기반 선택  
- **딥러닝 기반**: 신경망이 형태소 분석 방법 학습

---

## ### HMM : Hidden Markov Model
- 통계적 마르코프 모델  
- 현재 출력은 **이전 상태의 은닉 상태**에 의해 결정됨  
- **상태 전이 확률**, **관측 확률** 기반  
- 단계  
  1. 초기 상태 선택  
  2. 전이확률 기반 다음 상태 선택  
  3. 관측값 생성  

---

## ### CRF : Conditional Random Field
- 시퀀스 라벨링에 널리 사용  
- 특징 함수(feature function) 기반  
- 단어, 위치 정보 등을 활용해 레이블의 적합도 계산

---

## ### Character-Level BiLSTM-CRF
- 한국어 띄어쓰기 문제 해결에 유리  
- **음절 단위 입력**  
- **양방향 Bi-LSTM → 형태소 단위 결합 → Bi-LSTM → CRF 레이어**  
- 형태소 태깅 결과 출력

---

# 2. 개체명 인식 (Named Entity Recognition)

### 개체 예시
- 사람(PS), 장소(LC), 기관(OG), 날짜(DT)  
- 의학 분야: 약물, 임상 절차, 단백질 등  
- 한국어는 TTA 태그셋 많이 사용

### 태깅 체계
#### BIO
- B: Begin  
- I: Inside  
- O: Outside  

#### BIESO
- B: Begin  
- I: Inside  
- E: End  
- S: Singleton  
- O: Outside  

---

# 3. 정보추출 (Information Extraction)

### 목적
비정형 텍스트에서 **구조적 트리플 (주어–관계–목적어)** 추출

### 정보추출 시스템 구조
1. 문장 분할  
2. 토큰화  
3. 품사 태깅  
4. 엔티티 추출  
5. 패턴 기반 관계 추출  

### 접근 방법
- **규칙 기반**: 사람이 관계 규칙 정의  
- **기계학습 기반**: 데이터에서 패턴 자동 학습  
- **그래프 기반**: 개체–관계 그래프로 구성  

---

# 4. 텍스트 분류 (Text Classification)

문장을 입력해 **사전에 정의된 클래스**에 분류하거나 군집화

### 분류(Classification)
지도학습 기반 범주화

### 군집화(Clustering)
비지도학습 기반 자동 유사도 그룹화

### 텍스트 분류 프로세스
전처리 → 토큰화 → 특징 추출 → 모델 학습 → 예측


### 특징 추출 기법
- TF-IDF  
- Information Gain  
- Mutual Information  
- Chi-Square  
- GINI Index  

### 대표 사용분야
- 감성 분석  
- 스팸메일 필터링  
- 대화 의도 분류  
- 상품 카테고리 분류  
- 혐오 표현 분류  

---

# 5. 감성 분석(Sentiment Analysis)

문장의 감정을 분석하는 NLP 분야  
- 규칙 기반  
- 통계 기반  
- 딥러닝 기반  
- 감정 사전 사용 사례 많음  
- 영화리뷰, 쇼핑 리뷰, 정치, 서비스 평가 등 활용

---

# 6. 스팸 메일 필터링
메일 텍스트 분석 후 스팸 여부 분류

---

# 7. 대화 의도 분류(Intent Classification)
사용자 발화의 목적 분류  
챗봇에서 많이 사용

---

# 8. 자연어생성(NLG) 기반 하위 분야

---

# 8.1 기계 번역(Machine Translation)

### 번역의 목표
주어진 문장 x → 가장 가능성 높은 번역 y 찾기  
즉, **argmax P(y | x)**

---

# 기계 번역의 흐름
- Rule-Based MT  
- Statistical MT (SMT)  
- Neural MT (NMT)

---

## Rule-Based MT (규칙 기반)
형태론 → 통사론 → 의미론  
언어 구조 기반 번역

---

## SMT (Statistical Machine Translation)
- 병렬 코퍼스 기반 확률 모델  
- 단어 기반 → 구(Phrase) 기반 → 계층적(Hierarchical) 기반 발전  
- Pre-ordering: 번역 전 어순 조정  
- Syntax-based SMT: 구를 특정 syntactic role 로 제한

---

## NMT (Neural Machine Translation)
- Encoder–Decoder  
- Seq2Seq  
- Attention  
- Transformer 기반

---

# 9. 질의응답(QA)

### 구성 요소
1. 질문 처리 (질문 유형, 정답 유형)  
2. 문서/문장 검색 (TF-IDF, 코사인 유사도 등)  
3. 정답 처리 (정답 후보 추출)

### 유형
- IR + QA  
- 기계독해(MRC)  
- 시각질문응답(VQA)  
- 멀티모달 QA  
- 대화형 QA  
- Large Vision-Language Model 기반 QA  

---

# 10. 대화 시스템(Dialogue System)

## 종류
- 사용자 주도  
- 시스템 주도  
- 목적 지향(Task-Oriented)  
- 일상 대화(Open Domain)

---

# 목적 지향 대화 시스템(Task-Oriented Dialogue)

예: 키오스크, 예약, 주문

### 파이프라인 방식
음성 → ASR → NLU → 대화 관리(DM) → NLG → TTS

### NLU 역할
- 도메인 확인  
- 의도(Intent) 파악  
- 슬롯 채우기(BIO 태깅)

### 대화 상태 추적(DST)
대화 히스토리 기반 현재 상태 관리

### End-to-End 방식
- 파이프라인의 한계 개선  
- 적은 규칙, 높은 확장성  
- 많은 대화 데이터 요구

---

# 일상 대화 시스템(Open Domain Dialogue)

## 검색 기반 (Retrieval-based)
- 기존 발화/지식을 검색  
- 정확도 높지만 데이터에 없으면 불가능

## 생성 기반 (Generative)
- RNN, Seq2Seq, Transformer  
- 발화 히스토리 기반 생성

## Hybrid 방식
- 검색 + 생성 조합

---

# 11. 문서 요약(Summarization)

## 분류
- Extractive  
- Abstractive  
- Multi-document  
- Long-document  
- Unsupervised (TextRank/PageRank)

---

# Extractive Summarization
원문 문장 중 핵심 문장 추출 방식

# Abstractive Summarization
새로운 문장으로 의미 재구성  
→ 더 어려움

# Multi-document Summarization
여러 문서의 핵심 내용을 하나로 요약

# Long-document Summarization
Sparse Attention 등으로 긴 문서 처리

# Unsupervised Summarization
PageRank 기반 중요도 계산 후 핵심 문장 추출

---

# 12. NLP의 특수 분야

---

## 12.1 Hate Speech
- 혐오 발언 탐지  
- Counter Speech Generation  
- Sarcasm Detection  

---

## 12.2 Deception Detection
- Fake News Detection  
- Fact Checking  

---

## 12.3 Machine Translation 관련 태스크
- Quality Estimation  
- Automatic Post Editing  
- Word-level AutoCompletion  
- Chat Translation  

---

## 12.4 Dialogue의 확장 태스크
- Persona-grounded Dialogue  
- Persuasive Dialogue  
- Dialogue Summarization  
- Knowledge-grounded Dialogue  

---

## 12.5 기타 NLP 태스크
- Question Generation  
- Document-level Relation Extraction  
- Instruction Tuning  
- LLM Evaluation  

---

## 12.6 한국어 관련 Task
- 고전어 데이터셋  
- 케어콜 데이터셋  
- 혐오 발언 데이터셋  
- 쓰기 평가  
- 문법 교정  
