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

    def fetch_all_categories(self) -> list:
        query = "SELECT id, name, parent_id FROM categories"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        categories = [{"id": row[0], "name": row[1], "parent_id": row[2]} for row in result]
        return categories

    def create_category(self, name: str, parent_id: int = None) -> int:
        query = "INSERT INTO categories (name, parent_id) VALUES (%s, %s)"
        self.cursor.execute(query, (name, parent_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_category(self, category_id: int, name: str, parent_id: int = None) -> bool:
        query = "UPDATE categories SET name = %s, parent_id = %s WHERE id = %s"
        self.cursor.execute(query, (name, parent_id, category_id))
        self.connection.commit()
        return self.cursor.rowcount > 0