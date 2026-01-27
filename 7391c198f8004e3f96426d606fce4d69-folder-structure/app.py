import logging
from flask import Flask
from user_account_management import user_blueprint
from product_catalog_management import product_blueprint
from config import Config
from user_account_management.extensions import db, login_manager, mail
from user_account_management.utils import setup_database

# Initialize structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Set up the database
    with app.app_context():
        setup_database()

    # Register blueprints
    app.register_blueprint(user_blueprint)
    app.register_blueprint(product_blueprint)

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