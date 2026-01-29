# Epic Title: Remove Product from Shopping Cart

import sqlite3

class ShoppingCartRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')

    def remove_product(self, user_id: int, product_id: int):
        with self.connection:
            self.connection.execute("""
            DELETE FROM shopping_cart WHERE user_id = ? AND product_id = ?""",
            (user_id, product_id))