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

    def exists_in_cart(self, user_id: int, product_id: int) -> bool:
        query = "SELECT COUNT(*) as count FROM shopping_cart WHERE user_id = %s AND product_id = %s"
        self.cursor.execute(query, (user_id, product_id))
        result = self.cursor.fetchone()
        return result['count'] > 0

    def remove_cart_item(self, user_id: int, product_id: int) -> bool:
        query = "DELETE FROM shopping_cart WHERE user_id = %s AND product_id = %s"
        self.cursor.execute(query, (user_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0