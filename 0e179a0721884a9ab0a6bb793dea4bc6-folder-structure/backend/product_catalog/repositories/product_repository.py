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
        self.cursor = self.connection.cursor()

    def delete_product(self, product_id: int) -> bool:
        query = "DELETE FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0