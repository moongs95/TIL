# Data info & readiness check & Sampling


## Data info check

- 수집된 데이터의 기본 정보들을 확인
- 데이터를 읽고 형태, 타입, 기간 등 전반적인 기본정보 파악
- 전처리도 같이 수행

1. data shape 확인
2. data type 확인
3. null값 확인
4. 중복 데이터 확인
5. outlier 확인


## Data readiness check

- 데이터 수준 사전 점검
- 현재 가지고 있는 데이터 수준으로 문제를 해결할 수 있는지 점검

1. Target label 생성
2. Target Ratio 확인
3. 분석 방향성 결정


## Sampling

- sampling 수행 여부 결정
- 데이터 Mart 생성시간 단축
- 모델 학습 시간 단축

### Time series data

- up-sampling
- down-sampling

### Non-time series Data

- Target data가 너무 적다면 Over-sampling
- Data가 너무 많다면 Under-sampling : Stratified sampling(층화추출) 진행
