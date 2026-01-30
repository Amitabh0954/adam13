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

    def save_cart_state(self, user_id: int) -> bool:
        query = """
        INSERT INTO saved_shopping_cart (user_id, product_id, quantity)
        SELECT user_id, product_id, quantity FROM shopping_cart WHERE user_id = %s
        ON DUPLICATE KEY UPDATE quantity = VALUES(quantity)
        """
        try:
            self.cursor.execute(query, (user_id,))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False