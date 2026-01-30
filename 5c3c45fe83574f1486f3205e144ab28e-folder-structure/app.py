# Epic Title: User Account Management
from flask import Flask
from backend.user_account.routes.user_registration import user_registration_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(user_registration_bp, url_prefix='/api/user_account')
    
    @app.route('/')
    def index():
        return "Welcome to the User Account Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)