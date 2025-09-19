# 서버 통신 이론 : HTTP & REST API

## HTTP

- HTTP(HyperText Transfer Protocol)는 웹 상에서 데이터를 교환하기 위한 프로토콜
- 텍스트, 이미지, 비디오 등 다양한 형태의 데이터를 클라이언트와 서버 간에 전송
- 월드 와이드 웹의 기초적인 기술 중 하나로, 인터넷의 급속한 성장과 발전에 기여

### 요청 응답 프로세스

- 클라이언트(웹 브라우저 혹은 앱, 소비자)가 서버에 특정 리소스를 요청
- 서버는 이 요청을 처리하고 적절한 응답을 클라이언트에 반환

### HTTP Method(Client 기준)

- GET : 정보 조회
- POST : 데이터 전송
- PUT : 데이터 업데이트
- DELETE : 리소스 삭제

### HTTP 상태코드

- 서버가 클라이언트의 요청을 어떻게 처리했는지 설명하는 코드
- 200 OK : 요청이 성공적으로 처리
- 300번대 : 리다이렉션
- 404 Not Found : 요청한 리소스를 찾을 수 없음
- 500 Internal Server Error : 서버 내부 요류

## REST API

- 웹 표준을 기반으로 서버와 클라이언트 간의 통신을 구현하기 위한 인터페이스
- 자원의 표현에 의한 상태 전달을 의미, 웹의 기본 프로토콜인 HTTP를 사용

### 작동원리

- '자원(URI), 행위(HTTP Method), 표현(Representation)' 세가지 구성요소로 이루어짐
- 클라이언트는 URI를 통해 자원을 지정, HTTP 메서드를 이용해 해당 자원에 대한 행위를 지정

### 상태 비저장성(Statelessness)

- 서버는 클라이언트 상태를 유지하지 않으며 각 요청은 독립적으로 처리
- 서버 처리가 단순화, 확장성이 증가

### MLOps에 적용

- 데이터 수집 및 처리
- 모델 서빙
- 모델 파이프라인 동작

# 서버 통신 실습

## 환경 구축

- Node.js 설치
- npm install socket.io
- npm install express
- index.js 작성(필요 라이브러리 import, 클라이언트 요청시 response, 포트 설정, listen 설정)
- Postman 설치 및 가입 : REST API를 쉽게 테스트할 수 있는 Tool

## REST API 실습

### 초기 설정 및 데이터 구조

- npm install express
- Express.js : Node.js의 Express.js 프레임워크를 사용하여 REST API를 구축
- 데이터 저장소 : 키-값 쌍으로 정보 책 정보 저장

### Index.js 구현

```java
const express = require('express'); # 프레임 워크
const app = express();
const port = 3000;

app.use(express.json());


let books = {
  '1': { title: '1984', author: 'George Orwell', year: 1949 },
  '2': { title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', year: 1925 }
};

// 모든 책 목록 가져오기
app.get('/books', (req, res) => {
	res.json(books);
});

// id 받아서 null이 아니면 책 목록 가져오고 else면 404
app.get('/books/:id', (req, res) => {
	const book = books[req.params.id];
	if(book) {
	   res.json(book);
	}
	else{
	   res.status(404).send("Book not found");
	}
});

// 새 책 추가, 성공하면 책 id 나타내기
app.post('/books', (req, res) => {
	const nextId = Object.keys(books).length + 1;
	books[nextId] = req.body;
	console.log(req.body);
	res.status(201).send("book added with ID : ${nextId}");
});

// update
app.put('/books/:id', (req, res) => {
  const id = req.params.id;
  if (books[id]) {
    books[id] = req.body;
    res.send(`Book with ID ${id} updated`);
  } else {
    res.status(404).send('Book not found');
  }
});

// delete
app.delete('/books/:id', (req, res) => {
  const id = req.params.id;
  if (books[id]) {
    delete books[id];
    res.send(`Book with ID ${id} deleted`);
  } else {
    res.status(404).send('Book not found');
  }
});


// listen으로 구현하겠다는 것을 알려줘야 함.
app.listen(port, () => {
  console.log(`Bookstore app listening at http://localhost:${port}`);
});
```

### 실행

- node index.js
- localhost의 /books
- postman에서 get, post, put(update), delete 작업 Send해보고 확인
