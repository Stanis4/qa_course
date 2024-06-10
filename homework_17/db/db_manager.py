import os
import sqlite3
import typing

from pathlib import PosixPath

shop_db_path = os.path.abspath('../db/shop.db')


class DBManagerSQLite:

    def __init__(self, path_to_db: typing.Union[str, PosixPath] = shop_db_path):
        self.path_to_lib = path_to_db

    def __enter__(self):
        self.connection = sqlite3.connect(self.path_to_lib)
        self.cursor = self.connection.cursor()
        print('db connection was created')
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print('db connection was closed')
