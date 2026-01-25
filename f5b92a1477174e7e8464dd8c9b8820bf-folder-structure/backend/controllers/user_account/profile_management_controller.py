from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.user_account.profile_management_service import ProfileManagementService
import logging

logger = logging.getLogger(__name__)
profile_management_bp = Blueprint('profile_management', __name__)

profile_management_service = ProfileManagementService()

@profile_management_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    try:
        user = profile_management_service.get_profile(current_user.id)
        logger.info(f"Profile data for user '{current_user.email}' retrieved successfully")
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        logger.warning(f"Failed to retrieve profile data: {str(e)}")
        return jsonify({"message": str(e)}), 400

@profile_management_bp.route('/profile', methods=['PATCH'])
@login_required
def update_profile():
    data = request.get_json()

    try:
        user = profile_management_service.update_profile(current_user.id, data)
        logger.info(f"Profile data for user '{current_user.email}' updated successfully")
        return jsonify({"message": "Profile updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Failed to update profile data: {str(e)}")
        return jsonify({"message": str(e)}), 400