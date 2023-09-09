import sqlite3

# ต่อ Database โดยใช้ SQLITE3
conn = sqlite3.connect("model\database.db", check_same_thread=False)
cursor = conn.cursor()

# คำสั่ง SQL สร้าง Table
def create_table():
    cursor.execute('''
            CREATE TABLE mvc (
                url VARCHAR(255),
                textdata VARCHAR(255),
                monic VARCHAR(255),
                oiber VARCHAR(255)
            );
    ''')
    conn.commit()

# คำสั่ง SQL Insert เข้า Table โดยรับ Parameter 4 ตัว
def insert_data(url, textdata, monic, oiber):
    cursor.execute('''
        INSERT INTO mvc ( url, textdata, monic, oiber)
        VALUES (?, ?, ?, ?)
    ''', (url, textdata, monic, oiber))
    conn.commit()

# นำค่าที่มีทั้งหมดใน Table มาแสดง
def get_all_data():
    cursor.execute('''
        SELECT * FROM mvc
    ''')
    return cursor.fetchall()

# ปิดการเชื่อมต่อของ Database
def close_connection():
    conn.close()
