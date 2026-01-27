# OCR Detection

# 검출기 구조 이해하기

## 01. Text Detection

### 1.1 Overview
- 이미지에서 **텍스트가 존재할 수 있는 영역**을 찾는 과정
- OCR 파이프라인의 첫 단계로, 이후 인식 성능에 직접적인 영향을 미침

---

### Text Detection의 Hard Cases
텍스트 검출기는 다음과 같은 어려운 상황에서도 텍스트를 찾아야 함:

- 글자가 왜곡되어 있어도 **텍스트로 인식**
- 글자의 일부가 가려져 있어도 **텍스트 영역으로 판단**
- 특이한 형태여도 **하나의 단어(문자열)** 로 인식

---

### 사람은 어떻게 글자를 인식하는가?
- 사람은 **언어를 몰라도** 글자를 글자로 인식 가능
- 의미를 해석하는 것이 아니라
  - “글자처럼 보이는 패턴”을 인지

👉 **Text Detector도 동일**
- 언어를 이해하지 않음
- “글이 존재할 것 같은 위치에 있는 글자 형태”를 검출

---

## 1.2 Regression-based Text Detection

### Regression-based 방식 개요
- **Bounding Box (직사각형)** 형태로 Text Area를 찾는 모델
- 일반적인 Object Detection 접근과 유사

---

### Ground Truth
- Ground Truth의 형태는 데이터셋마다 다르게 제공될 수 있음
- 보통 직사각형 Bounding Box 형태

---

### Region Proposal
- 글자가 있을 법한 위치를 **후보 영역**으로 생성
- 예시:
  - Selective Search

---

### NMS (Non-Maximum Suppression)
- 동일한 텍스트를 가리키는 여러 Bounding Box 중
  - **중복 박스 제거**
  - 가장 신뢰도 높은 박스만 유지

---

### Final Output
- Cropped Images
- 또는 `.json` 형태의 Bounding Box 정보

---

### Text Direction
- Bounding Box의 **Left-Top 좌표가 기준**
- 시계 방향으로 좌표 정의

---

## 1.3 Segmentation-based Text Detection

### Segmentation-based 방식 개요
- **Polygon (다각형)** 형태로 Text Area를 찾는 모델
- 글자의 형태를 보다 정밀하게 표현 가능

---

### Ground Truth
- Ground Truth는 다양한 형태로 제공
- 주로 Polygon 기반 어노테이션

---

### Segmentation Map
- 이미지의 **각 픽셀을 분류**
- Text / Background 또는 다중 클래스

---

### Instance Segmentation
- 각 텍스트 인스턴스별로
  - **독립적인 Segmentation Mask** 생성

---

### Final Output
- 투명 배경을 가진 Cropped 이미지
- 또는 `.json` 형태의 Polygon 정보

---

## 1.4 Appendix

### Regression vs Segmentation 비교

| 구분 | Regression-based | Segmentation-based |
|------|------------------|--------------------|
| 글자 왜곡 파악 | 불가능 | 가능 |
| 겹친 문자 제거 | 불가능 | 가능 |
| 라벨링 비용 | 낮음 | 높음 |
| 출력 형태 | Bounding Box | Polygon / Mask |

---

### Layout Analysis
- 단순 텍스트 검출을 넘어
  - **텍스트의 역할(semantic)** 까지 예측
- 예시:
  - 제목
  - 본문
  - 표
  - 캡션 등

---

### Multi-class Text Detection
- 기존 Binary Classification (Text / Background)에서 확장
- 다중 클래스 텍스트 검출
  - 문서 구조 이해를 위한 핵심 기술
