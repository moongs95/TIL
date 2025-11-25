# 🌟 학계에서의 자연언어처리 연구와 기업에서의 자연언어처리 서비스

---

# 1. 학계에서의 자연언어처리 연구 A to Z

## 1.1 주요 학회 및 연구 그룹

### • 언어공학연구회
- 한국어를 중심으로 자연언어 연구  
- 매년 **한글 및 한국어정보처리 학술대회(HCLT)** 개최  

### • NLP & AI 연구실들  
- KoreanCommonGen:  
  - 주어진 형태소 정보로 상식에 맞는 문장 재구성  
- KULLM:  
  - Polyglot-ko 기반 한국어 LLM 모델  
- KU-NMT Group:  
  - 고려대학교 기계번역 연구 그룹  
- BioBERT:  
  - 생물의학 텍스트 마이닝 특화 BERT  
- KOLD:  
  - 한국어 공격적 언어 탐지 데이터셋  
- H2KE:  
  - 이해하기 쉬운 한국 고전 번역 연구  
- Prompt Injection 연구:  
  - 프롬프트를 모델 파라미터에 직접 주입  
- Non-parametric Decoding:  
  - 검색 기반 생성 모델의 성능 향상  
- KR-BERT:  
  - 한국어 특화 BERT  
- USenseVector, UConceptVector, UTagger  
- **한통이**: NLP 기반 다국어 어휘 대역 서비스(다문화 대상)

---

## 1.2 자연어처리 소개

### 자연언어(Natural Language)
- 특정 집단에서 사용하는 모국어(한국어, 영어 등)  
- 모호성, 애매성 존재 → NLP의 핵심 목표는 이를 해결하는 것  

### 인공언어(Artificial Language)
- 특정 목적을 위해 만든 언어 (프로그래밍 언어 등)  
- 구조가 명확하고 모호성이 없음  

### NLP 정의
> **자연언어처리(NLP)는 컴퓨터를 이용해 인간의 언어를 이해하고 처리하는 학문 분야**

### 주요 NLP 응용
- 기계번역, 자동통역  
- 정보검색  
- 질의응답  
- 문서요약  
- 철자 교정  
- 대화 시스템 등  
- 활용 사례: Google, Naver, IBM Watson, Siri 등  

---

## 1.3 자연언어 분석 단계

1) **형태소 분석(Morphological Analysis)**  
2) **구문 분석(Syntax Analysis)**  
3) **의미 분석(Semantic Analysis)**  
4) **화용 분석(Pragmatic Analysis)**  

### 형태소 분석 예시
- “감기는”  
  - 감기(명사) + 는(조사)  
  - 감(동사) + 기(명사화) + 는  
  - 감(동사) + 기는(어미)  

### 구조적 모호성 예시
- *Time flies like light*  
- *A man sees a woman with a telescope*  
→ 여러 parse tree 가능  

### 의미 분석(Semantics)
- “말이 많다” → 말(horse) vs 말(speech)

### 화용 분석(Pragmatics)
- “그는 …” → 문맥 기반 지시어 분석(A or B?)

---

## 1.4 자연어 처리의 특징

- 자연언어는 **모호성**이 존재 → 분류/추론 문제로 변환하여 해결  
- 텍스트 데이터는 **고차원** → Word Embedding 필요  
- 대부분의 NLP 문제는  
  - **Sequence Labeling**  
  - **Sequence-to-Sequence(Seq2Seq)** 로 볼 수 있음  

---

## 1.5 자연어처리를 위한 딥러닝 소개

### 대량 데이터 필요  
→ Word Embedding 사용하면 더 효율적으로 학습 가능  

### RNN (순환신경망)
- 시퀀스 입력에 적합  
- 단어 길이가 일정하지 않아 RNN 사용  

### LSTM
- 긴 문장에서 앞부분 정보가 희석되는 문제 해결  
- 게이트 도입하여 long-term memory 유지  

### GRU
- LSTM 성능 유지 + 계산량 감소  

---

## 1.6 딥러닝 기반 자연어처리 기초 태스크

- Classification  
- Sequence Labeling  
- Seq2Seq  
- Pointer Network  
- MRC(Machine Reading Comprehension)  
- QA(Question Answering)

---

## 1.7 학계 연구 결론 요약

- 딥러닝 기반 한국어 구문 분석, 상호참조 해결 성과 증가  
- 다양한 딥러닝 알고리즘을 결합해 안정적 성능 향상  
- 연구 결과 오픈소스 공유가 중요  
- 정부 차원의 인센티브 및 지원 필요  

---

# 2. 기업에서의 자연언어처리 서비스 A to Z

---

# 2.1 국내 기업의 NLP 서비스

### ▸ NAVER – HyperCLOVA X  
- 한국어 LLM  

### ▸ LG AI Research – EXAONE 2.0  
- 전문가 특화  
- 멀티모달  

### ▸ SKT  
- **A.Dot**: 개인화 서비스  
- **NUGU bizcall**: 음성인식  

### ▸ KT – Mi:dm  

### ▸ Upstage – AskUp  

### ▸ Papago – 기계번역 (이미지 번역 포함)  
### ▸ Flitto – 번역·통역 플랫폼  
### ▸ 와이즈넛 – WISE i Chat V3  
### ▸ 코난테크놀로지 – 대화형 AI  
### ▸ 솔트룩스 – Talkbot Studio  
### ▸ 뤼튼 – 콘텐츠 생성 AI  
### ▸ 포티투마루 – LLM42  
### ▸ Maum.ai  
### ▸ ETRI, KISTI, KETI  
### ▸ Superb AI – 데이터 라벨링  
### ▸ 셀렉트스타, 크라우드웍스, 딥네츄럴(Labelr)

---

# 2.2 해외 기업의 NLP 서비스

### OpenAI
- Jukebox (음악 생성)  
- DALL·E  
- ChatGPT  
- GPT-4  
- Whisper (음성 인식)  

### Anthropic – Claude  
- 안전성·윤리 강조

### Google  
- Vertex AI  
- Bard  

### Meta – AI Sandbox  
- 광고용 생성 AI  

### Microsoft  
- Bing Chat  
- Copilot (문서·코딩 보조)  

### IBM – WatsonX  
### Amazon – Alexa  
### Baidu – ERNIE-ViLG 2.0  
### Salesforce – Einstein GPT  
### Speakeasy Labs – Speak  
### Character AI  
### DeepL – 번역  
### SYSTRAN – 기계번역  
### Scale AI – 데이터 기반 AI 플랫폼  
### Appen – 데이터 플랫폼  

---

# 3. 강의 전체 요약

---

# Ch1. 자연언어처리란 무엇인가?

- NLP 정의 및 어려운 이유  
- NLG / NLU  
- 일상 속 NLP 사례  

---

# Ch2. 자연언어처리를 위한 언어학 기초

### 형태론 (Morphology)
- 형태소 분석  
- 언어의 기본 의미 단위 연구  

### 통사론 (Syntax)
- 문장 구조 연구  
- 문법 규칙, 구조적 모호성  

### 의미론 (Semantics)
- 단어/문장의 의미 연구  

### 화용론 (Pragmatics)
- 명시되지 않은 의미, 문맥 기반 의미  

### 언어학 기반 NLP 사례
- NER  
- 문법 교정  
- Dependency Parsing  

---

# Ch3. 자연언어처리의 시작: 텍스트 전처리

### 중요성
- Garbage in → Garbage out  
- NLP는 전처리의 비중이 매우 큼  

### 한국어 전처리
- **KoNLPy**: Twitter, Komoran, Mecab 등  
- **NLTK**: 영어 NLP 대표 라이브러리  

### 정규표현식
- 텍스트 정제 필수 도구  

---

# Ch4. 자연언어처리의 다양한 응용 시스템

- 텍스트 분류(의도 분류·스팸·감성 분석)  
- 정보 추출(IE)  
- 기계번역(MT)  
- 대화 시스템(Dialogue)  
- 문서요약(Summarization)  
- MRC·QA  

---

# Ch5. 자연언어처리의 역사 A to Z

- 규칙 기반 → 통계 기반 → 머신러닝 → 딥러닝  
- 뉴럴 심볼릭  
- Pretraining  
- Transformer → LLM

---

# Ch6. 딥러닝 기반 자연언어처리

- 딥러닝 학습 구조  
- RNN / LSTM / GRU  
- Cross Attention  
- Transformer / Self-Attention
