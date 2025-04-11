

import sqlite3

def init_db():
    conn = sqlite3.connect("specimens.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            specimen_name TEXT,
            microscope_size REAL,
            magnification REAL,
            actual_size REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(username, specimen_name, microscope_size, magnification, actual_size):
    conn = sqlite3.connect("specimens.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO specimens (username, specimen_name, microscope_size, magnification, actual_size)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, specimen_name, microscope_size, magnification, actual_size))
    conn.commit()
    conn.close()

# Call this once when the program starts
init_db()
