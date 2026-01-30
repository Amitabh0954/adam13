# Epic Title: User Account Management
from repositories.password_recovery_repository import PasswordRecoveryRepository
import re
import bcrypt
import jwt
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

class PasswordRecoveryService:
    def __init__(self):
        self.password_recovery_repository = PasswordRecoveryRepository()
        self.secret_key = 'supersecretkey'

    def send_reset_email(self, email: str) -> dict:
        user = self.password_recovery_repository.get_user_by_email(email)
        if not user:
            return {"error": "Email not found"}
        
        token = self.generate_reset_token(user['id'])
        reset_link = f"http://example.com/reset_password?token={token}"

        if self.send_email(email, reset_link):
            return {"message": "Password reset email sent"}
        return {"error": "Failed to send email"}

    def reset_password(self, token: str, new_password: str) -> dict:
        user_id = self.decode_reset_token(token)
        if not user_id:
            return {"error": "Invalid or expired token"}
        
        if not self.is_password_secure(new_password):
            return {"error": "Password does not meet security criteria"}
        
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        
        if self.password_recovery_repository.update_password(user_id, hashed_password):
            return {"message": "Password reset successfully"}
        return {"error": "Failed to reset password"}

    def generate_reset_token(self, user_id: int) -> str:
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def decode_reset_token(self, token: str) -> int | None:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    def send_email(self, to_email: str, reset_link: str) -> bool:
        from_email = 'noreply@example.com'
        subject = 'Password Reset Request'
        body = f'Please click the following link to reset your password: {reset_link}'
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        try:
            with smtplib.SMTP('localhost') as server:
                server.sendmail(from_email, to_email, msg.as_string())
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def is_password_secure(self, password: str) -> bool:
        return (
            len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[\W_]', password)
        )