# Epic Title: User Account Management

from flask import Flask
from backend.user_account_management.controllers.user_controller import user_bp
from backend.user_account_management.controllers.password_reset_controller import password_reset_bp
from backend.user_account_management.controllers.profile_controller import profile_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(password_reset_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)