import sqlite3

def create_db():
    conn = sqlite3.connect('device.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT UNIQUE,
                  content TEXT)''')
    conn.commit()
    conn.close()
    
def add_message(name, content):
    conn = sqlite3.connect('device.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO messages (name, content) VALUES (?, ?)", (name, content))
    conn.commit()
    conn.close()
    
def get_name(id):
    conn = sqlite3.connect('device.db')
    c = conn.cursor()
    c.execute("SELECT name FROM messages WHERE id=?", (id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def get_content(name):
    conn = sqlite3.connect('device.db')
    c = conn.cursor()
    c.execute("SELECT content FROM messages WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None