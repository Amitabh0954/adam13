# Epic Title: User Account Management

from flask import Flask
from backend.controllers.account.account_controller import account_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure key for production

# Register Blueprints
app.register_blueprint(account_bp, url_prefix='/account')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)