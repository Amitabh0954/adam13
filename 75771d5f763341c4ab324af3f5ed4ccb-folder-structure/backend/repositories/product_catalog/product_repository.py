# Epic Title: Add New Product

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

    def save_product(self, product_data: dict) -> int:
        with self.connection:
            cursor = self.connection.execute("""
            INSERT INTO products (name, price, description)
            VALUES (?, ?, ?)""",
            (product_data['name'], product_data['price'], product_data['description']))
        return cursor.lastrowid