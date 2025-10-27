# 🧠 Object Detection 요약 정리

## 01 Object Detection

### 1.1 Object Detection 이란?

**객체 검출(Object Detection)**  
- 이미지 속의 **각 물체의 Bounding Box 위치**와 **Category(Class)**를 예측하는 Task  
- Bounding Box: `{x0, y0, x1, y1}` 형태로 객체의 경계 좌표값 예측  
- Category: 사물의 class label 예측  
- Architecture = **Backbone (CNN)** + **Decoder (Detection Head)**  
  → Detection Head가 Bounding Box와 Class를 결정하며, 어떤 Head를 쓰느냐에 따라 모델 구조가 달라짐  

**Image Classification vs Object Detection**
- **Image Classification**: 이미지 전체에 어떤 물체가 있는지 분류  
- **Object Detection**: 이미지 내 각 Bounding Box의 객체 Class와 위치를 예측 (Classification + Localization)

**Localization (Bbox Regression)**  
- Bounding Box의 좌표 `{x0, y0, x1, y1}`을 회귀 형태로 예측  
- Regression 수행으로 Feature Map에서 추출된 RoI의 경계를 조정해 더 정확한 박스 생성  

---

### 1.2 2-stage Detector vs 1-stage Detector

**2-stage Detector**
- Region Proposals와 Feature Extractor 단계를 거침  
- Region Proposals: Bounding Box 후보 영역 제안  
- Feature Extractor: 후보 영역에 대한 특징 추출  

**1-stage Detector**
- Region Proposals 없이 Feature Extractor만으로 객체 검출 수행  
- 입력 이미지를 특징으로 변환 후 바로 Classification + Bbox 예측  

---

### 1.3 Object Detection Dataset

| Dataset | 클래스 수 | 이미지 크기 | 이미지 수 | 특징 |
|----------|------------|-------------|------------|------|
| **COCO** | 91 | 640×480 RGB | 330K | 1.5M개 객체 Annotation |
| **Pascal VOC** | 20 | 500×375 RGB | 11K | 27K개 객체 Annotation |
| **KITTI** | 8 | 1248×384 RGB | 15K | 80K개 객체 Annotation (3D용) |

---

### 1.4 성능 평가 방법

**Intersection of Union (IoU)**  
- `IoU = Area of Intersection / Area of Union`  
- IoU > 0.5 → 일치, IoU > 0.7 → 우수, IoU > 0.9 → 거의 완벽  

**Average Precision (AP)**  
- IoU 임계값으로 TP/FP 계산 → Precision & Recall 산출  
- Precision-Recall Curve의 넓이 = AP  
- Precision과 Recall이 모두 높을수록 AP가 높음  

---

## 🧩 2-stage Detector

### 01 R-CNN

**R-CNN이란**
- Region Proposals(ROI) 단계 수행  
- Fast/Faster R-CNN의 기반 모델 (CVPR 2014)

**과정**
1. **Selective Search**로 약 2000개 RoI 추출 (CPU 기반)
2. 각 RoI를 동일 크기로 Resize → CNN Backbone에 입력
3. **SVM**으로 Class 분류, **Bbox Regression**으로 위치 보정

**한계**
- CPU 기반 Selective Search로 매우 느림  
- 2000개의 RoI 각각 CNN 통과 → 연산량 큼  

---

### 02 Fast R-CNN

**Fast R-CNN이란**
- ICCV 2015, R-CNN보다 빠르고 효율적  

**특징**
- 입력 이미지를 한 번만 CNN에 통과시켜 Feature Map 생성  
- Selective Search로 RoI 추출 후, Feature Map 상에 **RoI Pooling** 수행  
- RoI Pooling으로 고정 크기 Feature Vector 생성  

**출력**
- Softmax Classifier → 객체 분류  
- Bbox Regressor → 위치 보정  

**한계**
- Selective Search 여전히 느림 (CPU)  
- RoI Pooling 정확도 제한  

---

### 03 Faster R-CNN

**Faster R-CNN이란**
- NIPS 2015, Fast R-CNN + **RPN(Region Proposal Network)**  
- Selective Search를 **GPU 기반 RPN**으로 대체  

**RPN 특징**
- Feature Map 기반으로 물체 위치 예측  
- **Anchor Box**(k개)를 이용하여 다양한 스케일 대응  
- Sliding Window 방식으로 Feature Map 전 영역 탐색  

**Training Process**
1. 이미지 전처리 (resize, normalization 등)
2. Faster R-CNN 초기화 및 가중치 설정  
3. **Positive Anchor (IoU ≥ 0.7)** → Classification + Regression Loss  
   **Negative Anchor (IoU ≤ 0.3)** → Classification Loss  
4. Regression은 MSE 기반  

**Test Process**
- Non-Maximum Suppression (NMS):  
  신뢰도 높은 박스 중심으로 중복 제거  
- 최종 출력: 각 객체의 위치 + Class Label  

**성과**
- Selective Search 대비 약 **10배 속도 향상**  
- 2-stage 중 가장 높은 정확도  

**한계**
- 연산량 많아 실시간 사용 어려움  
- YOLO 같은 1-stage Detector가 실시간 가능  

---

## ⚡ 1-stage Detector

### 01 1-stage Detector 개요

- Region Proposal 없이 Feature Extractor로 직접 검출  
- 단순한 구조 & 빠른 속도  
- 실시간 처리 가능  

---

### 02 YOLO v1 (You Only Look Once)

**YOLO란**
- CVPR 2016, 1-stage Detector 대표 모델  
- 단일 CNN으로 이미지 전체를 한 번에 예측 (Single Shot)  
- 이미지를 **S×S grid**로 분할, 각 셀이 Bounding Box + Class 확률 예측  

**Grid Image 방식**
- 객체 중심이 포함된 셀이 해당 객체 예측 담당  
- 각 셀은 여러 Bounding Box, Confidence, Class Probability 예측  

**Backbone**
- CNN 기반 Feature Extractor  
- 마지막 Conv Output이 각 Grid 셀의 Feature에 대응  

**Bounding Box + Confidence**
- 각 셀이 여러 Bbox와 Confidence 예측  
- Confidence = 개체 존재 확률 × IoU  

**Class Probability Map**
- 각 셀마다 Class별 조건부 확률 예측  
- 최종적으로 Confidence × Class Probability로 Score 계산  

**Output**
- 낮은 Confidence 박스 제거  
- 각 Class마다 NMS 수행 → 중복 박스 제거  

---

### YOLO Training Process

**Loss 구성**
1. **Localization Loss**  
   - 박스 좌표 (x, y, w, h) 오차  
   - 객체 중심을 포함하는 셀만 Loss 계산  

2. **Confidence Loss**  
   - 개체 존재 시: IoU 기반 Confidence  
   - 개체 없음 시: Confidence = 0  

3. **Classification Loss**  
   - 각 셀의 클래스 확률 (존재 시 1, 미존재 시 0)

→ 총 Loss = Localization + Confidence + Classification 제곱합  

---

### YOLO Test Process

1. 전처리 (resize, normalization)  
2. 모델 추론: 각 셀마다 Bbox, Confidence, Class 확률 출력  
3. NMS로 중복 박스 제거  
4. 최종 Detection 결과 산출  

---

### Experiments

| 모델 | FPS | 특징 |
|------|-----|------|
| YOLO | 45 | 빠른 속도, mAP 우수 |
| Fast YOLO | 155 | 매우 빠름, 정확도는 약간 낮음 |
| Faster R-CNN | 7 | 높은 정확도, 느린 속도 |

**결론:**  
- YOLO는 속도 측면에서 압도적  
- 정확도도 준수하여 **실시간 Object Detection에 적합**  
