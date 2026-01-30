# Epic Title: Product Catalog Management
import mysql.connector

class CategoryRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_categories(self) -> list:
        query = "SELECT * FROM categories"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_category(self, name: str, parent_id: int = None):
        query = "INSERT INTO categories (name, parent_id) VALUES (%s, %s)"
        self.cursor.execute(query, (name, parent_id))
        self.connection.commit()

    def update_category(self, category_id: int, name: str, parent_id: int = None) -> bool:
        query = "UPDATE categories SET name = %s, parent_id = %s WHERE id = %s"
        self.cursor.execute(query, (name, parent_id, category_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete_category(self, category_id: int) -> bool:
        query = "DELETE FROM categories WHERE id = %s"
        self.cursor.execute(query, (category_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0