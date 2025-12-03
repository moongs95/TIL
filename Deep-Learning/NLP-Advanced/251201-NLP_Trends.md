# 📌 NLP 최신 트렌드 정리

## 01. Scaling Laws

### 1.1 모델 성능에 영향을 주는 요인

- 최근 등장하고 있는 NLP 모델의 크기는 지속적으로 커지고 있음 (Scaling Up)
- GPT-3 모델: **175 Billion parameters**
- 모델 파라미터 증가 ➜ 성능 향상 + 수행 가능한 task 증가
- 데이터, 모델 크기, 컴퓨팅을 함께 늘리면 성능을 예측 가능하게 향상

모델 성능에 영향을 주는 주요 요인 3가지:
1. **모델 파라미터 수 N** (Parameters) - 임베딩 제외 모델 파라미터 수
2. **데이터 크기 D** (Dataset Size)
3. **컴퓨팅 양 C** (Compute)

> 모델 구조(너비/깊이)는 상대적으로 덜 중요한 요인  
> (넓고 얕은 Layer vs 좁고 깊은 Layer 구조 차이)

---

### 1.2 Scaling Laws 핵심 특징

#### 특징 1 — 3요인은 함께 Scaling Up 되어야 함
- N, D, C 중 **하나라도 고정 → 패널티 발생 → 성능 저하 가능**

#### 특징 2 — N과 D를 동시에 scaling하면 **성능 예측 가능하게 증가**
- 반대로 하나만 증가시키면 **증가폭 제한**
- 예) 같은 데이터에 큰 모델 → 오히려 성능이 낮을 수 있음

#### 특징 3 — 큰 모델일수록 **더 적은 학습 단계 / 데이터로 동일 성능**
- Sample Efficient(데이터 효율적)

---

## 02. RLHF (Reinforcement Learning from Human Feedback)

> 사람의 피드백을 활용한 강화학습으로  
> LLM을 **사용자 의도와 더 Align**시키는 기법

---

### 2.1 큰 언어모델의 약점

- Scaling Laws와는 다르게 **모델을 키운다고 무조건 의도를 잘 따르지 않음**
- 자동 수집된 웹 크롤링 데이터 → **거짓/유해/부적절 응답 학습 위험**

예시  
| 사용자 요청 | 모델이 해야할 응답 | 실제 대형 LM의 문제 응답 |
|--|--|--|
| "저작권 침해 방법 알려줘" | "불법이라 답변 불가합니다" | 불법 다운로드 소개 |

---

### 2.2 RLHF 정의

| 구성 요소 | 설명 |
|---|---|
| Human Feedback | 사람이 응답 비교, 선호도 선택 |
| Reinforcement Learning | 사람 선호에 따라 모델을 보상/패널티로 학습 |

---

### 2.3 InstructGPT 학습 단계

#### Step 1. SFT (Supervised Fine-Tuning)
- **Labeler가 Prompt + 올바른 응답(Demonstration)**을 생성
- 예:  
  - Prompt: "6살 아이에게 달 착륙 설명해줘"
  - Demonstration: "사람들은 우주선을 타고…"

#### Step 2. RM (Reward Model)
- 하나의 Prompt에 대해 **모델 응답 여러개 생성**
- Labeler가 **순위 매김 → 보상모델 학습**
- 예: 4 > 3 > 2 = 1

#### Step 3. RL (Reinforcement Learning)
- Reward Model 점수 기반으로 **보상·벌칙 적용하며 학습**
- 사용자 선호에 최적화

---

### 📊 평가 결과

#### 정성적
| Prompt | GPT-3 | InstructGPT |
|--|--|--|
| 6살 아이에게 달 착륙 설명해줘 | 지시 반복/엉뚱한 답 | 어린이 맞춤 설명 |

#### 정량적
| 지표 | 의미 | 결과 |
|--|--|--|
| RealToxicity | 안전성 | 개선 |
| TruthfulQA | 진실성 | 개선 |
| Hallucination | 허위 생성↓ | 개선 |
| Customer Assist | 사용자 선호도↑ | 개선 |

> **결론: 더 안전하고, 진실되고, 의도를 잘 따르는 LLM 구축 성공**

---

## 📌 요약

| 항목 | Scaling Laws | RLHF |
|--|--|--|
| 목표 | 성능 최대화 | 사용자 의도 정렬 |
| 핵심요인 | N, D, C 동시 확장 | Human feedback 기반 강화학습 |
| 해결하는 문제 | 모델 용량에 따른 성능 한계 | 유해성, 오답, 무의미 응답 |

---

## 📎 추가 학습 Tip
- Scaling Laws → Compute Budget 계획에 필수
- RLHF → ChatGPT와 같은 **윤리적/상업적 LLM**의 핵심 기술
