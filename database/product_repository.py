from database import create_connection


def save_product(title, price, website):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products(title,price,website) VALUES(?,?,?)",
        (title, price, website)
    )

    conn.commit()

    conn.close()


def get_products():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    data = cursor.fetchall()

    conn.close()

    return data
