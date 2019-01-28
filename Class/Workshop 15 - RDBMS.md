# Workshop 15 - RDBMS

## 2019-01-28

1. 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data를 입력해봅시다.

| id(INTEGER) | name(TEXT) | debut(INTEGER) |
| ----------- | ---------- | -------------- |
| 1           | Queen      | 1973           |
| 2           | Coldplay   | 1998           |
| 3           | MCR        | 2001           |

```sqlite
sqlite> CREATE TABLE bands (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT,
   ...> debut INTEGER);
   
sqlite> INSERT INTO bands (name, debut) VALUES ('Queen', 1973);
sqlite> INSERT INTO bands (name, debut) VALUES ('Coldplay', 1998);
sqlite> INSERT INTO bands (name, debut) VALUES ('MCR', 2001);
```



2. bands 테이블에서 모든 데이터 레코드의 id와 name만 조회하는 Query를 작성하라.

```sqlite
sqlite> SELECT id, name FROM bands;
```



3. bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 Query를 작성하라.

```sqlite
sqlite> SELECT name FROM bands WHERE debut < 2000;
```

