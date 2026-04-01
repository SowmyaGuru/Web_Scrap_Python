import sqlite3

def check_products():

     connection = sqlite3.connect("inventory.db")
     cursor = connection.cursor()

     cursor.execute("SELECT * from products")
     rows = cursor.fetchall()

     if rows:
        print("Products found:\n")
     for row in rows:
        print(row)
     else:
        print("No data found in products table.")
     connection.close()