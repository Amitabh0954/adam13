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
        self.cursor = self.connection.cursor(dictionary=True)

    def exists_by_id(self, category_id: int) -> bool:
        query = "SELECT COUNT(*) as count FROM categories WHERE id = %s"
        self.cursor.execute(query, (category_id,))
        result = self.cursor.fetchone()
        return result['count'] > 0

    def exists_by_name(self, name: str) -> bool:
        query = "SELECT COUNT(*) as count FROM categories WHERE name = %s"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchone()
        return result['count'] > 0

    def create_category(self, name: str, parent_id: int = None) -> int:
        query = "INSERT INTO categories (name, parent_id) VALUES (%s, %s)"
        self.cursor.execute(query, (name, parent_id))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_all_categories(self) -> list:
        query = "SELECT * FROM categories ORDER BY name"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_category(self, category_id: int) -> bool:
        query = "DELETE FROM categories WHERE id = %s"
        self.cursor.execute(query, (category_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0