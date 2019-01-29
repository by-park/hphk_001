# Homework 16

## 2019-01-29



다음과 같은 스키마를 가지는 DB 테이블 friends를 생성한다.

```sqlite
sqlite> CREATE TABLE friends (
   ...> id INTEGER,
   ...> name TEXT,
   ...> location TEXT
   ...> );
sqlite> INSERT INTO friends (id, name, location) VALUES (1, 'Justin', 'Seoul');                                 
sqlite> INSERT INTO friends (id, name, location) VALUES (2, 'Simon', 'New York');                        
sqlite> INSERT INTO friends (id, name, location) VALUES (3, 'Chang', 'Las Vegas');                   
sqlite> INSERT INTO friends (id, name, location) VALUES (4, 'John', 'Sydney');     
```



2. 스키마를 다음과 같이 변경한다.

```sqlite
ALTER TABLE friends ADD COLUMN married INTEGER;
```



3. 데이터를 다음과 같이 추가한다.

```sqlite
sqlite> UPDATE friends SET married = 1 WHERE id = 1;                       
sqlite> UPDATE friends SET married = 0 WHERE id = 2;                       
sqlite> UPDATE friends SET married = 0 WHERE id = 3;
sqlite> UPDATE friends SET married = 1 WHERE id = 4;      
```



4. 아래 동작을 수행하기 위한 SQL을 각각 작성하세요.

```sqlite
DELETE FROM friends WHERE married = 0;
```



5. 테이블을 삭제한다.

```sqlite
DROP TABLE friends;
```

