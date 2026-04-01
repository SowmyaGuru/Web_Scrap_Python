import sqlite3
import os

def check_products():
     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
     DB_PATH = os.path.join(BASE_DIR, "..", "inventory.db")

     connection = sqlite3.connect(DB_PATH)
     #connection = sqlite3.connect("inventory.db")
     cursor = connection.cursor()

     cursor.execute("SELECT * from products")
     rows = cursor.fetchall()

     if rows:
        print("Products found:\n")
     for row in rows:
        print(row)
     else:
        print("Successfully completed")
     connection.close()