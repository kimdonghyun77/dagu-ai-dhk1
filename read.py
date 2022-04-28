import sqlite3
# connect = sqlite3.connecimport sqlite3
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect;
cursor = connect.cursor()

sql = ' select id,title,body from topics'

#title = input('제목을 알려주세요: ')
#body = input('본문을 알려주세요: ')
#sql = 'insert into topics (title, body) values(?,?)'

cursor.execute(sql)
row = cursor.fetchall()
print(rows)

#row = cursor.fetchone()
# sql = 'insert into topics (title, body) values("'+title+'","'+body+'")'sql인젝션문제 
#connect.commit()
#cursor.close()
#connect.close()

# print(title, body)  
#import sqlite3
# connect = sqlite3.connect('data.db')
# with cursor = connect.cursor()

#title = input('제목을 알려주세요: ')
#body = input('본문을 알려주세요: ')
#sql = 'insert into topics (title, body) values(?,?)'
#cursor.execute(sql, (title, body))

# sql = 'insert into topics (title, body) values("'+title+'","'+body+'")'sql인젝션문제 

#cursor.execute(sql)

#connect.commit()
#cursor.close()
#connect.close()

# print(title, body)  
# import sqlite3
# connect = sqlite3.connect('data.db')
#with cursor = connect.cursor()

#title = input('제목을 알려주세요: ')
#body = input('본문을 알려주세요: ')
#sql = 'insert into topics (title, body) values(?,?)'
#cursor.execute(sql, (title, body))

# sql = 'insert into topics (title, body) values("'+title+'","'+body+'")'sql인젝션문제 

#cursor.execute(sql)

#connect.commit()
#cursor.close()
#connect.close()

# print(title, body)