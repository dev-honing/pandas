# main.py
import os
import pandas as pd

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

if __name__ == '__main__':
    # CSV 파일 경로
    csv_file_path = os.path.join(os.path.dirname(__file__), 'netflix_titles.csv')
    
    # 데이터프레임 출력
    print(translate_and_classify_data(csv_file_path))
