# Epic Title: Product Catalog Management
import mysql.connector
from backend.models.product_catalog.category import Category

class CategoryRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_category_by_name(self, name: str) -> dict:
        self.cursor.execute("SELECT * FROM categories WHERE name = %s", (name,))
        return self.cursor.fetchone()

    def add_category(self, category: Category) -> bool:
        query = """
        INSERT INTO categories (name, description, parent_id) VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (category.name, category.description, category.parent_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_all_categories(self) -> list:
        self.cursor.execute("SELECT * FROM categories")
        return self.cursor.fetchall()