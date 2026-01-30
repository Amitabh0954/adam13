# Epic Title: User Account Management
from flask import Flask
from backend.controllers.user_account.registration_controller import registration_bp
from backend.controllers.user_account.login_controller import login_bp
from backend.controllers.user_account.password_reset_controller import password_reset_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)
app.register_blueprint(password_reset_bp)

@app.route('/')
def index():
    return "Welcome to the User Account Management System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)