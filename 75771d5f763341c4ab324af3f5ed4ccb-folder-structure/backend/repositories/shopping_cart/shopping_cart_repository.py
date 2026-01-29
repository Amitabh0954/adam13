# Epic Title: Modify Quantity of Products in Shopping Cart

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

    def update_quantity(self, user_id: int, product_id: int, quantity: int):
        with self.connection:
            self.connection.execute("""
            UPDATE shopping_cart SET quantity = ? WHERE user_id = ? AND product_id = ?""",
            (quantity, user_id, product_id))