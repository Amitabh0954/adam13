# Epic Title: Shopping Cart Functionality
import mysql.connector

class ShoppingCartRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="shopping_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_cart_by_user_id(self, user_id: int) -> dict:
        query = "SELECT * FROM shopping_carts WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def create_cart(self, user_id: int = None) -> int:
        query = "INSERT INTO shopping_carts (user_id) VALUES (%s)"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_cart_items(self, cart_id: int) -> list:
        query = "SELECT * FROM cart_items WHERE cart_id = %s"
        self.cursor.execute(query, (cart_id,))
        return self.cursor.fetchall()

    def add_cart_item(self, cart_id: int, product_id: int, quantity: int) -> bool:
        query = "INSERT INTO cart_items (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (cart_id, product_id, quantity))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def update_cart_item(self, cart_id: int, product_id: int, quantity: int) -> bool:
        query = "UPDATE cart_items SET quantity = %s WHERE cart_id = %s AND product_id = %s"
        self.cursor.execute(query, (quantity, cart_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete_cart_item(self, cart_id: int, product_id: int) -> bool:
        query = "DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s"
        self.cursor.execute(query, (cart_id, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def save_cart_state(self, user_id: int, cart_items: list) -> bool:
        cart = self.get_cart_by_user_id(user_id)
        if cart:
            cart_id = cart['id']
        else:
            cart_id = self.create_cart(user_id)

        for item in cart_items:
            self.add_cart_item(cart_id, item['product_id'], item['quantity'])
        return True

    def retrieve_cart_state(self, user_id: int) -> list:
        cart = self.get_cart_by_user_id(user_id)
        if not cart:
            return []

        cart_id = cart['id']
        return self.get_cart_items(cart_id)