# Epic Title: User Login

import sqlite3
import time

class UserRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT,
                last_name TEXT
            )""")
            
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                start_time INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )""")

    def find_user_by_email(self, email: str) -> dict|None:
        cursor = self.connection.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "email": row[1], "password": row[2], "first_name": row[3], "last_name": row[4]}
        return None
    
    def create_session(self, user_id: int) -> int:
        with self.connection:
            cursor = self.connection.execute("""
            INSERT INTO sessions (user_id, start_time)
            VALUES (?, ?)""", 
            (user_id, int(time.time())))
        return cursor.lastrowid