# Epic Title: Shopping Cart Functionality
import mysql.connector
from backend.models.shopping_cart.cart_item.py import CartItem

class ShoppingCartRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopping_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_to_cart(self, cart_item: CartItem) -> bool:
        query = """
        INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
        """
        self.cursor.execute(query, (cart_item.user_id, cart_item.product_id, cart_item.quantity))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_cart(self, user_id: int) -> list:
        self.cursor.execute("SELECT * FROM shopping_cart WHERE user_id = %s", (user_id,))
        return self.cursor.fetchall()

    def clear_cart(self, user_id: int) -> bool:
        self.cursor.execute("DELETE FROM shopping_cart WHERE user_id = %s", (user_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0