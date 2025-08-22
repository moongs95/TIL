# Co-work with git, github

## Issue

- github 프로젝트의 다양한 이슈를 관리하기 위한 기능
- 할 일, 버그, 질문 등을 관리
- label, 상태 관리 등의 업데이트가 잘 이루어져야 원활한 작업 가능

## Milestone

## Projects

## wiki

## Pull Requests

- issue와 연결 가능
- close, resolve, fix #{issue-num}

## github flow with fork

1. issue 탭에서 issue 생성
2. fork해서 본인의 repo 생성
3. git clone {repo-addr}
4. cd로 이동 후 branch 생성해서 작업
5. git push oirgin -u {branch-name}
6. compare & full request 생성
7. 관리자에게 리뷰 받기

- 관리자는 리뷰 후 approve or request하기
- 모든게 승인되면 merge함

```shell
git switch main
git remote -v
git remote add upstream {merged-repo-addr}
git remote -v
git fetch upstream main
git merge FETCH_HEAD
``` 
