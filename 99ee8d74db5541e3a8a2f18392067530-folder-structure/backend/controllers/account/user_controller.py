# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.services.account.user_service import UserService
from backend.services.account.password_reset_service import PasswordResetService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user_service = UserService()
    result = user_service.register_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user_service = UserService()
    result = user_service.login_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    session['user_id'] = result['user_id']
    return jsonify({'message': 'User logged in successfully'}), 200

@user_bp.route('/password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    password_reset_service = PasswordResetService()
    result = password_reset_service.initiate_password_reset(email)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password reset link sent successfully'}), 200

@user_bp.route('/password-reset/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('password')

    if not new_password:
        return jsonify({'message': 'New password is required'}), 400

    password_reset_service = PasswordResetService()
    result = password_reset_service.reset_password(token, new_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password updated successfully'}), 200

@user_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not logged in'}), 401

    data = request.get_json()
    user_service = UserService()
    result = user_service.update_user_profile(user_id, data)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Profile updated successfully'}), 200

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User not logged in'}), 401

    user_service = UserService()
    profile = user_service.get_user_profile(user_id)

    if not profile:
        return jsonify({'message': 'Profile not found'}), 404

    return jsonify(profile), 200