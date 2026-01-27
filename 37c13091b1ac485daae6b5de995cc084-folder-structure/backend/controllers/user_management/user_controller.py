from flask import Blueprint, request, jsonify, url_for
from flask_login import login_user, logout_user, login_required, current_user
from backend.services.user_management.user_service import UserService
from backend.utils import generate_token, confirm_token, send_email

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

# Inline comment referencing the Epic Title
# Epic Title: Shopping Cart Functionality

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user_service.register_user(email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user = user_service.authenticate_user(email, password)
        if user:
            login_user(user)
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@user_blueprint.route('/password-recovery', methods=['POST'])
def password_recovery():
    data = request.get_json()
    email = data.get('email')

    try:
        user = user_service.find_by_email(email)
        if user:
            token = generate_token(user.email)
            reset_url = url_for('user.reset_password', token=token, _external=True)
            send_email(
                subject="Password Reset Request",
                recipient=user.email,
                body=f"To reset your password, click the following link: {reset_url}"
            )
            return jsonify({"message": "Password reset link sent to your email"}), 200
        else:
            return jsonify({"error": "Email not registered"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    email = confirm_token(token)
    if not email:
        return jsonify({"error": "Invalid or expired token"}), 400

    data = request.get_json()
    new_password = data.get('password')

    try:
        user_service.reset_password(email, new_password)
        return jsonify({"message": "Password has been reset successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/profile', methods=['GET'])
@login_required
def get_profile():
    return jsonify(current_user.to_dict()), 200

@user_blueprint.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    try:
        user_service.update_profile(current_user.id, data)
        return jsonify({"message": "Profile updated successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400