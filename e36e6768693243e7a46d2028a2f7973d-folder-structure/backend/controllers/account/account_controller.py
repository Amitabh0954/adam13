# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
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

@account_bp.route('/password_reset_request', methods=['POST'])
def password_reset_request():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    account_service = AccountService()
    result = account_service.initiate_password_reset(email)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password reset link sent'}), 200

@account_bp.route('/password_reset', methods=['POST'])
def password_reset():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({'message': 'Token and new password are required'}), 400

    account_service = AccountService()
    result = account_service.reset_password(token, new_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password reset successfully'}), 200