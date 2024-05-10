import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Persons (
id INTEGER PRIMARY KEY,
name TEXT,
date1 TEXT,
date2 TEXT,
profession TEXT,
country TEXT,
photo TEXT,
wiki TEXT
)
''')


connection.commit()
connection.close()