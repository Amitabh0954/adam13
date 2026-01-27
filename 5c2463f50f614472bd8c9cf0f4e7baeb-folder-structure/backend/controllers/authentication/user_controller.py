from flask import Blueprint, request, jsonify, url_for
from flask_login import login_user, logout_user, login_required
from backend.services.authentication.user_service import UserService

auth_blueprint = Blueprint('auth', __name__)
user_service = UserService()

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        user_service.register_user(email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_blueprint.route('/login', methods=['POST'])
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

@auth_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200