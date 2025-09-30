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
conn.close()


def add_device(name: str, temp: int, humidity: int):
    cursor.execute('''
    INSERT INTO devices (name, temp, humidity)
    VALUES (?, ?, ?)
    ''', (name, temp, humidity))
    return f"Add name: {name}, temp: {temp}, humidity: {humidity}"

def get_data(id):
    cursor.execute('SELECT * FROM devices WHERE id = ?', (1,))
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

def update_temp(id: int, temp: int,):
    cursor.execute('''
        UPDATE devices 
        SET temp = ? 
        WHERE id = ?
    ''', (temp, id))
    conn.commit()
    conn.close()
    
    return f"Update temp id:{id}"

def update_humidity(id: int, humidity: int,):
    cursor.execute('''
        UPDATE devices 
        SET humidity = ? 
        WHERE id = ?
    ''', (humidity, id))
    conn.commit()
    conn.close()
    
    return f"Update humidity id:{id}"


