# Epic Title: Product Catalog Management
import mysql.connector
from backend.models.product_catalog.product import Product

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
        self.cursor.execute("SELECT * FROM products WHERE name = %s", (name,))
        return self.cursor.fetchone()

    def add_product(self, product: Product) -> bool:
        query = """
        INSERT INTO products (name, description, price, category_id) VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (product.name, product.description, product.price, product.category_id))
        self.connection.commit()
        return self.cursor.rowcount > 0