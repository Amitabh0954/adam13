# Epic Title: Save Shopping Cart for Logged-in Users

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

    def save_cart(self, user_id: int, cart_items: list):
        with self.connection:
            self.connection.execute("DELETE FROM shopping_cart WHERE user_id = ?", (user_id,))
            for item in cart_items:
                self.connection.execute("""
                INSERT INTO shopping_cart (user_id, product_id, quantity)
                VALUES (?, ?, ?)""",
                (user_id, item['product_id'], item['quantity']))

    def load_cart(self, user_id: int) -> list:
        cursor = self.connection.execute("""
        SELECT product_id, quantity FROM shopping_cart WHERE user_id = ?""", (user_id,))
        cart_items = [{'product_id': row[0], 'quantity': row[1]} for row in cursor.fetchall()]
        return cart_items