# Epic Title: Product Catalog Management

from typing import Optional, Dict, List
import mysql.connector
from mysql.connector import connection

class CategoryRepository:
    def __init__(self, db_connection: connection.MySQLConnection):
        self.db_connection = db_connection

    def add_category(self, name: str, parent_id: Optional[int] = None) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO categories (name, parent_id) VALUES (%s, %s)
        """
        cursor.execute(query, (name, parent_id))
        self.db_connection.commit()

    def update_category(self, category_id: int, name: str, parent_id: Optional[int] = None) -> None:
        cursor = self.db_connection.cursor()
        query = """
        UPDATE categories SET name = %s, parent_id = %s WHERE id = %s
        """
        cursor.execute(query, (name, parent_id, category_id))
        self.db_connection.commit()
    
    def delete_category(self, category_id: int) -> None:
        cursor = self.db_connection.cursor()
        query = """
        DELETE FROM categories WHERE id = %s
        """
        cursor.execute(query, (category_id,))
        self.db_connection.commit()

    def find_all_categories(self) -> List[Dict[str, str]]:
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT * FROM categories
        """
        cursor.execute(query)
        categories = cursor.fetchall()
        self.db_connection.commit()
        return categories