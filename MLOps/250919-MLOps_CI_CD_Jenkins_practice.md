# CI/CD

## Continuous Integration(CI, 연속 통합)

- 개발자들이 코드 변경 사항을 중앙 저장소에 정기적으로 병합하는 것을 의미
- 이 과정에서 자동화된 빌드 및 테스트가 수행되어 코드 변경이 주 저장소에 통합되기 전에 문제를 조기에 발견하고 해결

## Continuous Deployment(CD, 연속 배포)

- 테스트를 거친 코드를 자동으로 production 환경에 배포하는 과정
- 수동 개입 없이도 새로운 코드 변경 사항이 사용자에게 신속하게 도달하도록 함

## MLOps에서의 중요성

- 빠른 반복과 지속적인 개선 : 모델 반복 속도 향상, 모델을 지속적으로 개선하고 최적화
- 품질 보증 및 신뢰성 : 자동화된 테스트로 모델의 정확도, 성능 및 안정성을 지속적으로 모니터링하고 검증
- 협업 및 투명성 강화 : 데이터 과학자, 개발자, 운영 팀 간의 협업을 강화, 코드, 데이터, 모델의 변경사항이 지속적으로 통합되어 모든 이해 관계자가 최신 상태를 파악
- 배포 및 운영의 간소화 : 자동화된 배포로 수동 프로세스에서 발생할 수 있는 오류를 줄이고 배포 속도를 향상

## Workflow Management와 무엇이 다른가?

- CI/CD 도구 : 개발 이후 서비스 어플리케이션, 소프트웨어 개발 및 배포 상품화에 초점
- Workflow Management : 개발 단계 절차 자동화, 데이터 개발 분야에 초점

## CI/CD 도구

### Jenkins

- Java로 작성된 오픈소스 자동화 서버, 소프트웨어 개발의 연속적 통합 및 연속적 배포를 위한 도구
- 주요 특징 : 플러그인 생태계, 유연성과 확장성, 마스터-슬레이브 아키텍처, 강력한 커뮤니티 지원, 광범위한 플러그인, 높은 커스터마이징

### GitLab CI/CD

- 소스 코드 관리와 CI/CD가 통합된 웹 기반의 DevOps 생명주기 도구
- 주요 특징 : 통합된 환경, YAML 파일 기반의 파이프라인 구성, 자동화된 테스트 및 배포, 통합된 솔루션, 간편한 설정, 높은 가시성

### GitHub Actions

- GitHub 저장소에 내장된 CI/CD 기능으로 소프트웨어 워크플로우를 자동화
- 주요 특징 : 깊은 GitHub 통합, 마켓플레이스, 다양한 운영 체제 지원, GitHub과의 원활한 통합, 쉬운 설정, 다양한 커뮤니티 기반 액션

### Circle CI

- 클라우드 기반 CI/CD 서비스로 빠른 빌드 테스트 및 배포를 지원
- 주요 특징 : 컨테이너 기반의 아키텍처, 쉬운 통합, 병렬 처리, 빠른 빌드 속도, 사용의 용이성, 강력한 병렬 처리 가능

### Travis CI

- GitHub 프로젝트에 쉽게 통합되는 CI 서비스로, 오픈 소스 프로젝트에 널리 사용
- 주요 특징 : GitHub와의 긴밀한 통합, YAML 파일을 통한 설정, 다양한 언어 지원, 간단한 설정, 다양한 언어 지원, 오픈 소스 프로젝트에 대한 무료 사용

# Jenkins CI/CD practice

## Jenkins 환경 구축

- Docker를 활용해 환경을 구축
- docker compose 파일 작성
- 커맨드 실행 : docker-compose up
- localhost 접속

## 비밀번호 확인

- 컨테이너 ID 확인
- 커맨드 실행
- docker ps
- 커맨드 실행
- docker logs [컨테이너 ID]
- 비밀번호 확인 후 들어감
- 초기에 id, pw, email 설정

## Jenkins Hello World

- +New Item
- Pipeline 선택
- Pipeline script 작성

```bash
node{
  // init stage
  stage("init"){ # 깃허브 코드가 자동으로 변경 감지, 태스크 수행으로옮겨옴
  sh "echo init hello world"
  }
  // build stage
  stage("build"){ # 코드를 기반으로 머신러닝 다시 학습
  sh "echo start build"
  }
  // deploy stage
  stage("deploy"){ # 평가 후 적합하면 서빙
  sh "echo deploying"
  }
}
```

- init(깃허브 코드변화 감지, 옮기기) -> build(모델 학습 - airflow에서 workflow 실행) -> deploy(학습된 모델을 상품화하기 위해 옮기기)
- CI/CD 자동화 과정
```text
1. airflow에 workflow가 있음
2. 각각의 work가 컨테이너로 존재
3. 깃에서 코드가 변경
4. 코드를 해당 컨테이너 도커에 옮겨주고 다시 build
5. image를 다시 push
6. airflow에서 docker registry 해당 컨테이너 업데이트 수행
```
