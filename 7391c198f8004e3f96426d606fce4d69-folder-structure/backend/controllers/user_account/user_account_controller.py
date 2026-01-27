from flask import Blueprint, request, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
from backend.repositories.user_account.user_repository import UserRepository
from backend.services.user_account.email_service import send_email
from user_account_management.extensions import db

user_account_controller = Blueprint('user_account_controller', __name__)
user_repo = UserRepository()

MAX_LOGIN_ATTEMPTS = 5
TOKEN_EXPIRATION_HOURS = 24

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
    user.current_login_at = datetime.now()
    user.login_count += 1
    user_repo.update_user(user)

    login_user(user)
    session.permanent = True
    return jsonify({"message": "Login successful"}), 200

@user_account_controller.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@user_account_controller.route('/reset_password_request', methods=['POST'])
def reset_password_request():
    data = request.get_json()
    email = data.get('email')

    user = user_repo.get_user_by_email(email)
    if not user:
        return jsonify({"error": "Email not found"}), 404

    token_serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    token = token_serializer.dumps(email, salt='password-reset-salt')

    expires_at = datetime.now() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
    password_reset_token = user_repo.create_password_reset_token(user, token, expires_at)

    reset_url = url_for('user_account_controller.reset_password', token=token, _external=True)
    send_email(
        subject="Password Reset Request",
        recipients=[email],
        text_body=f"Click to reset your password: {reset_url}",
        html_body=f'<p>Click to reset your password: <a href="{reset_url}">{reset_url}</a></p>'
    )

    return jsonify({"message": "Password reset email sent"}), 200

@user_account_controller.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        data = request.get_json()
        new_password = data.get('password')

        if not validate_password(new_password):
            return jsonify({"error": "Password does not meet security criteria"}), 400

        password_reset_token = user_repo.get_password_reset_token_by_token(token)
        if not password_reset_token or password_reset_token.expires_at < datetime.now():
            return jsonify({"error": "Invalid or expired token"}), 400

        user = password_reset_token.user
        user.password = generate_password_hash(new_password)

        user_repo.delete_password_reset_token(password_reset_token)
        user_repo.update_user(user)

        return jsonify({"message": "Password reset successful"}), 200

    return jsonify({"message": "Please provide a new password"}), 200

def validate_password(password: str) -> bool:
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return False
    return True