# Epic Title: Product Catalog Management
import mysql.connector

class ProductRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_catalog_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def search_products(self, search_term: str, page: int, page_size: int) -> tuple:
        offset = (page - 1) * page_size
        search_term = f"%{search_term}%"

        query = """
        SELECT * FROM products 
        WHERE name LIKE %s OR description LIKE %s OR category LIKE %s
        LIMIT %s OFFSET %s
        """
        self.cursor.execute(query, (search_term, search_term, search_term, page_size, offset))
        results = self.cursor.fetchall()

        count_query = """
        SELECT COUNT(*) AS total FROM products 
        WHERE name LIKE %s OR description LIKE %s OR category LIKE %s
        """
        self.cursor.execute(count_query, (search_term, search_term, search_term))
        total = self.cursor.fetchone()['total']

        return results, total