import sqlite3
connect = sqlite3.connect('data.db')
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE topics (
        id        INTEGER      PRIMARY KEY AUTOINCREMENT,
        title     VARCHAR (50) NOT NULL,
        body      TEXT
    )
''')
cursor.close()
connect.close()

<!-- print(title, body) 최초commit-->