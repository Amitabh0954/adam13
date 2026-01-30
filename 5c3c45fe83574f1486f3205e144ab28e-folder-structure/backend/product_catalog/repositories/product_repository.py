# Epic Title: Product Catalog Management
import mysql.connector
from typing import List, Dict

class ProductRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_catalog_db"
        )
        self.cursor = self.connection.cursor()

    def is_name_taken(self, name: str) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE name = %s"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def create_product(self, name: str, price: float, description: str) -> int:
        query = "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, price, description))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_product(self, product_id: int, name: str, price: float, description: str) -> bool:
        query = """
        UPDATE products SET name = %s, price = %s, description = %s WHERE id = %s
        """
        self.cursor.execute(query, (name, price, description, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def product_exists(self, product_id: int) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def delete_product_by_id(self, product_id: int) -> bool:
        query = "DELETE FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def search_products(self, query: str, page: int, page_size: int) -> List[Dict[str, any]]:
        offset = (page - 1) * page_size
        search_query = f"%{query}%"
        
        statement = """
        SELECT id, name, price, description FROM products
        WHERE name LIKE %s OR description LIKE %s
        LIMIT %s OFFSET %s
        """
        
        self.cursor.execute(statement, (search_query, search_query, page_size, offset))
        results = self.cursor.fetchall()
        
        products = []
        for result in results:
            products.append({
                "id": result[0],
                "name": result[1],
                "price": result[2],
                "description": result[3]
            })
        
        return products

    def count_search_results(self, query: str) -> int:
        search_query = f"%{query}%"
        statement = "SELECT COUNT(*) FROM products WHERE name LIKE %s OR description LIKE %s"
        
        self.cursor.execute(statement, (search_query, search_query))
        result = self.cursor.fetchone()
        
        return result[0]