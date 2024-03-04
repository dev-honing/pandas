import os
import pandas as pd
import mysql.connector

def translate_and_classify_data(csv_file_path):
    # CSV 파일 읽기
    data = pd.read_csv(csv_file_path)

    # 번역 및 분류
    translated_data = data.rename(columns={
        'show_id': '연번',
        'type': '분류',
        'title': '제목',
        'director': '감독',
        'cast': '출연진',
        'country': '방영국가',
        'date_added': '추가날짜',
        'release_year': '개봉연도',
        'rating': '연령제한',
        'duration': '상영시간',
        'description': '부연설명'
    })
    
    return translated_data

def create_mysql_table(cursor):
    try:
        # 테이블 생성 SQL 쿼리
        create_table_query = """
            CREATE TABLE IF NOT EXISTS netflix_titles (
                연번 INT AUTO_INCREMENT PRIMARY KEY,
                분류 VARCHAR(255),
                제목 VARCHAR(255),
                감독 VARCHAR(255),
                출연진 VARCHAR(255),
                방영국가 VARCHAR(255),
                추가날짜 VARCHAR(255),
                개봉연도 INT,
                연령제한 VARCHAR(255),
                상영시간 VARCHAR(255),
                부연설명 TEXT
            )
        """
        # 테이블 생성
        cursor.execute(create_table_query)
        print("테이블 생성 완료!")

    except mysql.connector.Error as err:
        print("MySQL 오류: ", err)
    except Exception as e:
        print("테이블 생성 오류: ", e)

def insert_data_to_mysql(dataframe):
    try:
        # MySQL 연결 설정
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1234",
            database = "netflix"
        )

        cursor = connection.cursor() 

        # 테이블 생성
        create_mysql_table(cursor)

        # 데이터 삽입
        for index, row in dataframe.iterrows():
            sql = "INSERT INTO netflix_titles (연번, 분류, 제목, 감독, 출연진, 방영국가, 추가날짜, 개봉연도, 연령제한, 상영시간, 부연설명) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (row['연번'], row['분류'], row['제목'], row['감독'], row['출연진'], row['방영국가'], row['추가날짜'], row['개봉연도'], row['연령제한'], row['상영시간'], row['부연설명'])
            cursor.execute(sql, values)

        # 변경사항을 커밋하고 연결 종료
        connection.commit()
        connection.close()
        print("데이터 삽입 완료!")
    
    except mysql.connector.Error as err:
        print("MySQL 연결 오류: ", err)
    except Exception as e:
        print("데이터 삽입 오류: ", e)

if __name__ == '__main__':
    # CSV 파일 경로
    csv_file_path = os.path.join(os.path.dirname(__file__), 'netflix_titles.csv')
    
    # 번역된 데이터프레임 생성
    translated_data = translate_and_classify_data(csv_file_path)

    if translated_data is not None:
        # MySQL 데이터 삽입
        insert_data_to_mysql(translated_data)
        