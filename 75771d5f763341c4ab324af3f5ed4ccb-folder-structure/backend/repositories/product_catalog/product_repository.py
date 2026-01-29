# Epic Title: Update Product Details

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
                description TEXT NOT NULL
            )""")

    def update_product(self, product_id: int, updated_data: dict):
        with self.connection:
            self.connection.execute("""
            UPDATE products SET name = ?, price = ?, description = ? WHERE id = ?""",
            (updated_data['name'], updated_data['price'], updated_data['description'], product_id))