import os
from homework_17.db.db_manager import DBManagerSQLite

#shop_db_path = os.path.abspath('../db/shop.db')


def show_all_products():
    with DBManagerSQLite() as db_cursor:
        return print(db_cursor.execute('''SELECT * FROM products''').fetchall())


def show_product_more_than_025_price():
    with DBManagerSQLite() as db_cursor:
        return print(db_cursor.execute('''SELECT * FROM products WHERE price > 0.25''').fetchall())


def update_banana_price():
    with DBManagerSQLite() as db_cursor:
        return db_cursor.execute('''UPDATE products SET price = 0.25 WHERE name = "banana"''').connection.commit()


def remove_apple_from_products():
    with DBManagerSQLite() as db_cursor:
        return db_cursor.execute('''DELETE FROM products WHERE name = "apple"''').connection.commit()


if __name__ == '__main__':
    show_all_products()
    show_product_more_than_025_price()
    update_banana_price()
    remove_apple_from_products()
