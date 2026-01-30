# Epic Title: Product Catalog Management
import mysql.connector
from typing import List, Dict

class ProductSearchService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def search_products(self, query: str, page: int = 1, limit: int = 10) -> Dict[str, List[Dict]]:
        offset = (page - 1) * limit
        search_query = f"%{query}%"
        
        sql_query = """
        SELECT id, name, price, description FROM products
        WHERE name LIKE %s OR description LIKE %s
        LIMIT %s OFFSET %s
        """
        self.cursor.execute(sql_query, (search_query, search_query, limit, offset))
        results = self.cursor.fetchall()

        highlighted_results = self.highlight_search_terms(results, query)
        return {"products": highlighted_results, "page": page, "limit": limit}

    def highlight_search_terms(self, results: List[Dict], search_term: str) -> List[Dict]:
        highlighted_results = []
        for result in results:
            result['name'] = result['name'].replace(search_term, f"<strong>{search_term}</strong>")
            result['description'] = result['description'].replace(search_term, f"<strong>{search_term}</strong>")
            highlighted_results.append(result)
        return highlighted_results