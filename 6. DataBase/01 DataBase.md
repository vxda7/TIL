# 01 DataBase

### 기본 용어

##### 스키마( scheme) : 정의

##### Primary Key(기본키) : 각 행의 고유 값 반드시 설정해야하고 데이터베이스 관리 및 관계 설정시 주요하게 활용됨.

##### SQL(Structured Query Language) : 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계	된 특수 목적의 프로그래밍 언어

##### DDL 데이터 정의 언어: 정의하기 위한 언어	CREATE, DROP, ALTER

##### DML 데이터 조작 언어: 저장, 수정, 삭제, 조회	INSERT, UPDATE, DELETE, SELECT

##### DCL 데이터 제어 언어: 사용자 권한 제어를 위한 언어	GRANT, REVOKE, COMMIT, ROLLBACK



```sql
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- CREATE
INSERT INTO classmates (name, age, address) 
VALUES ('김승연', 26, '전대');

-- 확인
SELECT * FROM classmates;

-- CREATE
INSERT INTO classmates (name, address) 
VALUES ('김승연', '전대');

-- 데이터 확인
SELECT * FROM classmates;
-- 모든열에 데이터를 넣을 때는 데이터를 명시할 필요가 없당
INSERT INTO classmates
VALUES ('홍길동', 30, '서울');

-- 구조확인
.schema classmates

-- NOT NULL 필수항목
CREATE TABLE classmates(
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

-- 여러개 넣을 수 있음
VALUES ('홍길동', 30,'서울'), ('김철수', 23, '대전'), ('박나래', 23, '광주'), ('이요셉', 33, '구미');

-- rowid는 PRIMARY KEY 가 없으면 항목당 id로 들어감
SELECT rowid, name FROM classmates;

-- 원하는 부분 찾기 LIMIT 특정 갯수 OFFSET 위에서 무시할 갯수
SELECT rowid, * FROM classmates LIMIT 1 OFFSET 2;

-- DISTINCK 다음에 나오는 값을 기준으로 중복되는 값을 제외한 값들 출력
SELECT DISTINCT age FROM classmates;

-- WHERE 원하는거 찾기
SELECT rowid, * FROM classmates WHERE address="서울";

-- DELETE 방법
DELETE FROM classmates WHERE rowid=4;

-- UPDATE
UPDATE classmates SET name="홍길동",age="10000",address="여수" where name="아무나";
```



users 예제들 AVG, MAX, LIKE 사용법들 _ == ? , % == *

```sql
.mode csv
.import users.csv users
.headers on


.tables
-- SELECT * FROM users;
-- 나이가 30 이상인 사람
SELECT * FROM users WHERE age>=30;

-- 나이가 30 이상인 사람의 이름
SELECT first_name FROM users WHERE age >= 30;

-- 나이 30 이상이고 성이 김씨인 사람들의 성과 나이 출력
SELECT last_name, age FROM users WHERE age>=30 AND last_name="김";

-- 레코드의 갯수 반환
SELECT COUNT(*) FROM users;

-- 나이 30 이상의 성이 김씨인 사람들 수
SELECT COUNT(*) FROM users WHERE age>=30 AND last_name="김";

-- 나이가 30 이상인 사람의 평균
SELECT AVG(age) FROM users WHERE age>=30;

-- 계좌 잔액이 가장 높은 사람과 액수는?
SELECT first_name, MAX(balance) FROM users;

-- 나이가 30 이상인 사람들의 평균 계좌 잔액은?
SELECT AVG(balance) FROM users WHERE age >= 30;

-- 스키마로 표현하면 가져온 데이터는 전부 TEXT타입이 된다.
.schema users

-- users 에서 20대인 사람의 테이블은?
SELECT * FROM users WHERE age LIKE '2_';

-- users 에서 지역번호가 02인 사람?
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';

--users 에서 준으로 이름이 끝나는 사람?
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';

--중간번호가 5114 인 사람 
SELECT * FROM users WHERE phone LIKE '%-5114-%';
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

-- users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
SELECT * FROM users ORDER BY age LIMIT 10;

-- users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

-- users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람이름 10개만 뽑아보면?
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

DROP TABLE users;
```

