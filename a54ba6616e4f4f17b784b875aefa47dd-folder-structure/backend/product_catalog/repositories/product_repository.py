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

    def product_name_exists_with_different_id(self, product_id: int, name: str) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE name = %s AND id != %s"
        self.cursor.execute(query, (name, product_id))
        result = self.cursor.fetchone()
        return result[0] > 0

    def update_product(self, product_id: int, name: str, price: float, description: str) -> bool:
        fields_to_update = []
        params = []

        if name:
            fields_to_update.append("name = %s")
            params.append(name)

        if price is not None:
            fields_to_update.append("price = %s")
            params.append(price)

        if description:
            fields_to_update.append("description = %s")
            params.append(description)
        
        params.append(product_id)
        
        query = f"UPDATE products SET {', '.join(fields_to_update)} WHERE id = %s"
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.rowcount > 0