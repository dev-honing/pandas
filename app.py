# app.py
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL 연결 설정
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="netflix"
)

@app.route('/')
def index():
    # Netflix 제목 조회
    cursor = connection.cursor()
    cursor.execute("SELECT 제목 FROM netflix_titles")
    titles = cursor.fetchall()
    cursor.close()

    # HTML 템플릿 렌더링
    return render_template('index.html', titles=titles)

if __name__ == '__main__':
    app.run(debug=True)
