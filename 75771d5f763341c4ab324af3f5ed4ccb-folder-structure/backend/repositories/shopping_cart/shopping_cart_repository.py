# Epic Title: Add Product to Shopping Cart

import sqlite3

class ShoppingCartRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS shopping_cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                session_id TEXT,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )""")

    def add_product(self, user_id: int, product_id: int, quantity: int, session_id: str = None) -> int:
        with self.connection:
            cursor = self.connection.execute("""
            INSERT INTO shopping_cart (user_id, product_id, quantity, session_id)
            VALUES (?, ?, ?, ?)""",
            (user_id, product_id, quantity, session_id))
        return cursor.lastrowid