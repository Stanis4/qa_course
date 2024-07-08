import sqlite3
import os

shop_db_path = os.path.abspath('../db/shop.db')


def create_shop_db():
    connection = sqlite3.connect(shop_db_path)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL)''')

    connection.commit()

    data = [('orange', '0.5', '100'),
            ('apple', '0.3', '200'),
            ('banana', '0.2', '150')]

    for item in data:
        cursor.execute('''INSERT INTO products (name, price, quantity) VALUES (? , ?, ?)''', item)
        connection.commit()

    cursor.connection.commit()
    connection.close()


create_shop_db()
