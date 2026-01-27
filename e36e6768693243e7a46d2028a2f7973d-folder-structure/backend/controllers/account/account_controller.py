# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.services.account.account_service import AccountService

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    account_service = AccountService()
    result = account_service.register_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@account_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    account_service = AccountService()
    result = account_service.login_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    session['user_id'] = result['user_id']
    return jsonify({'message': 'User logged in successfully'}), 200

@account_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User must be logged in to view profile'}), 403

    account_service = AccountService()
    profile_data = account_service.get_profile(user_id)
    return jsonify(profile_data), 200

@account_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User must be logged in to update profile'}), 403

    data = request.get_json()
    account_service = AccountService()
    result = account_service.update_profile(user_id, data)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Profile updated successfully'}), 200