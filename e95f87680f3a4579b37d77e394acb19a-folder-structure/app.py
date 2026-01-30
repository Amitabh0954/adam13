# Epic Title: User Account Management
from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user
from datetime import timedelta
from backend.services.user_account_management.register_service import RegisterService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

login_manager = LoginManager()
login_manager.init_app(app)

register_service = RegisterService()

@login_manager.user_loader
def load_user(user_id):
    from backend.models.user import User
    return User.get(user_id)

@app.route('/api/user_management/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    response = register_service.register_user(email, password)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/')
def index():
    return "Welcome to the User Account Management System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)