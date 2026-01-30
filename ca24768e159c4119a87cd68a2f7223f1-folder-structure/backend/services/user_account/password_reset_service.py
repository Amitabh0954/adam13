# Epic Title: User Account Management
import mysql.connector
import bcrypt
import datetime
import uuid
import smtplib
from email.mime.text import MIMEText

class PasswordResetService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def generate_reset_token(self) -> str:
        return str(uuid.uuid4())

    def send_reset_email(self, email: str, reset_token: str):
        reset_link = f"http://yourdomain.com/reset_password?token={reset_token}"
        msg = MIMEText(f"Click the link to reset your password: {reset_link}")
        msg['Subject'] = 'Password Reset'
        msg['From'] = 'no-reply@yourdomain.com'
        msg['To'] = email

        # Using smtplib for demo purposes. In production, use a reliable email sending service.
        with smtplib.SMTP('localhost') as server:
            server.sendmail(msg['From'], [msg['To']], msg.as_string())

    def request_password_reset(self, email: str) -> dict:
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = self.cursor.fetchone()

        if not user:
            return {"error": "Email does not exist"}

        reset_token = self.generate_reset_token()
        expiration_time = datetime.datetime.now() + datetime.timedelta(hours=24)
        query = "INSERT INTO password_resets (user_id, reset_token, expires_at) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (user['id'], reset_token, expiration_time))
        self.connection.commit()

        self.send_reset_email(email, reset_token)
        return {"message": "Password reset email sent"}

    def verify_reset_token(self, reset_token: str) -> bool:
        self.cursor.execute("SELECT * FROM password_resets WHERE reset_token = %s", (reset_token,))
        token = self.cursor.fetchone()

        if not token:
            return False

        if datetime.datetime.now() > token['expires_at']:
            self.invalidate_reset_token(reset_token)
            return False

        return True

    def invalidate_reset_token(self, reset_token: str):
        query = "DELETE FROM password_resets WHERE reset_token = %s"
        self.cursor.execute(query, (reset_token,))
        self.connection.commit()

    def reset_password(self, reset_token: str, new_password: str) -> dict:
        if not self.verify_reset_token(reset_token):
            return {"error": "Invalid or expired reset token"}

        password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        query = """
        UPDATE users u
        INNER JOIN password_resets pr ON u.id = pr.user_id
        SET u.password = %s
        WHERE pr.reset_token = %s
        """
        self.cursor.execute(query, (password_hash, reset_token))
        self.connection.commit()

        self.invalidate_reset_token(reset_token)
        return {"message": "Password has been reset"}