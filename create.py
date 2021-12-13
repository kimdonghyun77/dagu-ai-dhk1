import sqlite3
connect = sqlite3.connect('data.db')
cursor = connect.cursor()

title = input('제목을 알려주세요: ')
body = input('본문을 알려주세요: ')

print(title, body)

cursor.close()
connect.close()