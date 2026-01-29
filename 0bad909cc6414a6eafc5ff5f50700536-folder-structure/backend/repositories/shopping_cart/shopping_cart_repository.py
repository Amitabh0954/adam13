# Epic Title: Shopping Cart Functionality

from typing import Dict, List, Optional
import mysql.connector
from mysql.connector import connection

class ShoppingCartRepository:
    def __init__(self, db_connection: connection.MySQLConnection):
        self.db_connection = db_connection

    def create_cart(self, user_id: Optional[int] = None) -> int:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO shopping_carts (user_id) VALUES (%s)
        """
        cursor.execute(query, (user_id,))
        self.db_connection.commit()
        return cursor.lastrowid

    def add_product_to_cart(self, cart_id: int, product_id: int, quantity: int) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO cart_items (cart_id, product_id, quantity) VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
        """
        cursor.execute(query, (cart_id, product_id, quantity))
        self.db_connection.commit()

    def get_cart_items(self, cart_id: int) -> List[Dict[str, int]]:
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT product_id, quantity FROM cart_items WHERE cart_id = %s
        """
        cursor.execute(query, (cart_id,))
        items = cursor.fetchall()
        self.db_connection.commit()
        return items

    def remove_product_from_cart(self, cart_id: int, product_id: int) -> None:
        cursor = self.db_connection.cursor()
        query = """
        DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s
        """
        cursor.execute(query, (cart_id, product_id))
        self.db_connection.commit()

    def update_product_quantity(self, cart_id: int, product_id: int, quantity: int) -> None:
        cursor = self.db_connection.cursor()
        query = """
        UPDATE cart_items SET quantity = %s WHERE cart_id = %s AND product_id = %s
        """
        cursor.execute(query, (quantity, cart_id, product_id))
        self.db_connection.commit()