# Epic Title: User Account Management
import mysql.connector
import bcrypt
import datetime

class LoginService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)
        self.failed_attempts = {}
        self.session_timeout = datetime.timedelta(minutes=30)

    def is_account_locked(self, email: str) -> bool:
        if email in self.failed_attempts and self.failed_attempts[email]["count"] >= 5:
            last_attempt_time = self.failed_attempts[email]["last_attempt"]
            if (datetime.datetime.now() - last_attempt_time).seconds < 300:
                return True
            else:
                del self.failed_attempts[email]
        return False

    def record_failed_attempt(self, email: str):
        if email not in self.failed_attempts:
            self.failed_attempts[email] = {
                "count": 1,
                "last_attempt": datetime.datetime.now()
            }
        else:
            self.failed_attempts[email]["count"] += 1
            self.failed_attempts[email]["last_attempt"] = datetime.datetime.now()

    def reset_failed_attempts(self, email: str):
        if email in self.failed_attempts:
            del self.failed_attempts[email]

    def authenticate(self, email: str, password: str) -> dict:
        if self.is_account_locked(email):
            return {"error": "Account is locked due to multiple failed login attempts. Please try again later."}

        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = self.cursor.fetchone()

        if not user:
            self.record_failed_attempt(email)
            return {"error": "Invalid email or password"}

        if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            self.record_failed_attempt(email)
            return {"error": "Invalid email or password"}

        self.reset_failed_attempts(email)
        session_token = self.create_session(user['id'])
        return {"message": "Login successful", "session_token": session_token}

    def create_session(self, user_id: int) -> str:
        session_token = bcrypt.gensalt().decode('utf-8')
        expiration_time = datetime.datetime.now() + self.session_timeout
        query = "INSERT INTO sessions (user_id, session_token, expires_at) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (user_id, session_token, expiration_time))
        self.connection.commit()

        return session_token

    def is_session_valid(self, session_token: str) -> bool:
        self.cursor.execute("SELECT * FROM sessions WHERE session_token = %s", (session_token,))
        session = self.cursor.fetchone()

        if not session:
            return False

        if datetime.datetime.now() > session['expires_at']:
            self.invalidate_session(session_token)
            return False

        return True

    def invalidate_session(self, session_token: str):
        query = "DELETE FROM sessions WHERE session_token = %s"
        self.cursor.execute(query, (session_token,))
        self.connection.commit()