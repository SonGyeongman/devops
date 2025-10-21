import mariadb

# mariadb 서버에 연결
conn = mariadb.connect(
    user='root',
    host='localhost',
    password='son76031991!',
    database='exampledb'
)

# conn.set_charset('utf8mb4')

# 커서 생성
cur = conn.cursor(dictionary=True)

# 명령어 실행
cur.execute("SELECT DATABASE()")
# 한번 호출에 하나의 Row를 가져올때 사용
print(cur.fetchone())
# print(cur.fetchall())
# print(cur.fetchmany(2))

# 연결 해제
conn.close()