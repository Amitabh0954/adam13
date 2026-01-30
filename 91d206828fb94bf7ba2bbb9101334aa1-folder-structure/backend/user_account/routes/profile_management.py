# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from services.profile_management_service import ProfileManagementService

profile_management_bp = Blueprint('profile_management', __name__)
profile_management_service = ProfileManagementService()

@profile_management_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    response = profile_management_service.get_profile(current_user.id)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@profile_management_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    response = profile_management_service.update_profile(current_user.id, data)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200