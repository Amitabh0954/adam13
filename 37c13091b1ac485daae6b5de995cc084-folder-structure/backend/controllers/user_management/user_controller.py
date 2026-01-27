from flask import Blueprint, request, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from backend.services.user_management.user_service import UserService
from backend.utils import tracker
from datetime import timedelta

user_blueprint = Blueprint('user', __name__)
user_service = UserService()
MAX_INVALID_ATTEMPTS = 5
LOCKOUT_PERIOD = timedelta(minutes=15)  # 15 minutes lockout period

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
    user = user_service.find_by_email(email)

    if user and tracker.is_locked_out(user.id, MAX_INVALID_ATTEMPTS, LOCKOUT_PERIOD):
        return jsonify({"error": "Account locked due to too many invalid login attempts"}), 403

    try:
        authenticated_user = user_service.authenticate_user(email, password)
        if authenticated_user:
            login_user(authenticated_user)
            session.permanent = True
            return jsonify({"message": "Login successful"}), 200
        else:
            if user:
                tracker.add_attempt(user.id)
            return jsonify({"error": "Invalid credentials"}), 401
    except ValueError as e:
        if user:
            tracker.add_attempt(user.id)
        return jsonify({"error": str(e)}), 400

@user_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@user_blueprint.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return jsonify({"message": f"Welcome to your dashboard, {current_user.email}!"}), 200