import sqlite3
sqlite3.connect('data.db')
import sqlite3
con1 = sqlite3.connect('data.db')
cursor = con1.cursor()
cursor.execute('''
    CREATE TABLE topics (
        id        INTEGER      PRIMARY KEY AUTOINCREMENT,
        title     VARCHAR (50) NOT NULL,
        body      TEXT
    )
''')
