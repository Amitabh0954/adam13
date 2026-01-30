# Epic Title: User Account Management
from flask import Flask, session
from backend.user_account.routes.user_registration import user_registration_bp
from backend.user_account.routes.user_login import user_login_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # Session will timeout after 30 minutes of inactivity
    
    app.register_blueprint(user_registration_bp, url_prefix='/api/user_account')
    app.register_blueprint(user_login_bp, url_prefix='/api/user_account')
    
    @app.route('/')
    def index():
        return "Welcome to the User Account Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)