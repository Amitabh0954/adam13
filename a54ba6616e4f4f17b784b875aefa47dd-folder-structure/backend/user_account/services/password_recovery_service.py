# Epic Title: User Account Management
from repositories.user_repository import UserRepository
import hashlib, uuid
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

class PasswordRecoveryService:
    def __init__(self):
        self.user_repository = UserRepository()

    def request_password_reset(self, email: str) -> dict:
        if not self.user_repository.email_exists(email):
            return {"error": "Email does not exist"}

        token = self.generate_token()
        expiration = datetime.utcnow() + timedelta(hours=24)
        self.user_repository.save_password_reset_token(email, token, expiration)

        self.send_reset_email(email, token)
        return {"message": "Password reset link has been sent to your email"}

    def reset_password(self, token: str, new_password: str) -> dict:
        record = self.user_repository.get_password_reset_record(token)
        
        if not record:
            return {"error": "Invalid or expired token"}
        
        if record['expiration'] < datetime.utcnow():
            return {"error": "Token has expired"}
        
        hashed_password = self.hash_password(new_password)
        self.user_repository.update_password(record['email'], hashed_password)
        self.user_repository.delete_password_reset_token(token)
        
        return {"message": "Password has been reset successfully"}

    def generate_token(self) -> str:
        return str(uuid.uuid4())
    
    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def send_reset_email(self, email: str, token: str):
        msg = MIMEText(f'Click the link to reset your password: http://localhost:5000/reset_password?token={token}')
        msg['Subject'] = 'Password Reset Request'
        msg['From'] = 'noreply@example.com'
        msg['To'] = email

        server = smtplib.SMTP('smtp.example.com')
        server.login('user', 'password')
        server.sendmail('noreply@example.com', [email], msg.as_string())
        server.quit()