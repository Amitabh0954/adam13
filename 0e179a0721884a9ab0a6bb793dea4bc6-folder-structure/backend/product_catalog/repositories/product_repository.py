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

    def is_name_taken(self, name: str, exclude_id: int) -> bool:
        query = "SELECT COUNT(*) FROM products WHERE name = %s AND id != %s"
        self.cursor.execute(query, (name, exclude_id))
        count = self.cursor.fetchone()[0]
        return count > 0

    def update_product(self, product_id: int, name: str | None, price: float | None, description: str | None) -> bool:
        query = "UPDATE products SET "
        fields = []
        values = []

        if name is not None:
            fields.append("name = %s")
            values.append(name)
        if price is not None:
            fields.append("price = %s")
            values.append(price)
        if description is not None:
            fields.append("description = %s")
            values.append(description)

        query += ", ".join(fields) + " WHERE id = %s"
        values.append(product_id)

        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.rowcount > 0