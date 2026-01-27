import logging
from flask import Flask
from backend.controllers.authentication.user_controller import auth_blueprint
from config import Config
from backend.extensions import db, login_manager, bcrypt, mail
from backend.utils import setup_database

# Initialize structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # Set up the database
    with app.app_context():
        setup_database()

    # Register blueprints
    app.register_blueprint(auth_blueprint)

    @app.before_first_request
    def startup():
        logger.info("Application startup")

    @app.teardown_appcontext
    def shutdown(_):
        logger.info("Application shutdown")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)