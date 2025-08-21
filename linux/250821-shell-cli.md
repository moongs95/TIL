# Linux shell

## Index

- CLI basic

### 파일 목록보기

```shell
ls
ls -l
ls -a
ls *.txt
```

### 파일 만들기

```shell
touch hello.txt
touch test1 test2 test3
```

### 파일 내용 보기

```shell
cat hello.txt
more hello.txt
less hello.txt
```

### 파일 삭제

```shell
rm hello.txt
rm test1 test2 test3
```

### 디렉토리

```shell
mkdir dir1
mkdir -p dir2/sub1

rmdir dir1
rm -r dir2

cd dir1
cd ..
cd ../..
cd ~
cd -
```

### 파일 복사/이동

```shell
cp hello.txt hello2.txt
cp test1 dir1
cp -r dir1 dir2

mv hello.txt hello2.txt
mv test1 dir1
mv dir1 dir2
```

### 파일 링크

```shell
ln -s hello.txt hellosymlink
ln hello.txt hellolink

ls -ali
```

### 파일 속성 보기

```shell
file ehllo
file dir
file hellosymlink
```

### 시스템 종료

```shell
reboot
poweroff
shutdown
```

### 도움말/매뉴얼

```shell
man man
man -a printf
man -k printf
man -k ^printf
```

### 파일 편집기
```shell
vi hello.txt
nano hello.txt
```

