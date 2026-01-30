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

    def search_products(self, query: str, page: int, per_page: int) -> list:
        offset = (page - 1) * per_page
        wild_query = f"%{query}%"
        search_query = """
            SELECT id, name, price, description 
            FROM products 
            WHERE name LIKE %s OR description LIKE %s 
            LIMIT %s OFFSET %s
        """
        self.cursor.execute(search_query, (wild_query, wild_query, per_page, offset))
        return self.cursor.fetchall()

    def count_search_results(self, query: str) -> int:
        wild_query = f"%{query}%"
        count_query = "SELECT COUNT(*) AS count FROM products WHERE name LIKE %s OR description LIKE %s"
        self.cursor.execute(count_query, (wild_query, wild_query))
        return self.cursor.fetchone()['count']