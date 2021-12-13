import sqlite3
# connect = sqlite3.connec
with cursor = connect.curs

title = input('제목을 알려
body = input('본문을 알려
sql = 'insert into topics 
cursor.execute(sql, (title

# sql = 'insert into topic

cursor.execute(sql)

connect.commit()
cursor.close()
connect.close()

# print(title, body)  