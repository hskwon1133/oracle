#delete

import oracledb as db

DB_USER = 'C##KH'
DB_PASSWORD = '1234'
DB_DSN = 'localhost:1521/xe'

conn = db.connect(user = DB_USER, password = DB_PASSWORD, dsn = DB_DSN)

# cursor 진행

cursor = conn.cursor()

b = input ('id: ')

sql = "DELETE BOARD WHERE ID = :i"

sql_param = {
    'i' : b
}

cursor.execute(sql, sql_param)
conn.commit()
conn.close()