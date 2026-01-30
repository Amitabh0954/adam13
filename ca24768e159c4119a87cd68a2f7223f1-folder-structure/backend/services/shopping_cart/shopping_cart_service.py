# Epic Title: Shopping Cart Functionality
import mysql.connector
from typing import Dict

class ShoppingCartService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_product_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        if quantity <= 0:
            return {"error": "Quantity must be greater than zero"}

        query = "INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + %s"
        self.cursor.execute(query, (user_id, product_id, quantity, quantity))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            return {"error": "Failed to add product to cart"}
        return {"message": "Product added to cart successfully"}

    def get_cart(self, user_id: int) -> Dict[str, list]:
        query = """
        SELECT p.id as product_id, p.name, p.price, sc.quantity
        FROM shopping_cart sc
        JOIN products p ON sc.product_id = p.id
        WHERE sc.user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        cart_items = self.cursor.fetchall()
        return {"cart_items": cart_items}