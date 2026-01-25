from flask import Flask
from backend.controllers.user_account.registration_controller import registration_controller

def register_routes(app: Flask):
    app.register_blueprint(registration_controller, url_prefix='/api')

#### 6. Update MySQL database schema to ensure constraints are applied

##### Create Users Table