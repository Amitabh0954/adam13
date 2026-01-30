# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.user_registration_service import UserRegistrationService

user_registration_bp = Blueprint('user_registration', __name__)

@user_registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_service = UserRegistrationService()
    response = user_service.register_user(data)
    return jsonify(response), 201