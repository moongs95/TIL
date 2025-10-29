# Object Detection Overview

## 01 Object Detection Overview

### 1.1 Object Detection이란?
- 이미지나 비디오에서 객체 탐지
- Task: Localization (위치) + Classification (종류)
- Bounding box: 객체 전체를 감싸는 최소 사각형
- Annotation: bounding box + class 라벨

### 1.2 Object Detection Usecases
- 보안/감시
- 자율주행
- 의료
- OCR

### 1.3 Object Detection History
- 2-stage detector
- 1-stage detector
- Transformer-based detector

## 02 Chapter Overview

### 2.1 2-Stage Detector
- Region Proposal + Classification 두 단계 수행
- 대표 모델: R-CNN, SPPNet, Fast R-CNN, Faster R-CNN

### 2.2 1-Stage Detector
- 2-stage 단계를 통합, 속도 빠름
- 대표 모델: YOLO, SSD, RetinaNet, CenterNet

### 2.3 Transformer-based Detector
- Transformer로 휴리스틱 과정 제거, 단순화
- 대표 모델: DETR, Swin-T

---

# 2-Stage Detector

## 01 2-Stage Detector

### 1.1 2-Stage Detector란?
- Stage 1: 객체 위치 탐지 (Region proposal)
- Stage 2: 객체 종류 분류 (Classification)

### 1.2 2-Stage Detector 발전
- R-CNN → SPPNet → Fast R-CNN → Faster R-CNN → FPN

## 02 R-CNN

### 2.1 R-CNN Overview
- 최초 2-stage detector
- Region proposals + CNN

### 2.2 Selective Search
- Sliding Window: 계산량 많고 느림
- Selective Search: 작은 영역 병합, 색상/질감/경계 기준

### 2.3 R-CNN Pipeline
1. Selective search로 ~2000 RoI 생성
2. RoI 크기 통일 후 CNN 통과
3. Feature vector 추출 (2000x4096)
4. SVM으로 classification / Regression으로 bbox 조정

## 03 Fast R-CNN

### 3.1 Limitations of R-CNN
- RoI마다 CNN 연산 → 느림
- 이미지 crop/resize 필요 → 성능 저하
- Stage2 모델 별도 학습

### 3.2 RoI Projection
- 전체 feature map 추출 후 RoI 투영 → CNN 연산 1번
- Fc layer 입력 전 feature vector 크기 조정

### 3.3 RoI Pooling
- 임의 크기 feature map → 고정 크기(WxH)로 pooling
- Grid로 나누어 max pooling

### 3.4 Fast R-CNN Pipeline
1. Selective search로 RoI 생성
2. 단일 CNN으로 feature map 생성
3. RoI projection/pooling → feature vector 생성
4. Classification + Bounding box regression 수행

## 04 Faster R-CNN

### 4.1 Limitations of R-CNN/Fast R-CNN
- Selective search 느림, CPU/GPU 모두 필요
- End-to-end 학습 불가

### 4.2 Region Proposal Network (RPN)
- Anchor box 기반 RoI 생성
- Intermediate layer → Classification, Bounding box regression
- NMS: 중복 bbox 제거

### 4.3 Faster R-CNN Pipeline
1. CNN으로 feature map 추출
2. RPN + NMS → RoI 생성
3. RoI projection/pooling
4. Softmax + bbox regression (end-to-end 학습)

### 4.4 Results
- 속도 크게 향상

## 05 Review
- R-CNN: 최초 2-stage detector, CNN 연산 많음
- Fast R-CNN: 단일 CNN + RoI pooling, 속도 향상, end-to-end 불가
- Faster R-CNN: RPN 도입, end-to-end, 속도 향상

---

# 1-Stage Detector

## 1 1-Stage Detector

### 1.1 1-Stage Detector란?
- 2-stage보다 연산 단순, 실시간 탐지 적합

### 1.2 1-Stage Detector 발전
- YOLO v1: 최초 1-stage detector, region proposal 제거
- YOLO v2: Better, Faster, Stronger
- YOLO v3: Multi-scale feature maps
- YOLO v4: 최신 딥러닝 기술 적용, CSPDarknet-53 backbone
- YOLO v5~v8: anchor-free, 다양한 task 통합

## 02 YOLO v1

### 2.1 Overview
- Bounding box + class 동시에 예측
- 전체 이미지 참조 → 맥락 이해 증가

### 2.2 Pipeline
1. 이미지 SxS grid 분할
2. 각 grid cell B개의 bbox + confidence score 예측
3. Conditional class probability 계산
4. Confidence score 기반 bbox filtering → NMS 적용

### 2.3 Darknet
- 24 conv layers + 2 fc layers
- Grid S=7, B=2, Class C=20
- Output: 7x7(2x5 + 20) (x, y, w, h, confidence + class)

### 2.4 Loss Function
- Localization loss + Confidence loss + Classification loss

### 2.5 Results
- 빠르지만 localization 정확도 낮음

## 03 YOLO v2

### 3.1 Overview
- YOLO v1 문제점: localization error, 낮은 recall
- YOLO 9000: Better, Faster, Stronger

### 3.2 Improvements

**Better**
- Batch normalization → mAP ↑
- High-res classifier → mAP ↑
- Anchor boxes → recall ↑
- Dimension clusters → optimal anchor → mAP ↑
- Direct location prediction → tx, ty logistic 적용 → mAP ↑
- Fine-grained features → 작은 객체 대응 → mAP ↑
- Multi-scale training → 다양한 input size 학습

**Faster**
- Darknet-19 backbone, fc 제거, global avg pooling

**Stronger**
- ImageNet + COCO joint training
- WordTree 활용 → 총 9418 classes

### 3.3 Results
- 이전 YOLO 대비 빠르고 정확도 개선

## 04 Other YOLOs

### 4.1 YOLO v3
- Multi-scale feature maps → 다양한 크기 객체 탐지
- Darknet-53 backbone

### 4.2 YOLO v4
- 최신 딥러닝 기법 적용
- Bag of Freebies: CutMix, Mosaic, Dropblock, label smoothing
- Bag of Specials: Mish activation, CSP, MiWRC
- CSPDarknet-53 backbone

## 05 Review
- YOLO v1: 최초 1-stage detector
- YOLO v2: Better, Faster, Stronger → anchor, multi-dataset, 속도·정확도 개선
- YOLO v3: Multi-scale feature map, Darknet-53
- YOLO v4: 최신 딥러닝 기법 + CSPDarknet-53, 정확도와 속도 향상

