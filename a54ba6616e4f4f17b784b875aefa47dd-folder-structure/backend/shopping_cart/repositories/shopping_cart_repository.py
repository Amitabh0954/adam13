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

    def modify_quantity(self, user_id: int, product_id: int, quantity: int) -> bool:
        query = "UPDATE shopping_cart SET quantity = %s WHERE user_id = %s AND product_id = %s"
        self.cursor.execute(query, (quantity, user_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0