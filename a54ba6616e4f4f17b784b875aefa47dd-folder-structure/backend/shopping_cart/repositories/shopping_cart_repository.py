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

    def save_cart(self, user_id: int) -> bool:
        query = """
        INSERT INTO saved_carts (user_id, product_id, quantity)
        SELECT user_id, product_id, quantity FROM shopping_cart
        WHERE user_id = %s
        ON DUPLICATE KEY UPDATE quantity = VALUES(quantity)
        """
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def retrieve_cart(self, user_id: int) -> list:
        query = "SELECT product_id, quantity FROM saved_carts WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        cart_items = self.cursor.fetchall()
        return cart_items if cart_items else []