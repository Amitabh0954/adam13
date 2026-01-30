# Epic Title: Product Catalog Management
import mysql.connector

class ProductRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_product_by_name(self, name: str) -> dict:
        query = "SELECT * FROM products WHERE name = %s"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()

    def create_product(self, name: str, description: str, price: float, category: str):
        query = "INSERT INTO products (name, description, price, category) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, description, price, category))
        self.connection.commit()