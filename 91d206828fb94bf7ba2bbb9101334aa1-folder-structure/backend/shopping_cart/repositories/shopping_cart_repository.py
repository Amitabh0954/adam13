# Epic Title: Shopping Cart Functionality
import mysql.connector

class ShoppingCartRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_catalog_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_cart_item(self, user_id: int, product_id: int) -> dict:
        query = "SELECT * FROM shopping_cart WHERE user_id = %s AND product_id = %s"
        self.cursor.execute(query, (user_id, product_id))
        return self.cursor.fetchone()

    def add_cart_item(self, user_id: int, product_id: int, quantity: int) -> int:
        query = "INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (user_id, product_id, quantity))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_cart_item(self, user_id: int, product_id: int, quantity: int) -> bool:
        query = "UPDATE shopping_cart SET quantity = %s WHERE user_id = %s AND product_id = %s"
        self.cursor.execute(query, (quantity, user_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0