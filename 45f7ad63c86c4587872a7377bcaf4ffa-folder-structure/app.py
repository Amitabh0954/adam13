# Epic Title: User Account Management

from flask import Flask
from backend.account.registration.routes import registration_bp
from backend.account.login.routes import login_bp
from backend.database import engine, Base

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Choose a secure secret key for production

# Register Blueprints
app.register_blueprint(registration_bp, url_prefix='/account')
app.register_blueprint(login_bp, url_prefix='/account')

# Create tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)