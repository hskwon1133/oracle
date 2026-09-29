#import / connection
import oracledb as db

DB_USER = 'C##KH'
DB_PASSWORD = '1234'
DB_DSN = 'localhost:1521/xe'

conn = db.connect(user = DB_USER, password = DB_PASSWORD, dsn = DB_DSN)

cursor = conn.cursor()
sql = 'SELECT * FROM BOARD'

cursor.execute(sql)

result = cursor.fetchall() #결과집합
print(result)

cursor.close()
conn.close()