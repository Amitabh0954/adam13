# Epic Title: Product Catalog Management
import mysql.connector

class CategoryRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_catalog_db"
        )
        self.cursor = self.connection.cursor()

    def create_category(self, name: str, parent_id: int = None) -> int:
        query = "INSERT INTO categories (name, parent_id) VALUES (%s, %s)"
        self.cursor.execute(query, (name, parent_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def assign_category(self, product_id: int, category_id: int) -> bool:
        query = "INSERT INTO product_categories (product_id, category_id) VALUES (%s, %s)"
        self.cursor.execute(query, (product_id, category_id))
        self.connection.commit()
        return self.cursor.rowcount > 0