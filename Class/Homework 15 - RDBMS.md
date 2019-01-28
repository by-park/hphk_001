# Homework 15 - RDBMS

## 2019-01-28



1. 우리가 사용하는 SQLite 는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하세요.

- 모든 데이터를 row와 column의 2차원 테이블로 표현한다.
- 상호관련성을 가진 테이블의 집합이다.



2. True False

2.1 RDBMS를 조작하기 위해서는 SQL문을 사용한다. [True]

2.2 SQL에서 명령어는 대문자로 써야만 동작한다. [False]

2.3 일반적인 SQL문에서 명령어는 세미콜론(;)으로 끝난다. [True]

2.4 SQLite에서 dot(.)  으로 시작하는 명령어는 SQL이 아니다. [True]

2.5 한 개의 DB에는 한 개의 테이블만 존재한다. [False]



3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.

```sqlite
.nullvalue "NULL"
CREATE TABLE ssafy (
	id INTEGER,
	location TEXT,
	class INTEGER
	);
INSERT INTO ssafy (id, location) VALUES (1, 'JEJU');
SELECT class from ssafy WHERE id = 1;

```



> NULL

