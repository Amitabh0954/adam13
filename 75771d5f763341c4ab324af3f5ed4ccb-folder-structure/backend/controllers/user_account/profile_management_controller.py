# Epic Title: Profile Management

from flask import Blueprint, request, jsonify
from services.user_account.profile_management_service import ProfileManagementService
from validators.user_account.profile_management_validator import ProfileManagementValidator

profile_management_controller = Blueprint('profile_management_controller', __name__)

@profile_management_controller.route('/update-profile', methods=['POST'])
def update_profile():
    data = request.get_json()
    validator = ProfileManagementValidator(data)
    if validator.is_valid():
        service = ProfileManagementService()
        response = service.update_profile(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400