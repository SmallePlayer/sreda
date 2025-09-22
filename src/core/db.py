import sqlite3

conn = sqlite3.connect('enviroment.db')
cursor = conn.cursor()




def create_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        temp INTEGER,
        humidity INTEGER
    )
''')
conn.commit()


def add_device(name: str, temp: int, humidity: int):
    cursor.execute('''
    INSERT INTO users (name, temp, humidity)
    VALUES (?, ?, ?)
    ''', (name, temp, humidity))




