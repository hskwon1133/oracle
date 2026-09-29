import oracledb as db

#db connection

DB_USER = 'C##KH'
DB_PASSWORD = '1234'
DB_DSN = '192.168.40.92:1521/xe'

conn = db.connect(user= DB_USER, password = DB_PASSWORD, dsn = DB_DSN)

#db insert cursor로 진행

cursor = conn.cursor()


a = input('title: ')
b = input('content: ')
sql = "INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES (1, :t, :c)" #세미콜론 제거 # fstring 대신 :t, :c로 바인더 활용해서 가능, 따옴표 세개로 해서 탭 구분으로 진행도 가능
sql_params = {
    't' : a,
    'c' : b
}
cursor.execute(sql, sql_params)
result = cursor.rowcount
print(result)

#트랜잭션, 커밋
conn.commit()
conn.close() # 연결 후 종료