# Epic Title: Delete Product

import sqlite3

class ProductRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                description TEXT NOT NULL,
                is_deleted BOOLEAN NOT NULL DEFAULT 0
            )""")

    def delete_product(self, product_id: int):
        with self.connection:
            self.connection.execute("""
            UPDATE products SET is_deleted = 1 WHERE id = ?""",
            (product_id,))