# Workshop 16

## 2019-01-29



1. 해당 테이블을 수정하여 (15 워크샵) 다음과 같이 컬럼을 추가하고 데이터를 삽입하라.

```sqlite
sqlite> CREATE TABLE bands (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT,
   ...> debut INTEGER);
sqlite> INSERT INTO bands(name, debut) VALUES ('Queen', 1973);
sqlite> INSERT INTO bands(name, debut) VALUES ('Coldplay', 1998);         
sqlite> INSERT INTO bands(name, debut) VALUES ('MCR', 2001);              
sqlite> ALTER TABLE bands ADD COLUMN members INTEGER;
sqlite> UPDATE bands SET members = 4 WHERE id = 1;
sqlite> UPDATE bands SET members = 5 WHERE id = 2;                         
sqlite> UPDATE bands SET members = 9 WHERE id = 3;    
```



2. id가 3인 레코드의 members를 5로 수정하라.

```sqlite
UPDATE bands SET members = 5 WHERE id = 3;  
```



3. id가 2인 레코드를 삭제하라

```sqlite
DELETE FROM bands WHERE id = 2;    
```

