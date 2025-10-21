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
cur = conn.cursor()

# 명령어 실행
sql = "SELECT * FROM employees"
cur.execute(sql)
# 한번 호출에 하나의 Row를 가져올때 사용
employees = cur.fetchall()
for employee in employees:
    print(employee)

# 연결 해제
conn.close()