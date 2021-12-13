import sqlite3
# connect = sqlite3.connect('data.db')
with cursor = connect.cursor()

title = input('제목을 알려주세요: ')
body = input('본문을 알려주세요: ')
sql = 'insert into topics (title, body) values(?,?)'
cursor.execute(sql, (title, body))

# sql = 'insert into topics (title, body) values("'+title+'","'+body+'")'sql인젝션문제 

cursor.execute(sql)

connect.commit()
cursor.close()
connect.close()

# print(title, body)  