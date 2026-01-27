# OCR 개론

# OCR 모델의 구성 요소

## 01. OCR Pipeline

### 1.1 OCR Pipeline 개요
- 검출기(Text Detector)와 인식기(Text Recognizer)를 **분리하여 학습**하는 OCR 모델의 inference 파이프라인

```text
Document Images
→ Image Pre-processing
→ Text Detection
→ Text Recognition
→ Restructuring (Optional)
→ Output Text
```


---

### 1.2 Image Pre-processing
딥러닝 모델이 입력 이미지를 **효과적으로 처리**할 수 있도록 정제하는 과정

#### 주요 기법
- **Keystone Correction**
  - 사다리꼴처럼 왜곡된 직사각형 이미지를 보정
- **Line Straightening**
  - 각 줄이 가지는 곡선 왜곡 수정
- **Deskew / Skew Correction**
  - 이미지 기울기 보정
- **Denoising & Binarized Image**
  - 이미지 이진화 과정에서 노이즈 제거
  - 불필요한 색상 제거가 중요

#### File-level Pre-processing
- 하나의 이미지에 두 장의 문서가 포함된 경우
  - 한 장씩 **분리(split)** 하는 작업

---

### 1.3 Text Detection
- 이미지에서 **텍스트가 존재할 수 있는 영역**을 찾는 과정

#### Object Detection 관점
- Computer Vision의 객체 검출 문제와 유사

#### Text Segmentation
- Object Detection과의 차이점:
  - 분류 라벨이 **Background / Text**의 이진 분류

#### Text Recognition의 필요성
- 검출 결과만으로는 **텍스트의 의미 파악 불가**
- Text Detection + Text Recognition으로 역할 분리

#### Layout Analysis
- **Text Detection (with semantic entity)**
  - 단순 텍스트 여부가 아닌
  - 해당 박스가 어떤 역할인지 분류
- 초기: Binary Classification
- 현재: 다중 클래스 분류로 진화

---

### 1.4 Text Recognition
- Word Box 내부의 텍스트를 실제 **문자열로 인식**

#### Word Box
- 인식기에 입력되는 **최종 텍스트 영역**

#### Recognition Pipeline
- 이미지 → Visual Feature Map
- Feature Map을 기반으로 **문자 시퀀스 출력**

---

### 1.5 Restructuring
- 인식된 텍스트 정보를 **사람이 이해하기 쉬운 형태로 정렬**

#### 필요성
- 인식기는 텍스트를 **순서 없이 나열**
- 위치 정보를 기반으로 **재배열(정렬)** 필요

#### 복원 수준
- 위치 정보만 복원
- 테이블 구조까지 복원
  - 표, 도식 등까지 포함한 **고도화 단계**

---

# OCR 데이터 탐구

## 01. Overview

### 1.1 데이터 구조

#### Text Area
- Bounding Box (BBox)

#### Text Direction
- **Left-Top 좌표**가 중요
- 시계 방향 순서로 정의

#### Polygon 형태
- 사각형이 아닌 **다각형(Polygon)** 형태의 Text Area

#### Feature 형식
- JSON
- non-JSON
- No lexicon

---

### 1.2 데이터 목록

#### English Dataset

| Dataset Name | Type | Text Detection | Text Recognition |
|-------------|------|----------------|------------------|
| COCO Text v2 | Scene | ✓ | ✓ |
| CTW1500 | Scene | ✓ | ✓ |
| CUTE80 | Scene | ✓ | - |
| FUNSD | Document | ✓ | ✓ |
| NAF | Document | ✓ | ✓ |
| Text OCR | Scene | ✓ | ✓ |
| Total Text | Scene | ✓ | ✓ |

---

#### 한국어 데이터셋

| Dataset Name | Type | Text Detection | Text Recognition |
|-------------|------|----------------|------------------|
| 공공행정문서 | Document | ✓ | ✓ |
| 야외 실제 촬영 이미지 | Scene | ✓ | ✓ |
| 대용량 손글씨 | Document | ✓ | ✓ |
| 금융업 특화 문서 | Document | ✓ | ✓ |
| 의약품·화장품 패키징 | Scene | ✓ | ✓ |

---

# OCR 합성 데이터 탐구

## 01. OCR 합성 데이터

### 1.1 Synthetic Text Image
- 이미지와 Word Box를 **합성하여 생성**한 OCR 데이터

#### 합성 데이터의 필요성
- OCR 데이터 부족
  - 라벨링 난이도가 높음
    - 낮은 해상도
    - 다양한 글씨체
    - Bounding Box 라벨링의 어려움
  - 인적 비용 증가
- 적절한 이미지 수집의 어려움
  - 저작권 문제
  - 해상도 문제

---

#### OCR에서 합성 데이터 활용성이 높은 이유
- 사진 속 글자는 사람이 의도적으로 만든 **인공물**
  - 그 의도를 기계적으로 모방 가능
  - 연구를 통해 실제 데이터와의 간극 감소 가능

- 검출기와 인식기로 분리된 모델 구조
  - 검출기 전용 합성 데이터 생성 가능
  - 인식기 전용 합성 데이터 생성 가능

---

#### 합성 데이터 생성 전략

##### 검출기용 합성 데이터
- 다양한 배경 활용
- 기하학적 왜곡, 조명 변화 생성 가능

##### 인식기용 합성 데이터
- 배경 제약 없이 다양한 단어 생성
- 글자 자체의 변형으로 난이도 조절
- 변형이 심해도 **Ground Truth 확보 가능**

---

### 1.2 MJSynth
- **Word Box 이미지 생성** 합성 엔진
- 이를 기반으로 만든 데이터셋
- 특징:
  - **Text Recognition 전용**
  - 단어 단위 학습에 최적화

---

### 1.3 SynthText
- **Scene Text Image 생성** 합성 엔진
- 데이터셋 특징:
  - Text Detection
  - Text Recognition
  - **두 작업 모두 지원**

---

### 1.4 그 외 이미지 합성 엔진

#### UnrealText
- 3D 그래픽 엔진 **Unreal Engine 4.22** 기반
- Scene Text Image 생성
- 더 자연스러운 음영과 그림자 표현 가능

---

#### Editing Text in the Wild (SRNet)
- 이미지 번역을 위한 **데이터 증강 모델**
- OCR 데이터 증강 모델로 활용 가능성
- 실제 환경의 텍스트 편집을 모방

---

#### Document Synthetic Data
- 전체 문서 형태 합성은 난이도 높음
- 활용 전략:
  - 인식기에 다양한 단어 학습
  - 도메인 특화 사전(Dictionary) 기반 합성 데이터 생성
