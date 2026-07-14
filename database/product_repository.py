from database import create_connection

def save_product(name, price, website):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS products (name TEXT, price REAL, website TEXT)"
    )

    cursor.execute(
        "INSERT INTO products VALUES (?, ?, ?)",
        (name, price, website)
    )

    conn.commit()
    conn.close()
