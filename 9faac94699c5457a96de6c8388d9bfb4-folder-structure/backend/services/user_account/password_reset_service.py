# Epic Title: User Account Management

from backend.repositories.user_account.user_repository import UserRepository
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

class PasswordResetService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.serializer = URLSafeTimedSerializer('Thisisasecret!')
        self.password_reset_expiry = 24 * 3600  # 24 hours

    def request_password_reset(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        if user:
            token = self.serializer.dumps(email, salt='password-reset-salt')
            self.send_email(email, token)

    def reset_password(self, token: str, new_password: str) -> dict:
        try:
            email = self.serializer.loads(token, salt='password-reset-salt', max_age=self.password_reset_expiry)
        except:
            return {'status': 'error', 'message': 'The reset link is invalid or has expired'}
        
        user = self.user_repository.get_user_by_email(email)
        if user:
            user.set_password(new_password)
            self.user_repository.update_user(user)
            return {'status': 'success'}
        return {'status': 'error', 'message': 'User not found'}

    def send_email(self, email: str, token: str):
        link = f'http://example.com/reset?token={token}'
        msg = MIMEText(f'Please use the following link to reset your password within 24 hours: {link}')
        msg['Subject'] = 'Password Reset Request'
        msg['From'] = 'noreply@example.com'
        msg['To'] = email

        with smtplib.SMTP('smtp.example.com') as server:
            server.sendmail('noreply@example.com', email, msg.as_string())