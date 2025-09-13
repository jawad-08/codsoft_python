import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "contacts.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            address TEXT
        )
        """)
        conn.commit()
