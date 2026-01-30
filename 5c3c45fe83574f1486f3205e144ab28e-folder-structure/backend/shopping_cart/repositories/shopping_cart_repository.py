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

    def product_exists(self, product_id: int) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def get_active_cart(self, user_id: int) -> int:
        query = "SELECT id FROM carts WHERE user_id = %s AND active = 1"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def create_cart(self, user_id: int) -> int:
        query = "INSERT INTO carts (user_id, active) VALUES (%s, 1)"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_product(self, cart_id: int, product_id: int, quantity: int) -> bool:
        query = """
        INSERT INTO cart_items (cart_id, product_id, quantity)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE quantity = quantity + %s
        """
        self.cursor.execute(query, (cart_id, product_id, quantity, quantity))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def product_in_cart(self, cart_id: int, product_id: int) -> bool:
        query = "SELECT COUNT(*) FROM cart_items WHERE cart_id = %s AND product_id = %s"
        self.cursor.execute(query, (cart_id, product_id))
        result = self.cursor.fetchone()
        return result[0] > 0

    def remove_product(self, cart_id: int, product_id: int) -> bool:
        query = "DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s"
        self.cursor.execute(query, (cart_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def update_product_quantity(self, cart_id: int, product_id: int, quantity: int) -> bool:
        query = "UPDATE cart_items SET quantity = %s WHERE cart_id = %s AND product_id = %s"
        self.cursor.execute(query, (quantity, cart_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def save_cart_state(self, user_id: int, cart_id: int) -> bool:
        query = "UPDATE carts SET active = 0 WHERE user_id = %s AND id = %s"
        self.cursor.execute(query, (user_id, cart_id))
        self.connection.commit()
        return self.cursor.rowcount > 0