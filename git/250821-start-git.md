# Start git

## Index

- shell, vim command
- what is git?
- git command

### Shell, Vim Command

1. shell command

```shell
$ ls
$ ls -al
$ cd dev
$ mkdir bin
$ cp main.py bin
$ mv main.py bin
```

2. vim command

vim은 지구상의 가장 완벽한 텍스트 에디터 입니다.

```text
mode:
normal, insert, visual, command-line
```

### Set configuration

```shell
$ git config --global user.name {username}
$ git config --global user.email {emailaddr}
```

### How to start

```shell
$ git clone {repo-addr}
$ cd {repo}
```

### Branch basic

fuzzvizz algorithms를 이용한 branch 실습

```shell
$ git branch fuzz
$ git switch fuzz
$ vi fuzzbuzz.py
$ git add fuzzbuzz.py
$ git commit -m "feat: Print 'fizz'"
$ git switch main
$ git merge fizz
```
