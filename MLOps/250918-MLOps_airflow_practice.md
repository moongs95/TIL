# Airflow Workflow Management 실습

## 실습환경 구축

- docker container를 사용해서 docker image로 실행하기(독립적인 공간에서 수행)
- Dockerfile 정의

```dockerfile
FROM python:3.8-slim
# 환경 변수 설정
ENV AIRFLOW_HOME=/usr/local/airflow
# 필수 패키지 설치
RUN apt-get update && apt-get install -y gcc libc-dev libpq-dev vim \
    && rm -rf /var/lib/apt/lists/*
# pip 업그레이드
RUN pip install --upgrade pip
# Airflow 설치 (Python 3.8용 constraints 사용)
RUN pip install "apache-airflow==2.8.1" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
# Airflow 환경설정
RUN mkdir -p $AIRFLOW_HOME
WORKDIR $AIRFLOW_HOME
RUN airflow db init
# Airflow DAGs 폴더에 DAG 파일 복사
COPY my_dag.py $AIRFLOW_HOME/dags/
# Airflow 웹 서버 포트 노출
EXPOSE 8080
# Airflow 웹 서버 및 스케줄러 실행
CMD airflow webserver -p 8080 & airflow scheduler
```

- docker build 해주고 run을 포트설정으로 해줌

### 계정생성

```bash
docker ps
docker exec -it [container id] bash
airflow users create --username [name] --firstname [fn] --lastname [ln] --role Admin --email [email]
```
- 비밀번호 생성, 확인

## Airflow의 DAG

### 정의

- DAG(Directied Acyclic Graph)이며 Airflow에서 워크플로우를 정의하는 주요 구성요소
- 방향성을 가진 비순환 그래프이며, 여러 작업(Task)들과 이들 간의 의존성을 나타냄
- 작업(Task) : DAG 내에서 실행되는 개별 단위
- 의존성(Dependency) : 한 작업이 다른 작업에 의존하는 관계를 의미

### 구성 요소

- Operator : Airflow에서 작업을 수행하는 객체
- Task : Operator의 인스턴스로 DAG 내에서 실행되는 개별 작업
- Task Instance : 특정 시점에서의 Task의 실행 인스턴스
- Workflow : 전채적인 작업의 흐름을 나타내며 하나 이상의 DAG로 구성

### 주의 사항

- 의존성 순환 : DAG에서는 순환 의존성을 가질 수 없음
- 스케쥴링 : 'start_date'와 'schedule_interval'을 적절히 설정하여 작업이 예상대로 실행되도록 해야함
- 오류 처리 : 각 Task는 실패할 수 있으므로 오류처리 로직 고려

## Airflow DAG 실습

- 1단계 : dag 작성
- 2단계 : dag 실행
- 3단계 : dag 실행 결과 확인
