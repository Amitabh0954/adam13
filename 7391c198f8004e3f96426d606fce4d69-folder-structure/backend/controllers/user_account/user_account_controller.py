from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.repositories.user_account.user_repository import UserRepository

user_account_controller = Blueprint('user_account_controller', __name__)
user_repo = UserRepository()

MAX_LOGIN_ATTEMPTS = 5

@user_account_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    if user_repo.get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    if not validate_password(password):
        return jsonify({"error": "Password does not meet security criteria"}), 400

    hashed_password = generate_password_hash(password)
    new_user = user_repo.create_user(email, hashed_password, first_name, last_name)

    return jsonify({"message": "User registered successfully"}), 201

@user_account_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_repo.get_user_by_email(email)
    
    if user is None or not check_password_hash(user.password, password):
        if user:
            user.invalid_login_attempts += 1
            user_repo.update_user(user)
            if user.invalid_login_attempts >= MAX_LOGIN_ATTEMPTS:
                return jsonify({"error": "Too many invalid login attempts"}), 403
        return jsonify({"error": "Invalid credentials"}), 401

    user.invalid_login_attempts = 0
    user.last_login_at = user.current_login_at
    user.current_login_at = datetime.datetime.utcnow()
    user.login_count += 1
    user_repo.update_user(user)

    login_user(user)
    session.permanent = True
    return jsonify({"message": "Login successful"}), 200

@user_account_controller.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

def validate_password(password: str) -> bool:
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return False
    return True