# Epic Title: User Registration

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

    def save_user(self, user_data: dict) -> sqlite3.Cursor:
        with self.connection:
            cursor = self.connection.execute("""
            INSERT INTO users (email, password, first_name, last_name)
            VALUES (?, ?, ?, ?)""", 
            (user_data['email'], user_data['password'], user_data['first_name'], user_data['last_name']))
        return cursor