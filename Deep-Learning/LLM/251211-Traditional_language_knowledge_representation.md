# 전통적인 언어 지식 표현 체계 정리

---

# 1. 정보이론 (Information Theory)

## 1.1 왜 정보이론인가?
- 딥러닝 학습은 **훈련 데이터를 기반으로 새로운 데이터의 확률분포를 학습**하는 과정.
- 예측 분포 Q와 실제 정답 분포 P 간의 차이를 정량화해야 함.
- 정보이론은 **확률과 정보량, 불확실성**을 측정하는 도구.

---

## 1.2 정보량 (Information Content)
- 사건 A의 정보량:  
  **I(A) = −log P(A)**
- 자주 발생하는 사건 → 정보량 ↓  
- 드물게 발생하는 사건 → 정보량 ↑

### 예시
- 동전 앞면: P=0.5 ⇒ −log₂(0.5) = 1
- 주사위 1: P=1/6 ⇒ −log₂(1/6) ≈ 2.585

---

## 1.3 엔트로피 (Entropy)
- 확률분포의 불확실성을 수치화한 값.
- **H(X) = − Σ P(x) log P(x)**
- 분포가 균등할수록 불확실성이 커져 엔트로피 ↑  
- 결정적일수록 엔트로피 ↓

### 특징
- 항상 양수
- log 밑은 보통 자연로그(e)
- 모델의 불확실성 측정에 사용

---

## 1.4 교차 엔트로피 (Cross Entropy)
- 실제 분포 P와 모델 분포 Q의 차이 측정  
  **H(P, Q) = − Σ P(x) log Q(x)**
- 분류 모델 학습의 핵심 기반(loss function)

---

## 1.5 KL Divergence
- 두 분포 P, Q의 차이를 나타내는 지표  
  **KL(P || Q) = Σ P(x) log (P(x) / Q(x))**
- Cross Entropy = Entropy + KL Divergence  
  ⇒ **Cross Entropy 최소화 = KL 최소화**

---

# 2. One-hot Encoding

## 2.1 개념
- 단어를 고차원 벡터로 표현. 단 하나의 위치만 1, 나머지 0.
- 단어 간 유사도, 의미 정보 없음.

## 2.2 문제점
- 단어수가 커질수록 차원이 커짐 (Sparse, Memory expensive)
- 단어 관계/문맥 정보 없음

---

# 3. 통계적 언어 모델 (Statistical LM)

## 3.1 개념
- 단어 시퀀스에 확률을 부여하는 모델
- 목표: 실제 언어의 확률분포를 잘 근사하는 것

---

## 3.2 조건부 확률 & 연쇄 법칙
- 문장 확률:  
  **P(w₁, w₂, …, wₙ) = Π P(wᵢ | w₁,…, wᵢ₋₁)**

---

## 3.3 N-gram LM
- Markov 가정: 현재 단어는 바로 직전 단어들(n−1)에만 의존.
- **P(wᵢ | wᵢ₋₁,…,wᵢ₋ₙ₊₁)**

### Trade-off
- n ↑ → 문맥 정보 ↑ but sparsity 문제 발생  
- n ↓ → sparsity 완화 but 성능 ↓

---

# 4. 카운트 기반 언어모델

## 4.1 국소 표현 vs 분산 표현
| 구분 | 국소 표현 (One-hot, BoW) | 분산 표현 (Word Embedding) |
|------|---------------------------|-----------------------------|
| 차원 | 매우 높음 | 낮고 dense |
| 의미 | 없음 | 의미·문맥 반영 |
| 장점 | 단순 | 유사도 계산 가능 |
| 단점 | sparse, 의미 관계 없음 | 학습 필요 |

---

## 4.2 Bag of Words (BoW)
- 단어 순서 무시하고 **단어 등장 빈도만 고려**
- 벡터 차원 = vocabulary 크기
- 문맥·단어 의미 고려 불가

---

# 5. TF-IDF

## 5.1 개념
### TF (Term Frequency)
- 문서 내 단어 등장 비율  
  TF(t,d) = count(t) / total_terms(d)

### IDF (Inverse Document Frequency)
- 단어가 제공하는 정보량  
  **IDF(t) = log(N / DF(t))**

### TF-IDF
- 문서 내 중요 단어 식별  
  높은 TF & 낮은 DF → 높은 TF-IDF

---

## 5.2 활용
- 검색 엔진 랭킹
- 키워드 추출
- 문서 요약
- 문서 군집화

---

## 5.3 Inverted Index
- key: 단어  
- value: 단어가 등장하는 문서 리스트
- 검색 엔진 기본 구조

---

# 6. BM25

## 6.1 개념
- TF-IDF 개선 버전
- 단어 빈도, 문서 길이까지 고려한 검색 점수 산출

## 6.2 장점
- TF saturation(무한정 증가 방지)
- IDF 영향 강화 → 불용어 영향 감소
- 문서 길이 정규화

## 6.3 한계
- 단어 순서, 문맥 정보 없음

---

# 7. 생성형 언어모델 평가 지표

## 7.1 Perplexity (PPL)
- 모델이 다음 단어를 얼마나 헷갈렸는지 나타냄  
  **낮을수록 좋음**
- PPL = exp(average negative log likelihood)

---

## 7.2 BLEU (MT에서 주로 사용)
- n-gram precision 기반  
- 동일 단어가 등장하면 정답으로 간주  
- Brevity Penalty 포함  
- 문맥·의미 정보 반영 못함

---

## 7.3 ROUGE (요약 평가)
- Recall 기반  
- Reference의 단어가 예측 문장에 있으면 OK

### 종류
- **ROUGE-N**: n-gram overlap
- **ROUGE-L**: LCS 기반
- **ROUGE-S**: Skip-bigram

---

## 7.4 METEOR
- Precision + Recall 조화 평균
- stem, synonym, paraphrase 매칭 지원  
  ⇒ BLEU의 단순 매칭 한계를 보완

---

## 7.5 chrF / chrF++
- Character-level F-score  
- 언어적 변형에 강함  
- chrF++는 word-level도 병합하여 더 강력

---

## 7.6 BLEURT
- BERT 임베딩 기반 의미적 비교  
- 의미·구문 변형까지 평가 가능  
- 최근 요약/번역 평가에서 많이 사용

---

## 7.7 기타 지표
- COMET  
- BERTScore  
- MAUVE 등
