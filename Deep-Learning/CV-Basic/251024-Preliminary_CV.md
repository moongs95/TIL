# 고전 컴퓨터 비전

## 01 고전 컴퓨터 비전

### 1.1 고전 컴퓨터 비전이란?

- 고전 컴퓨터 비전: 규칙 기반의 이미지 처리 알고리즘 (e.g. OpenCV)
    - 주어진 입력 → 원하는 형태 → 인간이 직접 만듦
- 딥러닝: 데이터 학습 기반의 이미지 처리
    - 입력에서 원하는 출력을 정의, 출력과의 오차를 줄이면서 업데이트

### 1.2 고전 컴퓨터 비전의 활용

- 딥러닝으로 해결하기 어려운 문제에 활용 (e.g. 로보틱스, 가상현실)
- 딥러닝 모델의 결과의 후처리
- 딥러닝 모델 없이 데이터를 가공 할 때 활용
    - Morphological Transform
    - Edge & Contour Detection

⇒ 딥러닝은 다량의 데이터가 필요함. 정답 라벨을 고전 컴퓨터 비전으로 만들어서 정확도 높임

## 02 Morphological Transform

### 2.1 Morphological Transform이란?

**정의**

- 이미지에 기반한 연산이며, 흑백 이미지에서 일반적으로 수행
- 입력: 원본 이미지, 커널(연산자)
- 커널의 종류
    - Erosion
    - Dilation
    - Opening
    - Closing
    - Morphological gradient
    - Top hat

→ 다양한 연산 제공

**중요성**

- Morphological transform은 이미지 전처리 영역에서 유용하게 사용
- ex. opening 연산을 통해 이미지의 노이즈를 제거하는데 사용 가능

### 2.2 Erosion이란?

**정의**

- Erosion: 물체의 경계를 침식
- 이미지의 특징을 축소할 때도 사용 가능

**동작 원리**

- 홀수 크기의 커널이 이미지와 컨볼루션 연산을 수행
- 커널 아래 모든 픽셀이 1이면 1, 그 외에는 0이 됨
- 경계(0→1바뀌는 곳) 근처의 픽셀은 침식

→ 물체의 두께가 얇아짐

### 2.3 Dilation이란?

**정의**

- Dilation은 Erosion과는 정반대로 동작
- 사물의 크기를 팽창할 때도 사용 가능

**동작 원리**

- 홀수 크기의 커널이 이미지와 컨볼루션 연산을 수행
- 커널 아래의 하나 이상의 픽셀이 1이면 1, 그 외에는 0이 됨
- 경계 근처의 픽셀은 팽창

### 2.4 Opening이란?

**정의**

- Opening은 Erosion 커널과 Dilation 커널 순서대로 동작되는 연산
- 반대로 동작시키면 (Dilation->Erosion), Closing 커널이라고 부름
- 노이즈를 제거하는데 사용
- 물체의 경계도 얇아짐 → dilation으로 원래대로 복원

## 03 Contour Detection

→ 이미지에서 객체의 경계를 찾음

### 3.1 Contour Detection

**목표**

- Contour: 같은 색깔 및 intensity를 가지는 연속적인 경계점들로 이루어진 curve, 물체의 경계들
- 고전 컴퓨터 비전을 활용하여 raw image에서 객체의 contour를 추출

→ 2. edge 추출, 3. contour 추출

**중요성**

- 딥러닝 모델 사용 X
    - 딥러닝 모델 학습을 위한 데이터 가공 시 활용 가능
- 데이터가 부족하면 초기 데이터 가공 상태에서 딥러닝 성능이 더 떨어질 수도 있음
- 다양한 환경에서도 딥러닝 모델을 잘 구축하려면 여러 상황에서도 쉽고 비용 효율적인 고전 컴퓨터 비전 기술로 전처리하는 능력이 중요

**과정**

- Edge detection -> Dilation (optional) -> Contour detection

- 입력 → 엣지 추출 결과 : 바이너리(엣지는 1, 아닌부분 0) → 선택적으로 dilation 연산으로 너무 세밀한 엣지는 합쳐줌 → 알고리즘을 통해 엣지들이 이어져 있는 커브들을 찾아서 경계 반환

### 3.2 Canny Edge Detector

- 컴퓨터 비전에서 가장 널리 사용되는 edge detector
- 1986년 TPAMI에 발표된 논문으로, John Canny에 의해 개발됨 → 상당히 오래됨

**장단점**

- (장점) 정확도 높음
- (단점) 실행 시간 느림
- (단점) 구현 복잡함

→ 현재는 컴퓨터 기술 발전으로 단점이 크게 보안됨

**과정**

- (1단계) 노이즈 제거
- (2단계) 이미지 내의 높은 미분값 찾기
- (3단계) 최대값이 아닌 픽셀 값 0으로 치환
- (4단계) 하이퍼파라미터 조정을 통한 세밀한 엣지 검출

**(1단계) 노이즈 제거**

- 이미지 내에 노이즈가 있다면, 엣지를 찾는데 어려움이 있음
- 노이즈 줄이기 위해, 가우시안 필터 이용, 튀는 픽셀값 제거
    - 가우시안 필터란?
        - 가우시안 분포 함수를 근사하여 생성한 필터 마스크
        - 가우시안 필터 마스크 행렬은 중앙부에서 큰 값을 가짐
        - 중앙에서 외곽으로 갈 수록 0에 가까운 작은 값을 가짐

**(2단계) 이미지 내의 높은 미분값 찾기** - Find the intensity gradient

- Sobel 커널을 각 방향으로 적용하여 gradient를 추출
    - Sobel 커널이란?
        - 행 또는 열의 변화율을 계산하는 마스크
        - Edge 검출에 특화
- gradient : 열 또는 행 방향으로 픽셀값의 변화 정도 → 클수록 엣지일 확률이 높다!
- 수평방향의 gradient: Gx, 수직방향의 gradient: Gy
- Gradient의 방향은 엣지와 수직한 방향

**(3단계) 최대값이 아닌 픽셀 값 0으로 치환** - Non Maximum Suppression

- 목표: 엣지 검출에 기여하지 않은 픽셀을 제거
- Gradient 방향으로 gradient의 최대값을 가진 픽셀을 찾음
- 주변의 값과 비교하여, 엣지가 아닌 픽셀값들을 제거(0으로 치환)함

**(4단계) 하이퍼파라미터 조정을 통한 세밀한 엣지 검출** - Hyteresis Thresholding

- 2가지의 Threshold (Low Threshold, High Threshold)를 정의

### 3.3 Contour Edge Detection with OpenCV

**Contour Detection**

- Raw image를 binary image로 변환 -> OpenCV의 findContours() 함수 이용
    - Binary image를 만들 때 edge detection의 결과를 활용

- cv2.findContours()
