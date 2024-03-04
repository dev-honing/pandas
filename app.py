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

# 데이터베이스에서 제목을 검색하는 함수
def search_titles(keyword, page, per_page):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="netflix"
    )
    cursor = connection.cursor(dictionary=True)

    # 페이지와 페이지당 아이템 수를 기반으로 오프셋 계산
    offset = (page - 1) * per_page

    # 데이터베이스에서 제목을 검색하는 쿼리문 실행
    cursor.execute("SELECT * FROM netflix_titles WHERE 제목 LIKE %s LIMIT %s OFFSET %s", ('%' + keyword + '%', per_page, offset))
    titles = cursor.fetchall()

    # 연결 및 커서 닫기
    cursor.close()
    connection.close()

    return titles

# 검색 결과를 보여주는 라우트
@app.route('/search')
def search():
    keyword = request.args.get('keyword')  # 검색어
    page = int(request.args.get('page', 1))  # 페이지
    per_page = 10  # 페이지당 아이템 수

    # 제목 검색
    titles = search_titles(keyword, page, per_page)

    # 검색 결과를 index.html로 전달하여 렌더링
    return render_template('index.html', titles=titles, page=page)

# 메인 페이지 라우트
@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = 10

    # 제목 목록 가져오기
    titles = get_titles(page, per_page)

    return render_template('index.html', titles=titles, page=page)

if __name__ == '__main__':
    app.run(debug=True)
