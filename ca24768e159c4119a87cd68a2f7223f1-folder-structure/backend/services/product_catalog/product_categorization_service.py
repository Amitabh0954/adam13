# Epic Title: Product Catalog Management
import mysql.connector
from typing import List, Dict

class ProductCategorizationService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_category(self, name: str, parent_id: int = None) -> dict:
        if not name:
            return {"error": "Category name cannot be empty"}

        query = "INSERT INTO categories (name, parent_id) VALUES (%s, %s)"
        self.cursor.execute(query, (name, parent_id))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            return {"error": "Failed to add category"}
        return {"message": "Category added successfully"}

    def assign_category_to_product(self, product_id: int, category_id: int) -> dict:
        query = "INSERT INTO product_categories (product_id, category_id) VALUES (%s, %s)"
        self.cursor.execute(query, (product_id, category_id))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            return {"error": "Failed to assign category to product"}
        return {"message": "Category assigned to product successfully"}

    def get_categories(self) -> List[Dict]:
        self.cursor.execute("SELECT id, name, parent_id FROM categories")
        categories = self.cursor.fetchall()
        return categories