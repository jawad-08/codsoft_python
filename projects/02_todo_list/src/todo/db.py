import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "todo.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Pending'
        )
        """)
        conn.commit()
