# Epic Title: Product Catalog Management

from typing import Optional, Dict
import mysql.connector
from mysql.connector import connection

class ProductRepository:
    def __init__(self, db_connection: connection.MySQLConnection):
        self.db_connection = db_connection

    def add_product(self, name: str, price: float, description: str, category: str) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO products (name, price, description, category) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, price, description, category))
        self.db_connection.commit()

    def find_product_by_name(self, name: str) -> Optional[Dict[str, str]]:
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT * FROM products WHERE name = %s
        """
        cursor.execute(query, (name,))
        product = cursor.fetchone()
        self.db_connection.commit()
        return product

    def update_product(self, product_id: int, price: Optional[float] = None, description: Optional[str] = None, category: Optional[str] = None) -> None:
        cursor = self.db_connection.cursor()
        updates = []
        values = []
        if price is not None:
            updates.append("price = %s")
            values.append(price)
        if description is not None:
            updates.append("description = %s")
            values.append(description)
        if category is not None:
            updates.append("category = %s")
            values.append(category)
        if updates:
            query = f"UPDATE products SET {', '.join(updates)} WHERE id = %s"
            values.append(product_id)
            cursor.execute(query, values)
            self.db_connection.commit()