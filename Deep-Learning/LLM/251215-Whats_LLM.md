# Large Language Model (LLM) 이란

## 1. Large Language Model 개요

### 1.1 LLM의 정의

#### 기본 개념
- **기존 언어모델의 확장판**
- **방대한 파라미터 수를 가진 언어모델**

#### Large Language Models 시대 = Foundation Models의 시대
- **창발성(Emergence)**: 단일 모델로 여러 Task를 처리 가능
- **새로운 인공지능 개발 방식**: 육수 하나만 잘 끓이면 되는 시대
```
기존 방식: Task마다 개별 모델 개발
LLM 방식: 하나의 Foundation Model로 다양한 Task 수행
```

#### LLM의 핵심
- **Human Alignment (Human Feedback)**
- 인간의 피드백을 통한 모델 정렬
- 인간의 의도와 가치에 맞춘 모델 개발

#### LLM은 리셋 모먼트
- AI 개발 패러다임의 근본적 변화
- 새로운 시대의 시작

---

### 1.2 LLM의 등장 배경

#### Scaling Law (확장 법칙)
- 모델 크기, 데이터 크기, 계산량에 따른 성능 향상 법칙
- **특정 크기를 기점으로 급격한 성능 상승**

#### In-Context Learning
- 프롬프트 내에서 예시를 통해 학습
- 파라미터 업데이트 없이 새로운 Task 수행 가능

#### Instruction Tuning
- **Instruction Tuning은 언어모델의 성능을 향상시킴**
- 명령어 기반 학습으로 모델의 일반화 능력 개선

---

### 1.3 LLM의 제작 프로세스

#### LLM의 재료
1. **Infra**: Cloud, 운영환경, 하드웨어 등
2. **Backbone Model**: 기반 모델 아키텍처
3. **Tuning**: 비용 효율적인 백본 튜닝 기술
   - 어떻게 경량화할 것인가?
   - 반도체 기술로 행렬 연산 최적화
4. **Data**: 고품질 & 다량의 학습 데이터
   - Prompt, Instruction

#### LLM의 데이터 구성
- Webpages (웹 페이지)
- Conversation Data (대화 데이터)
- Books & News (책 & 뉴스)
- Scientific Data (과학 데이터)
- Code (코드)

#### LLM의 제작 과정 - Data Processing
```
Raw Corpus 
  ↓
Quality Filtering (품질 필터링)
  ↓
De-duplication (중복 제거)
  ↓
Privacy Reduction (개인정보 제거)
  ↓
Tokenization (토큰화)
```

#### LLM의 제작 과정 - Pre-training & Supervised Finetuning
1. **Pre-training**: 대규모 데이터로 기본 언어 능력 학습
2. **Supervised Finetuning**: 특정 Task를 위한 미세조정

#### LLM의 제작 과정 - 결과
- **Base LLM**: 사전학습만 완료된 기본 모델
- **Instruction Tuned LLM**: Instruction Tuning까지 완료된 모델

---

## 2. Large Language Model의 방향성

### 2.1 Data & Size

#### 데이터의 중요성
- **모델의 역량을 충분히 활용하고 있는가?**

#### Scaling Law의 재검토
- **"정말 더 크게?"**
- Chinchilla 연구: 모델 크기를 줄이고 training tokens를 늘렸더니 성능이 더 좋음

**질문**: 모델링과 데이터 중 어떤 것이 더 중요?
**답변**: 모델 크기도 늘리고 데이터 양도 늘리고!

#### 효율성 개선
- Self-attention의 시간 복잡도는 O(n²)
- 이를 줄이기 위한 다양한 연구 진행

#### 데이터 구성의 중요성
**예시: 한국어 LLM 학습 데이터 구성**
```
- blog
- cafe
- news
- comments
- kin (지식iN)
- modu
- Ency (백과사전)
- Others

→ 구성 비율을 조정했더니 성능이 달라지는 것을 확인
```

#### 핵심
- **중요한 것은 사전학습 모델의 크기!**
- Small LLM은 효과가 미비함
- **LIMA: Less Is More for Alignment** (적은 고품질 데이터로도 충분)

---

### 2.2 Multimodal (멀티모달)

#### Vision and Language
- **인공지능은 인간을 모방하는 것**
- 다양한 데이터를 다룸
- **언어에만 국한되지 않음**

#### 핵심 개념
```
Multimodal Data → Foundation Model → Common Embedding Space
```

#### 대표 모델
- PaLM-E
- Kosmos-1 & 2
- GPT-4V(ision)
- Gemini
- Meta의 ImageBind
- OpenAI Family

---

### 2.3 Multilingual (다국어)

#### 다국어 처리의 중요성
- 글로벌 서비스를 위한 필수 요소

#### 대표 모델
**Open Source 진영**:
- BLOOM
- Meta AI
- PaLM2 (한국어 예시 포함)
- OpenAI (95개 언어 이상 지원)

---

### 2.4 Synthetic Data (합성 데이터)

#### 합성 데이터의 부상
- **Generative Model 활용**
- **Synthetic Data의 비중 상승 추세**

#### 주목할 만한 성과
- **심지어 강력하고 사람보다 우수한 Case 발생**
- **사람보다 레이블링 성능이 뛰어남**

#### 의미
```
기존: 사람이 직접 레이블링
현재: AI가 생성한 합성 데이터로 학습
     → 더 빠르고, 더 저렴하고, 때로는 더 정확함
```

---

### 2.5 Domain Specialized (도메인 특화)

#### 개념
- **도메인 특화를 통해 니즈를 충족**
- 의료, 법률, 금융 등 특정 분야에 특화된 LLM

#### 장점
- 해당 도메인에서 더 높은 성능
- 전문 용어 및 맥락 이해 능력 향상

---

### 2.6 Evaluation (평가)

#### 평가 방식의 다양화
- **정확도나 정밀도와는 다른 평가 방식**

**새로운 평가 기준**:
- Reasoning (추론 능력)
- Knowledge (지식)
- Conversation (대화 능력)
- Creativity (창의성)
- Personality (개성)
- Storytelling (스토리텔링)
- Empathy (공감 능력)

#### LLM-EVAL
- **LLM이 LLM을 평가함**
- AI가 AI의 성능을 평가하는 새로운 패러다임

---

### 2.7 Prompt Engineering (프롬프트 엔지니어링)

#### 기본 정의

**Prompt**:
- LLM으로부터 사용자가 원하는 결과를 도출하기 위한 Input 혹은 Instruction

**Prompt Engineering**:
- 대화형 AI가 생성하는 결과물의 품질을 높일 수 있는 prompt 입력 값들의 조합을 찾는 작업

#### Prompt의 구성 요소

1. **Instruction**: 모델이 수행하기를 원하는 특정 태스크 또는 지시 사항
2. **Context**: 모델이 보다 더 나은 답변을 하도록 유도하는 외부 정보 또는 추가 내용
3. **Input Data**: 답을 구하고자 하는 것에 대한 인풋 또는 질문
4. **Output Indicator**: 결과물의 유형 또는 형식을 나타내는 요소

#### Prompt Engineering에 대한 재정의
```
기존 관점: Prompt Engineering
새로운 관점: Prompt Discovering

→ 단순히 LLM이 보유하고 있는 내재된 능력치를 발굴하는 것은
  Prompt Engineering이 아닌 Prompt Discovering!
```

---

#### Chain-of-Thought Prompting (COT)

**개념**:
- **단지 답변을 내놓기 위한 것이 아닌 답변에 도달하는 과정을 학습시키는 것**
- **사람의 생각의 흐름을 함께 학습시킴**

**효과**:
```
PaLM을 학습할 때:
추리(Reasoning) 관련 기존 데이터셋을 확장시켜
중간 논리를 설명한 부분을 넣었더니
→ 성능이 확연히 향상됨
```

---

#### Optimization & Tuning

**핵심 질문**:
- 어떻게 하면 더 고품질의 결과물을 도출할 수 있을까?
- 어떻게 하면 안 되던 것도 되게 만들어낼 수 있을까?

**Simple but Impactful 예시**:
- 감정 호소를 추가
- "step by step"을 추가했더니 더 잘 나오더라

---

#### Prompt Manager (Cross Function Modality)

**중요성**:
- Prompt를 발굴하는 것도 중요하나
- **개별적인 모달리티를 연결하기 위한 Prompt Manager 기술이 중요해질 것**
- **이것이 결국 서드 파티를 만드는 핵심**

---

#### Function Call

**정의**:
- 모델이 API 호출 입력으로부터 함수 호출 시점을 파악
- 함수 호출에 필요한 파라미터 등의 정보를 JSON 형태로 내보낼 수 있게 하는 것

**활용**:
- ChatGPT API 호출을 통해 원하는 함수를 적절한 인자와 함께 호출 가능

---

#### Prompt Engineering (Learning)

**Parameter Efficient Fine-Tuning (PEFT)**:
- **P-Tuning (Prompt Learning)**
- **LoRA (Adapter)**

**목적**:
- 모델의 일부 파라미터만을 튜닝함으로써
- 모델의 성능을 적은 자원으로도 높게 유지하는 방법론

---

#### Prompt Parameter Tuning (PPT)

**주요 파라미터**:

**1. Temperature**
```
낮은 값: 사실에 근거한 정확한 답변 제공
높은 값: 보다 창의적인 결과물 생성

답변의 창의성과 무작위성을 조정하는 값
```

**2. Top_p**
```
낮은 값: 답변이 보다 정확함
높은 값: 창의적이고 광범위해짐

답변의 무작위성을 제어하는 조정 값
```

**3. frequency_penalty**
```
높은 값: AI가 흔하지 않은 단어를 답변에 포함할 가능성 감소
0에 가까울수록: 흔히 사용되지 않는 단어를 포함할 가능성 증가
```

**4. presence_penalty**
```
높은 값: AI가 유사하거나 동일한 단어 및 문구를 반복할 가능성 감소
0에 가까울수록: 단어나 문구를 반복할 가능성 증가
```

---

#### Automatic Curriculum

**개념**:
- **"Goals"만 설정하면 달성을 위해 필요한 것을 자동으로 실행**
- 실수를 스스로 수정하는 **'자율반복(autonomous iterations)' 기능** 사용
- 결과물을 자동으로 생성

---

#### PromptOps

**핵심**:
- **Cost를 관리하기 위한 것이 핵심!**
- 프롬프트 최적화를 통한 비용 절감
- 효율적인 LLM 운영

---

### 2.8 3rd Party Platform

#### 발전 과정
```
Prompt Engineering 
  ↓
3rd Party Platform (LLM Applications)
  ↓
Private AI
```

#### 3rd Party Platform 구성
- **생성 AI 어플리케이션**
- **Foundation Model**
- **Cloud**
- **Hardware (반도체)**

#### 운영 체계의 진화
```
DevOps → MLOps → LLMOps (FMOps - Foundation Model Ops)
```

---

### 2.9 Open Source

#### Open Source의 현황
- **GPT-3 파라미터 크기인 175B까지 모델과 코드 오픈됨**
- 그러나 어차피 공개를 해도 돌릴 수 있는 곳이 많지 않음

#### 주요 Open Source 진영
- **Eleuther AI**: Big Model 민주화를 꿈꾸는 곳
- **Huggingface**: BigScience 그룹의 움직임

#### 중요한 점
- **잘 활용할 줄 알아야 하며, 미리 준비해야 함**
- **내 컴퓨터에서 LLM을 돌릴 수 있는 시대**

#### 주의사항
```
⚠️ Research use인지 Commercial use인지 잘 확인!

라이선스 종류:
- Research use: 연구 목적으로만 사용 가능
- Commercial use: 상업적 사용 가능
```

---

### 2.10 To be (미래 전망)

#### 1. Preoccupy (선점)
- **선점해야 함 (First Mover)**
- 빠르게 움직이는 것이 중요

#### 2. Rapid Adaptation (빠른 적응)

**검색의 패러다임 변화**:
```
기존: 키워드 방식 검색
현재: Instruct 방식 검색

주도권의 이동:
AI → 사용자
```

#### 3. Collaboration (협력)

**주요 협력 영역**:
- **Infra 영역**: NAVER X Samsung
- **Platform 영역**: MS X OpenAI
- **B2B2C**
- **Academia (학계)**
- **Evaluation (평가)**
- **Scaling Law (확장 법칙)**

---

#### At a Glance (한눈에 보기)

**핵심 메시지**:

**1. 잘 활용하자**
- LLM을 효과적으로 사용하는 방법 학습

**2. 빠르게 선점해야 함**
- 그러면서도 독자적인 것이 필요

**3. 미래의 LLM Research를 잘 대비하자**

**4. SOTA의 의미 없음**
- State-of-the-Art는 더 이상 절대적 기준이 아님

**5. Task의 수렴 현상 파악**
- LLM으로 인하여 Converge되는 Task를 잘 분간해야 함

**6. 실용성 중심의 연구**
```
Real-World에서 사용할 수 있고, 
도움이 되는 기술인지 아닌지로 
논문 및 연구는 나뉠 것
```

**7. LLM의 명확한 약점을 공략해라**
- Reasoning (추론)
- Commonsense (상식)
- Hallucination (환각)
- Expert Knowledge (전문 지식)
- Ethics (윤리)

**8. 최신 트렌드에 민감해야 함**
- **정신 똑바로 차리고, 잘 따라가야 함**
- **최신 트렌드에 굉장히 예민하고 민감해야 함**

---

## 전체 요약

### LLM의 핵심 특징

| 특징 | 설명 |
|------|------|
| **창발성** | 단일 모델로 여러 Task 처리 |
| **Human Alignment** | 인간의 피드백 기반 학습 |
| **Scaling Law** | 크기에 따른 성능 향상 법칙 |
| **In-Context Learning** | 프롬프트 내에서 학습 |
| **Multimodal** | 다양한 데이터 타입 처리 |

---

### LLM 개발의 주요 방향
```
1. Data & Size
   └─ 모델 크기와 데이터 양의 최적 균형

2. Multimodal
   └─ 언어를 넘어선 다양한 데이터 처리

3. Multilingual
   └─ 다국어 지원 강화

4. Synthetic Data
   └─ AI가 생성한 데이터로 학습

5. Domain Specialized
   └─ 특정 분야에 특화된 모델

6. Evaluation
   └─ 다양한 평가 기준 도입

7. Prompt Engineering
   └─ 효과적인 프롬프트 설계

8. 3rd Party Platform
   └─ LLM 기반 애플리케이션 생태계

9. Open Source
   └─ 모델과 코드의 공개

10. Future Direction
    └─ 선점, 협력, 실용성
```

---

### 중요한 패러다임 변화

#### 1. 개발 방식의 변화
```
기존: Task별 개별 모델 개발
LLM: Foundation Model 하나로 다양한 Task
```

#### 2. 검색 방식의 변화
```
기존: 키워드 기반 검색
LLM: 자연어 Instruction 기반 검색
```

#### 3. 평가 방식의 변화
```
기존: 정확도, 정밀도 등 정량적 지표
LLM: 창의성, 공감 능력 등 정성적 지표
```

#### 4. 데이터의 변화
```
기존: 사람이 직접 레이블링
LLM: AI가 생성한 합성 데이터 활용
```

---

### 성공을 위한 핵심 요소

**1. 선점 (First Mover)**
- 빠르게 움직여 시장을 선점

**2. 협력 (Collaboration)**
- Infra, Platform, 학계 등과의 협력

**3. 실용성 (Practicality)**
- Real-World에서 사용 가능한 기술 개발

**4. 지속적 학습 (Continuous Learning)**
- 최신 트렌드에 민감하게 반응

**5. 약점 공략 (Weakness Attack)**
- LLM의 명확한 한계를 개선

---

### LLM 활용 시 주의사항
```
✅ Do's:
- 최신 트렌드 지속적으로 학습
- 실용적인 문제 해결에 집중
- 협력 생태계 구축
- 윤리적 문제 고려

❌ Don'ts:
- SOTA만 쫓지 말 것
- 이론에만 치중하지 말 것
- 라이선스 무시하지 말 것
- 환경 문제 간과하지 말 것
```

---

## 미래 전망

### 단기 (1-2년)
- Prompt Engineering 고도화
- Domain Specialized 모델 증가
- Multimodal 기능 강화

### 중기 (3-5년)
- Private AI 보편화
- LLMOps 생태계 성숙
- Hallucination 문제 대폭 개선

### 장기 (5년+)
- AGI (Artificial General Intelligence)에 근접
- 완전한 인간-AI 협업 체계
- 새로운 AI 패러다임 등장 가능

---

## 핵심 Takeaway
```
💡 LLM은 단순한 기술이 아닌 패러다임의 변화

🚀 빠르게 움직이되, 독자적인 강점 필요

🤝 협력 없이는 성공 어려움

🎯 실용성과 윤리성을 동시에 고려

📈 지속적인 학습과 적응이 필수
```
