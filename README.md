# pandas
## Netflix 목록 분류하기
### 0. Command Prompt
PowerShell이 아닌 Command Prompt로 VS Code 터미널 실행
### 1. 가상환경 세팅
`python -m venv .venv/`
### 2. Git ignore 세팅
`echo .venv/ >> .gitignore`
### 3. 가상환경 실행
`.venv\Scripts\activate.bat`
### 4. pandas 설치
`pip install pandas`
### 5. python 파일 생성
main.py에 작성하고, DB 연결 설정과 쿼리문 로직을 작성했다.
```
DB: netflix
TABLE: netflix_titles
```
## 어려웠던 부분
### 1. CSV 파일의 데이터가 비어있던 문제
#### 1-1. 문제

```
MySQL 연결 오류:  1054 (42S22): Unknown column 'nan' in 'field list'
```
#### 1-2. 해결

NaN 값을 NULL로 변환하고 DB에 저장해서 해결
```
# NaN 값을 NULL로 변환
dataframe = dataframe.where(pd.notnull(dataframe), None)
```

### 2. DB 컬럼 설정
#### 2-1. 문제
```
MySQL 연결 오류:  1406 (22001): Data too long for column '출연진' at row 1
```

#### 2-2. 해결
cast(출연진)의 수가 많아서, VARCHAR의 길이를 255 -> 1000으로 변경해서 저장
```
출연진 VARCHAR(1000),
```