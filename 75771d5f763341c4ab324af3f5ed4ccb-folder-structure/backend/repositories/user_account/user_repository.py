# Epic Title: Profile Management

import sqlite3

class UserRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT
            )""")

    def update_user_profile(self, user_id: int, updated_data: dict):
        with self.connection:
            self.connection.execute("""
            UPDATE users SET first_name = ?, last_name = ? WHERE id = ?""",
            (updated_data['first_name'], updated_data['last_name'], user_id))