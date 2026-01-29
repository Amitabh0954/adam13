# Epic Title: Product Categorization

import sqlite3

class CategoryRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                parent_id INTEGER,
                FOREIGN KEY (parent_id) REFERENCES categories (id)
            )""")

    def save_category(self, category_data: dict) -> int:
        with self.connection:
            cursor = self.connection.execute("""
            INSERT INTO categories (name, parent_id)
            VALUES (?, ?)""",
            (category_data['name'], category_data.get('parent_id')))
        return cursor.lastrowid

    def update_category(self, category_id: int, updated_data: dict):
        with self.connection:
            self.connection.execute("""
            UPDATE categories SET name = ?, parent_id = ? WHERE id = ?""",
            (updated_data['name'], updated_data.get('parent_id'), category_id))