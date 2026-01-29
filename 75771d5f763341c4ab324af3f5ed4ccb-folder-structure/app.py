# Epic Title: Password Recovery

from flask import Flask
from backend.controllers.user_account.password_recovery_controller import password_recovery_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(password_recovery_controller, url_prefix='/api')
    
    # Additional setup such as logging and lifecycle hooks can be added here
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)