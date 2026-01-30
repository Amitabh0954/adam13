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
        query_temp = "DELETE FROM saved_cart_items WHERE user_id = %s"
        self.cursor.execute(query_temp, (user_id,))
        query = """
            INSERT INTO saved_cart_items (user_id, product_id, quantity)
            SELECT user_id, product_id, quantity FROM cart_items WHERE user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def retrieve_cart(self, user_id: int) -> list:
        query = """
            SELECT product_id, quantity FROM saved_cart_items WHERE user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()