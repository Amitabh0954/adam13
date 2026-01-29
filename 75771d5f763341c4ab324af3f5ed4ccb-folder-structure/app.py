# Epic Title: Profile Management

from flask import Flask
from backend.controllers.user_account.profile_management_controller import profile_management_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(profile_management_controller, url_prefix='/api')
    
    # Additional setup such as logging and lifecycle hooks can be added here
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)