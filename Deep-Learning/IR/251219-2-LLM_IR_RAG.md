# LLM 어플리케이션 구현 및 RAG

## 1. LLM 어플리케이션 구현

### 1.1 JSON Mode 활용

#### LLM의 활용

**가능한 것**:
- LLM의 **언어 이해 능력** 및 **추론 능력**을 활용하여 여러 형태의 어플리케이션을 구현

**역할**:
- 주어지는 작업을 위해 어떤 툴을 사용할지 판단
- 필요한 작업을 계획하는 역할

**필요성**:
```
이런 식으로 활용하기 위해서는:
- LLM은 자연어 형태의 출력이 아닌
- 구조화된 출력(JSON)을 반환하는 것이 필요함
```

---

#### Prompting을 통한 JSON 출력

**방법**:
- 프롬프팅을 통해 LLM에 **JSON 형태로 출력**하라고 명시

**한계**:
```
⚠️ 100%를 보장하지는 않음
```

**예시**:
```
"다음 정보를 JSON 형태로 출력해주세요:
{
  "name": "홍길동",
  "age": 30,
  "city": "서울"
}"
```

---

#### OpenAI API JSON Mode

**특징**:
- 구조화된 출력을 얻을 수 있도록 **OpenAI API 자체에서 JSON mode를 지원**
- 오류를 없애고 성능을 높임

**사용 방법**:

**1. 지시문에 명시**:
```
✅ 지시문에 JSON으로 출력하라고 명시적으로 알려줘야 함
```

**2. API 호출 시 설정**:
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Return your response in JSON format."},
        {"role": "user", "content": "Tell me about Paris"}
    ],
    response_format={"type": "json_object"}  # JSON mode 활성화
)
```

---

### 1.2 Function Calling 활용

#### 개념

**목적**:
- LLM의 추론 능력을 외부 툴 또는 API를 호출하기 적합한 형태로 최적화

**기능**:
1. 요청에 대한 **의도 분류**
2. 해당 요청을 처리하기 위해 필요한 **속성 정보들을 추출**

**특징**:
- **Instruction을 명시적으로 주지 않고 처리할 수 있는 요청**에 대한 **명세를 함수 형태로 정의하는 방식**
- **메시지의 내용이 특정 함수를 호출하기에 적합한 경우**만 **function calling이 유도**됨

---

#### OpenAI API Function Calling

**지원 모델**:
```
2023년 11월 6일 OpenAI DevDay에 공개한 모델들:
- gpt-3.5-turbo-1106
- gpt-4-1106-preview

특징: 함수 호출이 필요한 경우를 감지하도록 학습되어 있음
```

---

#### 사용 방법

**1. Tools 정의**:
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]
```

**2. API 호출**:
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "What's the weather like in Boston?"}
    ],
    tools=tools,
    tool_choice="auto"  # 또는 특정 tool을 강제로 선택
)
```

---

#### Tools 설정

**역할**:
- API 호출 시 tools에 사용할 **함수들의 명세를 작성 후 입력**

**모델의 판단**:
- 모델이 작업 수행을 위해 주어지는 tools 중:
  - 어떤 tool을 선택할지
  - 또는 메시지를 출력할지 판단해서 결과 반환

**tool_choice 옵션**:
```
- "auto": 모델이 자동으로 선택
- "none": tool 사용 안 함
- {"type": "function", "function": {"name": "함수명"}}: 특정 tool을 강제로 사용
```

---

#### 결과 확인

**finish_reason**:
```python
# 반환하는 정보에서 finish_reason을 통해 모델이 tool을 사용했는지 파악
if response.choices[0].finish_reason == "tool_calls":
    # Tool이 호출됨
    pass
```

**content 확인**:
```python
# content를 통해:
# 1. 어떤 tool을 사용했는지
# 2. tool의 입력값을 얻을 수 있음

tool_calls = response.choices[0].message.tool_calls
for tool_call in tool_calls:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
```

---

## 2. 대화형 IR - RAG

### 2.1 LLM의 등장

#### 변화

**가능해진 것**:
- **LLM을 통해 질문-답변 형태로 원하는 지식을 얻을 수 있게 되었음**

---

### 2.2 LLM의 한계

#### 주요 한계점

**1. Knowledge Cutoff (지식 단절)**
```
문제:
❌ 특정 날짜까지의 정보만 대응
❌ 학습 완료 시점 이후의 정보에 대해서는 제대로 대답하지 못함

예시:
- GPT-4의 지식 cutoff: 2023년 4월
- 그 이후 정보는 모름
```

**2. Hallucination (환각)**
```
문제:
❌ 실재하지 않는 정보를 그럴듯하게 만들어냄
❌ 사실 여부에 대한 판단이 어려움

특히 문제되는 경우:
- 맛집 추천 (존재하지 않는 식당)
- 인명 검색 (잘못된 정보)
- 구체적인 수치나 날짜
```

---

### 2.3 LLM과 IR의 결합

#### 필요성

**핵심**:
```
사실 기반의 정확한 대답을 위해서는
외부 정보를 활용할 수밖에 없음
```

---

#### 외부 정보가 필요한 이유

**1. 정보의 시의성 (Timeliness)**
```
문제:
- 정보의 의미나 가치는 시간에 따라 계속 변함
- 모델이 이를 실시간으로 학습하기 힘듦

예시:
- 주식 가격
- 날씨
- 최신 뉴스
```

**2. 모델의 내재적 특성 (Intrinsic Characteristics)**
```
문제:
- 모델은 정보를 압축해서 저장
- 학습 과정에서 정보의 손실이 발생할 수밖에 없음

특히 위험한 경우:
- 패턴화된 형태지만 세부 정보는 다를 수 있는 경우
- 거짓 정보 생성 확률 높음

예시:
- 사람 이름과 직책 (비슷한 패턴이지만 다른 정보)
- 주소와 전화번호
```

---

#### RAG의 등장

**개념**:
```
두 가지 이유로 LLM과 IR을 같이 활용하여
대답을 생성하는 기술이 대두됨
```

**역할 분담**:

**LLM**:
```
- 자체 지식을 사용하지 않음
- 추론 능력만 사용
- Reference를 주면 이를 토대로 질문에 답하는 능력 활용
```

**IR**:
```
- 지식은 LLM 모델의 학습 대상이 아님
- IR의 처리의 대상으로 간주
```

**용어**:
```
이런 기술 방식을 통칭하여
Retrieval Augmented Generation (RAG)라는 용어를 사용
```

---

### 2.4 RAG (Retrieval Augmented Generation)

#### 정의

**개념**:
- **외부 지식을 LLM에 활용하여 더 정확한 생성 결과를 얻는 방법**

---

#### RAG 프로세스

**3단계**:

**1. Retrieval (검색)**
```
- 질의와 연관된 문서를 데이터베이스 또는 검색엔진에서 가져옴
```

**2. Augmented (증강)**
```
- 질의와 검색된 문서를 함께 프롬프트를 구성해 LLM에 넣어줌
```

**3. Generation (생성)**
```
- LLM이 이를 토대로 적절한 답변을 생성
```

---

#### RAG 작동 방식 다이어그램
```
사용자 질의
  ↓
Retrieval (검색 엔진/Vector DB)
  ↓
관련 문서 추출
  ↓
Augmented (질의 + 문서)
  ↓
LLM Prompt
  ↓
Generation (답변 생성)
  ↓
사용자에게 답변 제공
```

---

## 3. 대화형 IR 구현

### 3.1 대화형 IR 구현

#### LLM과 IR의 역할 구분

**LLM의 역할**:
```
추론 능력을 통해:
1. 질의 의도 파악
2. 답변 생성 기능 구현

대화형 기능:
- LLM이 질의 의도를 파악할 때 기존 대화 히스토리까지 활용
- RAG가 그대로 대화형 IR이 됨
- 자연스러운 멀티턴 인터페이스를 제공할 수 있음
```

**IR의 역할**:
```
1. 데이터 전처리
2. 문서 색인
3. 문서 검색
→ 질문에 적합한 지식 정보를 추출하여 제공
```

---

#### 역할 분담 다이어그램
```
LLM:
- 질의 의도 파악
- 답변 생성
- 대화 히스토리 관리

IR:
- 데이터 전처리
- 문서 색인
- 문서 검색
```

---

### 3.2 LLM 프롬프트 엔지니어링

#### Reference 기반 답변 생성

**목적**:
- Reference를 분석하고 활용해서 **질문에 대한 답을 생성**

**프롬프트 구성**:

**1. 검색 결과 활용 지시**:
```
"검색엔진을 통해 얻은 지식 정보(레퍼런스)를 기반으로 답하세요."
```

**2. 모를 때 대응**:
```
"레퍼런스에 질문과 연관된 충분한 정보가 없으면 모른다고 답하세요."

중요: Hallucination 방지
```

**3. 필터링**:
```
"검색엔진 결과 중 질문과 연관도가 낮은 것을 미리 필터링하기 위해
LLM을 추가로 활용할 수 있음"
```

---

#### Standalone Query 생성

**목적**:
- 대화 히스토리를 보고 검색엔진에 입력으로 사용할 **최종 질의 생성**

**방법**:
```
기존 대화 히스토리로부터 standalone query를 생성하도록 지시
```

**예시**:
```
대화 히스토리:
사용자: "파리에 대해 알려줘"
AI: "파리는 프랑스의 수도입니다..."
사용자: "거기 날씨는 어때?"

Standalone Query: "파리의 날씨"
```

---

#### 시스템 고도화

**필요사항**:
```
시스템 고도화를 위해서는:
- 사용자와 시스템 간의 대화 히스토리를 효과적으로 저장 및 관리해야 함

고려사항:
- 비용
- 성능
```

---

## 전체 요약

### JSON Mode vs Function Calling

| 구분 | JSON Mode | Function Calling |
|------|-----------|------------------|
| **목적** | 구조화된 출력 | 외부 API 호출 |
| **사용 시점** | 데이터 추출, 구조화 | 특정 기능 실행 |
| **보장** | 100% JSON 형식 | 함수 호출 감지 |
| **설정** | response_format | tools 정의 |

---

### LLM의 한계와 해결책

| 한계 | 설명 | 해결책 |
|------|------|--------|
| **Knowledge Cutoff** | 특정 시점까지만 학습 | RAG (외부 지식 활용) |
| **Hallucination** | 거짓 정보 생성 | RAG (사실 기반 답변) |
| **정보 압축** | 세부 정보 손실 | RAG (원본 문서 참조) |

---

### RAG 프로세스
```
1. Retrieval (검색)
   - 질의 관련 문서 추출
   - Vector DB, 검색 엔진 활용
   ↓
2. Augmented (증강)
   - 질의 + 검색 문서
   - 프롬프트 구성
   ↓
3. Generation (생성)
   - LLM이 답변 생성
   - Reference 기반 답변
```

---

### 대화형 IR의 구성 요소
```
사용자 질의
  ↓
대화 히스토리 분석 (LLM)
  ↓
Standalone Query 생성 (LLM)
  ↓
문서 검색 (IR)
  ↓
관련도 필터링 (LLM)
  ↓
답변 생성 (LLM)
  ↓
사용자에게 제공
```

---

## 실전 활용 가이드

### JSON Mode 활용 시나리오

**1. 데이터 추출**:
```python
# 텍스트에서 구조화된 데이터 추출
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Extract person information in JSON format"},
        {"role": "user", "content": "John Doe is 30 years old and lives in New York"}
    ],
    response_format={"type": "json_object"}
)
```

**2. 분류 작업**:
```python
# 의도 분류를 JSON으로 반환
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Classify intent and return as JSON"},
        {"role": "user", "content": "I want to book a flight to Paris"}
    ],
    response_format={"type": "json_object"}
)
```

---

### Function Calling 활용 시나리오

**1. 날씨 조회**:
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]
```

**2. 데이터베이스 조회**:
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Search user database",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "limit": {"type": "integer"}
                }
            }
        }
    }
]
```

---

### RAG 구현 예시

**기본 RAG**:
```python
# 1. 문서 검색
relevant_docs = vector_db.search(query)

# 2. 프롬프트 구성
prompt = f"""
다음 정보를 참고하여 질문에 답하세요:

{relevant_docs}

질문: {query}
"""

# 3. 답변 생성
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
```

**대화형 RAG**:
```python
# 1. Standalone query 생성
standalone_query = generate_standalone_query(query, chat_history)

# 2. 문서 검색
relevant_docs = vector_db.search(standalone_query)

# 3. 프롬프트 구성 (히스토리 포함)
prompt = f"""
대화 히스토리:
{chat_history}

참고 문서:
{relevant_docs}

질문: {query}
"""

# 4. 답변 생성
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
```

---

## 주요 개념 정리

### JSON Mode
```
정의: LLM이 구조화된 JSON 형식으로 출력
목적: 데이터 추출, 의도 분류 등
설정: response_format={"type": "json_object"}
```

### Function Calling
```
정의: LLM이 외부 함수/API 호출 결정
목적: 외부 시스템 연동
설정: tools 파라미터로 함수 명세 제공
```

### RAG
```
정의: Retrieval Augmented Generation
구성: Retrieval + Augmented + Generation
목적: 외부 지식으로 정확한 답변 생성
```

### Standalone Query
```
정의: 대화 히스토리를 고려한 독립적인 질의
목적: 검색 엔진 입력용
예시: "거기 날씨는?" → "파리의 날씨"
```

### Hallucination
```
정의: LLM이 거짓 정보를 생성하는 현상
원인: 패턴 학습의 한계, 정보 압축
해결: RAG로 사실 기반 답변 생성
```

---

## Best Practices

### JSON Mode
```
✅ 지시문에 JSON 출력 명시
✅ 명확한 스키마 정의
✅ 에러 처리 구현
❌ 복잡한 중첩 구조는 피하기
```

### Function Calling
```
✅ 함수 설명 명확히 작성
✅ 파라미터 타입 정확히 정의
✅ required 필드 명시
❌ 너무 많은 함수 정의 피하기
```

### RAG
```
✅ 관련 문서만 선택 (Top-k)
✅ "모르면 모른다고 답하기" 지시
✅ 출처 표시
❌ 너무 많은 문서 포함 피하기
```

---

## 트렌드 및 미래 방향

### 현재 트렌드
```
1. RAG가 표준
2. Function Calling 고도화
3. Multi-turn 대화 강화
4. Hybrid Search (Sparse + Dense)
```

### 미래 방향
```
1. 완전 자동화된 에이전트
2. 멀티모달 RAG
3. 실시간 지식 업데이트
4. 개인화된 RAG
```

---

## 핵심 Takeaway
```
📝 JSON Mode: 구조화된 출력 보장

🔧 Function Calling: 외부 시스템 연동

🔍 RAG: LLM + IR = 정확한 답변

💬 대화형 IR: RAG + 히스토리 관리

🎯 Standalone Query: 대화 맥락 고려

⚠️ Hallucination: RAG로 해결

📚 역할 분담: LLM (추론) + IR (지식)

🚀 미래: 완전 자동화된 AI 에이전트
```
