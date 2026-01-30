# Epic Title: User Account Management
from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import timedelta
from backend.services.user_account_management.register_service import RegisterService
from backend.services.user_account_management.login_service import LoginService
from backend.services.user_account_management.password_recovery_service import PasswordRecoveryService
from backend.services.user_account_management.profile_management_service import ProfileManagementService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

login_manager = LoginManager()
login_manager.init_app(app)

register_service = RegisterService()
login_service = LoginService()
password_recovery_service = PasswordRecoveryService()
profile_management_service = ProfileManagementService()

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

@app.route('/api/user_management/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = login_service.authenticate_user(email, password)
    if not user:
        return jsonify({"error": "Invalid email or password"}), 400
    
    login_user(user)
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/api/user_management/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/api/user_management/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    response = password_recovery_service.initiate_password_reset(email)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/user_management/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"error": "Token and new password are required"}), 400

    response = password_recovery_service.reset_password(token, new_password)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/api/user_management/profile', methods=['GET'])
@login_required
def get_profile():
    response = profile_management_service.get_profile(current_user.id)
    return jsonify(response), 200

@app.route('/api/user_management/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    response = profile_management_service.update_profile(current_user.id, data)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@app.route('/')
def index():
    return "Welcome to the User Account Management System"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)