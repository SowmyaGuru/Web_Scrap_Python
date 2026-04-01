import sqlite3

DB_NAME = "inventory.db"

def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price REAL,
        status TEXT,
        image_url TEXT,
        product_url TEXT
    )
    """)

    connection.commit()
    connection.close()


def insert_product(name, price, status, image_url, product_url):
    connection = connect()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """INSERT INTO products 
            (name, price, status, image_url, product_url) 
            VALUES (?, ?, ?, ?, ?)""",
            (name, price, status, image_url, product_url)
        )
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Duplicate skipped: {name}")
    finally:
        connection.close()