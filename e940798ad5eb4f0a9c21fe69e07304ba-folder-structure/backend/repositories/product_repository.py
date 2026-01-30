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

    # Existing methods for managing products

    def get_product_by_id(self, product_id: int) -> dict:
        self.cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        return self.cursor.fetchone()

    def delete_product(self, product_id: int) -> bool:
        self.cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

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

    def update_product(self, product: Product) -> bool:
        query = """
        UPDATE products SET name = %s, description = %s, price = %s, category_id = %s WHERE id = %s
        """
        self.cursor.execute(query, (product.name, product.description, product.price, product.category_id, product.id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    # New methods for searching products

    def search_products(self, query: str, offset: int, page_size: int) -> list:
        search_query = f"%{query}%"
        self.cursor.execute("""
        SELECT products.*, categories.name AS category_name
        FROM products
        INNER JOIN categories ON products.category_id = categories.id
        WHERE products.name LIKE %s OR products.description LIKE %s OR categories.name LIKE %s
        LIMIT %s OFFSET %s
        """, (search_query, search_query, search_query, page_size, offset))
        return self.cursor.fetchall()

    def count_search_results(self, query: str) -> int:
        search_query = f"%{query}%"
        self.cursor.execute("""
        SELECT COUNT(*)
        FROM products
        INNER JOIN categories ON products.category_id = categories.id
        WHERE products.name LIKE %s OR products.description LIKE %s OR categories.name LIKE %s
        """, (search_query, search_query, search_query))
        return self.cursor.fetchone()['COUNT(*)']