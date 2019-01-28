# SQLite

## 2019-01-28



- 데이터 베이스의 필요성을 확인하기 위해 flask로 웹페이지를 만들고 해당 내용을 csv에 저장하는 실습을 하였다. csv 파일은 원하는 행과 열을 쉽게 뽑아내기 어렵다.

- 데이터 베이스란?

  - 데이터베이스는 체계화된 데이터의 모임이다.

- RDBMS란?

  - 관계형 데이터베이스 관리 시스템. 데이터베이스의 많은 형태 중에서 엑셀처럼 칼럼과 로우의 관계 설정으로 데이터를 저장하는 것이다.

- SQLite란?

  - 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다.
  - c9 에 기본으로 설치되어있다.

- Schema 스키마란?

  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 알려준다. 각 칼럼의 자료형을 표현해주는 것이다.

- SQL이란?

  - RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다. (반대로 파이썬은 범용 언어이다.)
  - 1) 자료의 검색과 관리
  - 2) 스키마 생성과 수정
  - 3) 데이터 베이스 객체 접근 조정 관리

- 데이터 추가, 읽기, 수정, 삭제

  - 추가

    ```sqlite
    CREATE TABLE classmate (
    	id INT PRIMARY KEY,
    	name TEXT,
    	age INT,
    	address TEXT);
    INSERT INTO classmate (id, name, age) VALUES (1, '홍길동', 23)
    ```

  - 읽기

    ```sqlite
    SELECT * FROM classmate;
    SELECT name, address FROM classmates LIMIT 2 OFFSET 2;
    ```

  - 삭제

    ```sqlite
    DELETE FROM classmates WHERE id=5;
    ```

  - 수정

    ```sqlite
    UPDATE classmates SET address = '부산' WEHRE id = 1;
    ```
