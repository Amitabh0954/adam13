# Epic Title: Search Products

import sqlite3

class ProductRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                description TEXT NOT NULL,
                is_deleted BOOLEAN NOT NULL DEFAULT 0
            )""")

    def search_products(self, query: str, limit: int, offset: int) -> list:
        query = f"%{query}%"
        cursor = self.connection.execute("""
        SELECT id, name, price, description FROM products
        WHERE (name LIKE ? OR description LIKE ?) AND is_deleted = 0
        LIMIT ? OFFSET ?""",
        (query, query, limit, offset))
        return [{'id': row[0], 'name': row[1], 'price': row[2], 'description': row[3]} for row in cursor.fetchall()]

    def count_products(self, query: str) -> int:
        query = f"%{query}%"
        cursor = self.connection.execute("""
        SELECT COUNT(*) FROM products
        WHERE (name LIKE ? OR description LIKE ?) AND is_deleted = 0""",
        (query, query))
        return cursor.fetchone()[0]