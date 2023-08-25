import sqlite3

conn = sqlite3.connect("model\database.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        Create table tersornpat(
            name varChar(100),
            email varChar(100)
        )
    ''')
    conn.commit()

def insert_data(username, email):
    cursor.execute('''
        INSERT INTO users (username, email)
        VALUES (?, ?)
    ''', (username, email))
    conn.commit()

def get_all_data():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def close_connection():
    conn.close()
