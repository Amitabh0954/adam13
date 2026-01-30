# Epic Title: Shopping Cart Functionality
import mysql.connector

class ShoppingCartRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopping_cart_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def is_product_available(self, product_id: int) -> bool:
        query = "SELECT COUNT(*) as count FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()["count"] > 0

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> int:
        query = """
            INSERT INTO cart_items (user_id, product_id, quantity)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE quantity = quantity + %s
        """
        self.cursor.execute(query, (user_id, product_id, quantity, quantity))
        self.connection.commit()
        return self.cursor.lastrowid