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
        self.cursor = self.connection.cursor()

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> int:
        query = "INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)"
        self.cursor.execute(query, (user_id, product_id, quantity))
        self.connection.commit()
        return self.cursor.lastrowid