# Epic Title: Product Catalog Management
import mysql.connector

class ProductDeleteService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def delete_product(self, product_id: int, is_admin: bool, confirmation: bool) -> dict:
        if not is_admin:
            return {"error": "Only admins can delete products"}
        if not confirmation:
            return {"error": "Deletion requires confirmation"}

        query = "DELETE FROM products WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            return {"error": "Product not found or already deleted"}

        return {"message": "Product deleted successfully"}