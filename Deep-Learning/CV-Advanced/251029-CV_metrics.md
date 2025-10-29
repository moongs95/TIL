# 🧮 CV Metrics

## 01 CV Metrics

### 1.1 CV Metrics 개요

**Classification**
- 예측값 형식: Class label

**Object Detection**
- 예측값 형식: [bounding box 좌표, confidence score]

**Semantic Segmentation**
- 예측값 형식: Class labels per pixel (mask)

---

## 02 Classification Metrics

Classification task의 성능 평가에 사용되는 주요 지표들

---

### 2.1 Confusion Matrix

**Confusion Matrix**
- 예측값과 실제값을 비교하여 모델 성능을 시각화한 표  
- 구성 요소:
  - **TP (True Positive)**: 실제 Positive를 Positive로 예측 (정답)
  - **FP (False Positive)**: 실제 Negative를 Positive로 예측 (오답)
  - **FN (False Negative)**: 실제 Positive를 Negative로 예측 (오답)
  - **TN (True Negative)**: 실제 Negative를 Negative로 예측 (정답)

---

### 2.2 Accuracy (정확도)

전체 데이터 중 올바르게 예측된 비율

\[
Accuracy = \frac{TP + TN}{TP + FP + FN + TN}
\]

---

### 2.3 Precision (정밀도)

모델이 Positive로 예측한 것 중 실제로 Positive인 비율

\[
Precision = \frac{TP}{TP + FP}
\]

---

### 2.4 Recall (재현율, Sensitivity)

실제 Positive 중에서 모델이 Positive로 예측한 비율

\[
Recall = \frac{TP}{TP + FN}
\]

---

### 2.5 Specificity (특이도)

실제 Negative 중에서 모델이 Negative로 예측한 비율

\[
Specificity = \frac{TN}{TN + FP}
\]

---

### 2.6 F1 Score

Precision과 Recall의 조화평균  
- 데이터가 불균형(imbalance)할 때 유용

\[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
\]

---

### 2.7 AUC-ROC

**ROC Curve**
- 다양한 threshold에서의 TPR과 FPR을 시각화한 그래프  
  - x축: FPR (False Positive Rate)  
  - y축: TPR (True Positive Rate)  

**AUC (Area Under Curve)**
- ROC 곡선 아래 면적  
- 1에 가까울수록 좋은 성능을 의미  

---

## 03 Object Detection Metrics

Object Detection task의 성능 평가 지표

---

### 3.1 IoU (Intersection over Union)

Bounding Box의 겹치는 영역 비율  
\[
IoU = \frac{Area\ of\ Intersection}{Area\ of\ Union}
\]

- **IoU ≥ threshold** → True Positive (TP)  
- **IoU < threshold** → False Positive (FP)

---

### 3.2 Precision & Recall

**Precision (정밀도)**  
\[
Precision = \frac{TP}{TP + FP}
\]

**Recall (재현율)**  
\[
Recall = \frac{TP}{TP + FN}
\]

---

### 3.3 PR Curve

Confidence score threshold 변화에 따른 Precision-Recall 관계  
- Threshold ↑ → bbox 수 ↓ → Recall ↓, Precision ↑  
- Threshold ↓ → bbox 수 ↑ → Recall ↑, Precision ↓  

**PR Curve 생성 과정**
1. 모든 예측 bbox의 TP/FP 판별  
2. Confidence score 기준 내림차순 정렬  
3. Threshold를 변화시키며 Precision과 Recall 계산  
4. 각 점을 연결해 PR 곡선 생성  

---

### 3.4 AP & mAP

**AP (Average Precision)**  
- PR Curve의 면적  
- Precision과 Recall의 균형을 수치화한 지표  

**mAP (Mean Average Precision)**  
- 모든 Class에 대한 AP의 평균  
- Object Detection 모델의 대표적인 평가 지표  

---

## 04 Segmentation Metrics

Segmentation task의 성능 평가에 사용되는 주요 지표

---

### 4.1 PA (Pixel Accuracy)

모든 Pixel 중 올바르게 예측된 Pixel 비율  
\[
PA = \frac{TP + TN}{TP + FP + FN + TN}
\]

---

### 4.2 MPA (Mean Pixel Accuracy)

모든 Class의 Pixel Accuracy 평균  
\[
MPA = \frac{1}{K} \sum_{i=1}^{K} \frac{TP_i}{TP_i + FP_i + FN_i + TN_i}
\]

---

### 4.3 IoU (Intersection over Union)

Segmentation의 IoU는 Object Detection과 동일하나,  
**Pixel 단위의 mask 영역**에서 계산됨

---

### 4.4 Dice Coefficient

두 영역의 교집합과 합집합의 조화평균  
- 데이터 불균형 시 IoU보다 안정적인 지표  

\[
Dice = \frac{2 \times |A \cap B|}{|A| + |B|}
\]

---

✅ **정리**
| Task | Metric | 주요 평가 포인트 |
|------|---------|------------------|
| Classification | Accuracy, F1, AUC | 전체 분류 정확도와 균형 |
| Object Detection | IoU, mAP | 위치 + 클래스 정확도 |
| Segmentation | IoU, Dice, MPA | 픽셀 단위 정확도 |

