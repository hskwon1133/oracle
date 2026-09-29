# 모듈 설치 :  pip install oracledb
import oracledb as db

#CONNECTION 준비

DB_USER = "C##KH"
DB_PASSWORD = "1234"
DB_DSN = 'localhost:1521/xe' #localhost:port/sid  소문자 대문자 전환 ctrl+shift+u


conn = db.connect(user = DB_USER, password = DB_PASSWORD, dsn = DB_DSN)

print(conn.version)


#SQL 실행
#결과 처리

