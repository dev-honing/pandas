# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 데이터베이스에서 제목 목록을 가져오는 함수
def get_titles(page, per_page):
    # 데이터베이스 연결 설정
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="netflix"
    )
    cursor = connection.cursor(dictionary=True)

    # 페이지와 페이지당 아이템 수를 기반으로 오프셋 계산
    offset = (page - 1) * per_page

    # 데이터베이스에서 제목 목록을 가져오는 쿼리문 실행
    cursor.execute("SELECT * FROM netflix_titles LIMIT %s OFFSET %s", (per_page, offset))
    titles = cursor.fetchall()

    # 연결 및 커서 닫기
    cursor.close()
    connection.close()

    return titles

# 메인 페이지 라우트
@app.route('/')
def index():
    # 현재 페이지와 페이지당 아이템 수 설정
    page = int(request.args.get('page', 1))
    per_page = 10

    # 제목 목록 가져오기
    titles = get_titles(page, per_page)

    # index.html 렌더링 및 데이터 전달
    return render_template('index.html', titles=titles, page=page)

if __name__ == '__main__':
    app.run(debug=True)
