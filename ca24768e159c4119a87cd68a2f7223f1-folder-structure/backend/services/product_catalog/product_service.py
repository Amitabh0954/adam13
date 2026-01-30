# Epic Title: Product Catalog Management
import mysql.connector

class ProductService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def add_product(self, name: str, price: float, description: str) -> dict:
        if not name:
            return {"error": "Product name cannot be empty"}
        if price <= 0:
            return {"error": "Product price must be a positive number"}
        if not description:
            return {"error": "Product description cannot be empty"}

        self.cursor.execute("SELECT * FROM products WHERE name = %s", (name,))
        if self.cursor.fetchone():
            return {"error": "Product name already exists"}

        query = "INSERT INTO products (name, price, description) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, price, description))
        self.connection.commit()
        if self.cursor.rowcount == 0:
            return {"error": "Failed to add product"}
        return {"message": "Product added successfully"}