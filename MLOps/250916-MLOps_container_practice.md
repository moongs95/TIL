# Container 실습

## Hello Docker World

- 1단계 : Dockerfile 작성
- 2단계 : Dockerfile 내에 스크립트를 실행한다면, 스크립트를 작성
- 3단계 : Docker 이미지 빌드
- 4단계 : Docker 컨테이너 실행

```bash
vi Dockerfile
# 기본 이미지로 Python 3.8  사용
FROM python:3.8-slim
# 작업 디렉토리 설정
WORKDIR /app
# python 스크립트 복사
COPY main.py /app
# 스크립트 실행
CMD ["python", "./main.py"]

vi main.py
print("Hello, Docker World!!!")

docker build -t hello-world-python .
docker run hello-world-python
```

## 서버 Docker Container

- 1단계 : Docker Registry 확인 및 검색
- 2단계 : docker login
- 3단계 : docker search nginx
- 4단계 : docker pull nginx
- 5단계 : docker images ls
- 6단계 : docker run -it -d -p 8001:80 --name nginxserver nginx:latest

```bash
# docker hub에서 nginx 찾기
docker search nginx
# 이미지 다운로드
docker pull nginx
# 이미지 확인
docker images
# 컨테이너 실행, 백그라운드에서 돌리겠다는 뜻
docker run -it -d -p 8001:80 --name nginxserver nginc:latest
# 컨테이너 확인
docker ps
curl localhost:8001
# 컨테이너 종료
docker stop
# 이후에 run 안하고 start만 해도 됨
docker start nginxserver
```

### html 변경 실습

1. 해당 docker의 컨테이너로 접속해서 index.html을 변경 할 수 있음

```bash
docker ps
# 해당 docker container로 들어가기
docker exec -it [docker id] bash
# html 파일이 있는 곳으로 이동
cd /usr/share/nginx/html
# index.html 변경
echo "변경하고 싶은 내용" > index.html
# 컨테이너 나가기
exit
```

2. 로컬에 있는 index.html을 docker에 있는 특정 경로로 이동시켜서 변경

```bash
# html 내용 작성
vi index.html
# 도커 컨테이너 안 위치에 복사
docker cp index.html nginxserver:/usr/share/nginx/html/index.html
```

## Scikit-learn Docker Container

- 1단계 : Dockerfile 작성
- 2단계 : python script 작성
- 3단계 : Docker 이미지 빌드
- 4단계 : Docker 컨테이너 실행
- 5단계 : docker image tag 변경
- 6단계 : docker image를 registry에 저장
- 7단계 : 로컬에 있는 docker image 삭제
- 8단계 : registry에 저장된 image를 로컬로 다운로드 받아서 실행

```bash
# 도커파일 작성
vi Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY model_learn.py /app/
CMD ["python", "./model_learn.py"]

# 환경변수 작성
vi requirements.txt
scikit-learn
pandas
numpy

# 모델 파일 작성
vi model_learn.py

# 도커 빌드 생성
docker build -t scikitlearn_modellearn .
# 도커 컨테이서 실행
docker run --name mldevelopment scikitlearn_modellearn

# 레파지토리 이용해서 허브 올리기
# 올리기 전 이름 꼭 변경! 도커 허브 아이디를 앞에 작성
docker tag [이미지 이름] [도커 허브 아이디]/[이미지 이름]
# 도커 로그인
docker login
# 도커 push
docker push [도커 허브 아이디]/[이미지 이름]

# 레파지토리 image 다운받아서 사용해보기
# 이미 만들어져 있는 image 삭제
docker rmi -f [이미지 ID]
# 허브에서 copy해서 pull실행
docker pull [도커 허브 아이디]/[이미지 이름]
# 컨테이너 실행
docker run --name test [도커 허브 아이디]/[이미지 이름]
```
