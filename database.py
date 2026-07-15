import sqlite3


DATABASE_NAME = "products.db"


def create_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        website TEXT
    )
    """)

    conn.commit()
    conn.close()
