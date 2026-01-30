# Epic Title: User Account Management
from repositories.password_recovery_repository import PasswordRecoveryRepository
from datetime import datetime, timedelta
import jwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.security import generate_password_hash

class PasswordRecoveryService:
    def __init__(self):
        self.password_recovery_repository = PasswordRecoveryRepository()
        self.secret_key = 'supersecretkey'
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587
        self.smtp_username = 'username'
        self.smtp_password = 'password'
        self.sender_email = 'no-reply@example.com'

    def send_recovery_email(self, email: str) -> dict:
        user = self.password_recovery_repository.get_user_by_email(email)
        if not user:
            return {"error": "User with this email does not exist"}

        token = jwt.encode({'user_id': user['id'], 'exp': datetime.utcnow() + timedelta(hours=24)}, self.secret_key, algorithm='HS256')
        link = f"http://example.com/reset-password/{token}"

        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = email
            msg['Subject'] = "Password Recovery"
            msg.attach(MIMEText(f"Click the link to reset your password: {link}", 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, email, msg.as_string())
            server.quit()

            return {"message": "Recovery email sent successfully"}
        except Exception as e:
            return {"error": str(e)}

    def reset_password(self, token: str, new_password: str) -> dict:
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            user_id = decoded['user_id']
            hashed_password = generate_password_hash(new_password)
            success = self.password_recovery_repository.update_password(user_id, hashed_password)
            if success:
                return {"message": "Password reset successfully"}
            return {"error": "Failed to reset password"}
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}