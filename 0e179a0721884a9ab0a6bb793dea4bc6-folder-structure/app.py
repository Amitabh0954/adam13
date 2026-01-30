# Epic Title: User Account Management
from flask import Flask
from datetime import timedelta
from backend.user_account.routes.user_registration import user_registration_bp
from backend.user_session.routes.user_login import user_login_bp
from flask_login import LoginManager

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(user_registration_bp, url_prefix='/api/user_account')
    app.register_blueprint(user_login_bp, url_prefix='/api/user_session')

    @app.route('/')
    def index():
        return "Welcome to the User Account Management System"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)