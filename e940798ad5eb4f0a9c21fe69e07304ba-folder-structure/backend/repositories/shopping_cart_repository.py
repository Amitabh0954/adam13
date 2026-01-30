# Epic Title: Shopping Cart Functionality
import mysql.connector
from backend.models.shopping_cart.cart_item import CartItem

class ShoppingCartRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopping_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_to_cart(self, cart_item: CartItem) -> bool:
        query = """
        INSERT INTO shopping_cart (user_id, product_id, quantity) VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)
        """
        self.cursor.execute(query, (cart_item.user_id, cart_item.product_id, cart_item.quantity))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_cart(self, user_id: int) -> list:
        self.cursor.execute("SELECT * FROM shopping_cart WHERE user_id = %s", (user_id,))
        return self.cursor.fetchall()

    def clear_cart(self, user_id: int) -> bool:
        self.cursor.execute("DELETE FROM shopping_cart WHERE user_id = %s", (user_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def remove_from_cart(self, user_id: int, product_id: int) -> bool:
        self.cursor.execute("DELETE FROM shopping_cart WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def update_quantity(self, user_id: int, product_id: int, quantity: int) -> bool:
        query = """
        UPDATE shopping_cart SET quantity = %s WHERE user_id = %s AND product_id = %s
        """
        self.cursor.execute(query, (quantity, user_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def save_cart(self, user_id: int):
        self.cursor.execute("SELECT * FROM shopping_cart WHERE user_id = %s", (user_id,))
        cart_items = self.cursor.fetchall()
        query = """
        INSERT INTO saved_carts (user_id, cart_state)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE cart_state = VALUES(cart_state)
        """
        import json
        cart_state = json.dumps(cart_items)
        self.cursor.execute(query, (user_id, cart_state))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def retrieve_saved_cart(self, user_id: int):
        self.cursor.execute("SELECT cart_state FROM saved_carts WHERE user_id = %s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            import json
            return json.loads(result['cart_state'])
        return []