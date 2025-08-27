# Data Mart & Feature Engineering


## Data Mart

1. Data Mart 기획 및 설계

- 모델링을 위한 Data Mart 기획
- 고객의 유니크한 특성을 Mart에 mapping함
- 전체 데이터를 넣는 것이 아니라 실제 이분석가가 프로젝트 목적에 맞게 마트를 만드는 것
- 미리 구축되어 있으니 작업 시작하기 용

2. Data 추출 및 Mart 개발

- 상위 단계에서 정의한 Data Mart를 기반으로 변수를 추출하는 과정
- 변수 추출은 Sampling한 데이터로 진행
- 가설에 따라 Mart를 얼마나 잘 구성하느냐가 분석가의 역량


## Feature Engineering

- 모델링의 목적인 성능 향상을 위해 Feature를 생성, 선택, 가공하는 일련의 모든 활동
- 차원이 너무 많은 경우에는 Domain 지식을 활용하여 축소할 것

1. Integer Feature Engineering
2. Categorical Feature Engineering


### 변수 선택 방법

1. Regression(회귀) : 상관계수 분석을 통해 유의미한 변수 선택, 다중공선성 확인
2. Classification(분류) : bin(통)으로 구분 후 Target 변수와의 관계 파악론
- IV 사용 : feature가 target과 non-target을 잘 구분해 줄 수 있는지에 대한 정보량을 표현하는 방법
