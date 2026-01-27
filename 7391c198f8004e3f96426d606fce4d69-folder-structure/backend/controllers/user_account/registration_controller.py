# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from backend.services.user_account.registration_service import RegistrationService

registration_bp = Blueprint('registration_bp', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    registration_service = RegistrationService()
    result = registration_service.register_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'User registered successfully'}), 201