# Epic Title: Product Catalog Management
import mysql.connector

class ProductRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_catalog_db"
        )
        self.cursor = self.connection.cursor()

    def is_name_taken(self, name: str) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE name = %s"
        self.cursor.execute(query, (name,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def create_product(self, name: str, price: float, description: str) -> int:
        query = "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, price, description))
        self.connection.commit()
        return self.cursor.lastrowid