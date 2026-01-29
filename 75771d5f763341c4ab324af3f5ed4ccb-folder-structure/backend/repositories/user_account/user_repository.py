# Epic Title: Password Recovery

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
            CREATE TABLE IF NOT EXISTS password_recoveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL,
                token_expiry_time INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )""")

    def find_user_by_email(self, email: str) -> dict|None:
        cursor = self.connection.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "email": row[1], "password": row[2], "first_name": row[3], "last_name": row[4]}
        return None
    
    def save_recovery_token(self, user_id: int, token: str, token_expiry_time: int):
        with self.connection:
            self.connection.execute("""
            INSERT INTO password_recoveries (user_id, token, token_expiry_time)
            VALUES (?, ?, ?)""", 
            (user_id, token, token_expiry_time))

    def find_user_by_token(self, token: str) -> dict|None:
        cursor = self.connection.execute("""
        SELECT u.id, u.email, u.password, u.first_name, u.last_name, pr.token_expiry_time
        FROM users AS u
        JOIN password_recoveries AS pr ON u.id = pr.user_id
        WHERE pr.token = ?""", (token,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "email": row[1], "password": row[2], "first_name": row[3], "last_name": row[4], "token_expiry_time": row[5]}
        return None

    def update_password(self, user_id: int, new_password: str):
        with self.connection:
            self.connection.execute("""
            UPDATE users SET password = ? WHERE id = ?""",
            (new_password, user_id))