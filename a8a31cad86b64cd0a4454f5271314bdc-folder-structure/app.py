# Epic Title: User Account Management

from flask import Flask
from backend.user_account_management.controllers.user_controller import user_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(user_bp, url_prefix='/users')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)