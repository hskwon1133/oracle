import oracledb as db

#db connection

DB_USER = 'C##KH'
DB_PASSWORD = '1234'
DB_DSN = '192.168.40.92:1521/xe'

conn = db.connect(user= DB_USER, password = DB_PASSWORD, dsn = DB_DSN)

print(conn.version)