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

    def remove_product_from_cart(self, user_id: int, cart_item_id: int) -> bool:
        query = "DELETE FROM cart_items WHERE id = %s AND user_id = %s"
        self.cursor.execute(query, (cart_item_id, user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0