from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.user_account.profile_service import ProfileService
import logging

logger = logging.getLogger(__name__)
profile_bp = Blueprint('profile', __name__)

profile_service = ProfileService()

@profile_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user_profile = profile_service.get_user_profile(current_user.id)
    return jsonify(user_profile), 200

@profile_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    name = data.get('name')
    preferences = data.get('preferences')

    try:
        profile_service.update_user_profile(current_user.id, name, preferences)
        logger.info(f"Profile updated for user ID: {current_user.id}")
        return jsonify({"message": "Profile updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Profile update failed: {str(e)}")
        return jsonify({"message": str(e)}), 400