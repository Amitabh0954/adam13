# Epic Title: User Account Management

from flask import Flask
from backend.account.registration.routes import registration_bp
from backend.account.login.routes import login_bp
from backend.account.password_recovery.routes import password_recovery_bp
from backend.database import engine, Base
from backend.mail import mail
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure secret key for production

# Register Blueprints
app.register_blueprint(registration_bp, url_prefix='/account')
app.register_blueprint(login_bp, url_prefix='/account')
app.register_blueprint(password_recovery_bp, url_prefix='/account')

# Config Mail
app.config.update(
    MAIL_SERVER='smtp.example.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your-email@example.com',
    MAIL_PASSWORD='your-email-password'
)
mail.init_app(app)

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)