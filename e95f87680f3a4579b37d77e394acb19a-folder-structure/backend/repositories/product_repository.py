# Epic Title: Product Catalog Management
import mysql.connector

class ProductRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_product_by_id(self, product_id: int) -> dict:
        query = "SELECT * FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def get_product_by_name(self, name: str) -> dict:
        query = "SELECT * FROM products WHERE name = %s"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()

    def create_product(self, name: str, description: str, price: float, category_id: int):
        query = "INSERT INTO products (name, description, price, category_id) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, description, price, category_id))
        self.connection.commit()

    def update_product(self, product_id: int, data: dict) -> bool:
        columns = ", ".join(f"{key} = %s" for key in data.keys())
        sql = f"UPDATE products SET {columns} WHERE id = %s"
        params = list(data.values()) + [product_id]
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete_product(self, product_id: int) -> bool:
        query = "DELETE FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def search_products(self, query: str, offset: int, limit: int) -> list:
        sql_query = """
            SELECT *, MATCH(name, description) AGAINST (%s IN NATURAL LANGUAGE MODE) AS relevance 
            FROM products 
            WHERE MATCH(name, description) AGAINST (%s IN NATURAL LANGUAGE MODE) 
            ORDER BY relevance DESC 
            LIMIT %s OFFSET %s
        """
        self.cursor.execute(sql_query, (query, query, limit, offset))
        return self.cursor.fetchall()