# 🌟 자연어처리 경진대회 이해하기 — Task · Pipeline · Metrics 완전 정리

---

# 1. 자연어 처리 Task 이해하기

## 1.1 Huggingface 소개

### Huggingface란?
- 기계학습 기반 애플리케이션을 구축하기 위한 도구를 제공하는 미국 회사  
- 2016년 3명의 프랑스 엔지니어가 설립  
- 2023년 기준 기업 가치 약 40억 달러  
- 대표 라이브러리: transformers, datasets, spaces

### 주요 모듈

#### ✔ 모델/토크나이저 불러오기

```python
from transformers import AutoModel, AutoTokenizer
```

#### ✔ 데이터셋 로드

```python
from datasets import load_dataset
```

#### ✔ pipeline으로 간단히 모델 처리

```python
from transformers import pipeline  
clf = pipeline("image-classification")  
clf2 = pipeline("summarization")
```

---

## 1.2 대표적인 자연어처리 Task

- 기계 번역(Machine Translation)
- 질의응답(Question Answering)
- 정보추출(Information Extraction)
- 감성분류(Sentiment Analysis)
- 요약(Summarization)

---

## 1.3 자연어처리 평가지표 (Evaluation Metrics)

### ✔ Confusion Matrix 용어
- TP: 모델이 맞다고 예측했고 실제로 맞음  
- FP: 모델이 맞다고 예측했지만 실제로 틀림  
- FN: 모델이 틀렸다고 예측했지만 실제로 맞음  
- TN: 모델이 틀렸다고 예측했고 실제로 틀림  

### ✔ 공식
- Accuracy = (TP + TN) / (TP + FP + FN + TN)  
- Precision = TP / (TP + FP)  
- Recall = TP / (TP + FN)  

### ✔ F1-score
Precision과 Recall의 조화평균  
→ 불균형 데이터에서 효과적

---

# BLEU Score

기계번역(NMT) 및 텍스트 생성 평가 지표  
- n-gram 기반 precision 평가  
- n=1~4 사용  
- reference와 얼마나 단어가 겹치는지 평가  

### ✔ Brevity Penalty
예측문장이 너무 짧아서 precision이 부풀려지는 것을 방지하기 위한 패널티

---

# 2. 자연어처리 Pipeline 이해하기

## 2.1 Task — 낚시성 기사 탐지

- Input: 뉴스 제목 + 본문  
- Output: 0(비낚시성) or 1(낚시성)

데이터셋  
- 비낚시성: 9,175  
- 낚시성: 14,390  

---

## 2.2 전체 파이프라인 구성

1. 환경 설정 (라이브러리 설치, 데이터 로드)  
2. 데이터셋 구축 (train/valid split + tokenizing + Dataset class 생성)  
3. 모델 & 토크나이저 로드  
4. TrainingArguments & Trainer로 학습  
5. Inference & Evaluation  

---

## 2.3 Dataset & Tokenizing

### 1) 데이터 불러오기 (개념 설명)
pd.read_csv(filepath, sep=",", header=0, usecols=[...], dtype={...}, encoding="utf-8")

### 주요 옵션 설명
- usecols: 필요한 컬럼만 읽기  
- dtype: 컬럼별 타입  
- encoding: utf-8 혹은 cp949  

---

### 2) Pytorch Dataset Class

Dataset을 사용하는 이유:
- 구조화된 데이터 관리  
- DataLoader와 결합해 batch 학습, shuffle, multiprocessing 등을 손쉽게 구현  
- PyTorch 생태계와 완전 호환  

Dataset 구성요소  
1. __init__: 데이터 초기화  
2. __len__: 길이 반환  
3. __getitem__: index 위치의 item 반환  

---

### 3) Tokenizing

- huggingface 토크나이저 로드  
- 사전학습된 tokenizer와 model은 반드시 같은 checkpoint 사용  
  (다르면 토큰 인덱스 불일치로 오류 발생)

---

# 2.3 Model & Trainer

## 1) Model
AutoModelForSequenceClassification 등 사용  
pretrained checkpoint 필요  
→ tokenizer와 동일 checkpoint 필수

---

## 2) Trainer

Trainer는 전체 학습 파이프라인을 자동화하는 high-level API

### 기능
- batch 학습  
- optimizer/scheduler 설정  
- early stopping 지원  
- compute_metrics로 평가 지표 설정  

---

### TrainingArguments 주요 옵션

- save_total_limit: 저장할 ckpt 개수 제한  
- warmup_steps: learning rate warmup 단계  
- load_best_model_at_end: 가장 성능 좋은 ckpt 불러오기  

---

### Trainer 주요 옵션

- compute_metrics: accuracy, f1 등 custom metric 가능  
- callbacks: early stopping 적용  
  - patience: 개선이 없을 때 기다릴 에폭 수  
  - threshold: 개선 판단 기준  
- optimizers: optimizer & scheduler 지정  

---

# 2.4 Inference & Evaluation

## Inference

- model.eval(): 평가 모드 전환  
- torch.no_grad(): gradient 비활성화 → 속도 증가 & 메모리 절약  

---

## Evaluation

모델 예측값 vs 라벨 비교  
accuracy, precision, recall, f1 등 사용  
sklearn.metrics 활용
