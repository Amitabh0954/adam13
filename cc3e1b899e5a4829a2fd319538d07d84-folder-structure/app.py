# Epic Title: User Account Management
from flask import Flask
from datetime import timedelta
from backend.controllers.user_management.register_user import register_user_bp
from flask_login import LoginManager

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from backend.models.user import User
        return User.get(user_id)

    app.register_blueprint(register_user_bp, url_prefix='/api/user_management')

    @app.route('/')
    def index():
        return "Welcome to the User Account Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)