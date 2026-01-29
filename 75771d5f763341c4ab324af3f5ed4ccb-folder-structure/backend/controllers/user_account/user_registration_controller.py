# Epic Title: User Registration

from flask import Blueprint, request, jsonify
from services.user_account.user_registration_service import UserRegistrationService
from validators.user_account.user_registration_validator import UserRegistrationValidator

user_registration_controller = Blueprint('user_registration_controller', __name__)

@user_registration_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    validator = UserRegistrationValidator(data)
    if validator.is_valid():
        service = UserRegistrationService()
        response = service.register_user(data)
        return jsonify(response), 201
    return jsonify(validator.errors), 400