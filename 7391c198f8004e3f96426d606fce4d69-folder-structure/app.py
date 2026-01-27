import logging
from flask import Flask
from user_account_management import user_blueprint
from config import Config

# Initialize structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(user_blueprint)

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