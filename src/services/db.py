import sqlite3
from typing import Optional

from src.config.settings import SQLITE_PATH


def create_db() -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT UNIQUE,
                  content TEXT)'''
    )
    conn.commit()
    conn.close()


def add_message(name: str, content: str) -> None:
    conn = sqlite3.connect(SQLITE_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT OR REPLACE INTO messages (name, content) VALUES (?, ?)",
        (name, content),
    )
    conn.commit()
    conn.close()


def get_name(row_id: int) -> Optional[str]:
    conn = sqlite3.connect(SQLITE_PATH)
    c = conn.cursor()
    c.execute("SELECT name FROM messages WHERE id=?", (row_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None


def get_content(name: str) -> Optional[str]:
    conn = sqlite3.connect(SQLITE_PATH)
    c = conn.cursor()
    c.execute("SELECT content FROM messages WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

