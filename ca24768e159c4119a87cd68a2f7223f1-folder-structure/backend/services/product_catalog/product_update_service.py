# Epic Title: Product Catalog Management
import mysql.connector

class ProductUpdateService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def update_product(self, product_id: int, name: str, price: float, description: str, is_admin: bool) -> dict:
        if not is_admin:
            return {"error": "Only admins can update product details"}
        if price <= 0:
            return {"error": "Product price must be a numeric value greater than 0"}
        if not description:
            return {"error": "Product description cannot be empty"}

        query = "UPDATE products SET name = %s, price = %s, description = %s WHERE id = %s"
        self.cursor.execute(query, (name, price, description, product_id))
        self.connection.commit()

        if self.cursor.rowcount == 0:
            return {"error": "No changes made or product not found"}
        return {"message": "Product updated successfully"}