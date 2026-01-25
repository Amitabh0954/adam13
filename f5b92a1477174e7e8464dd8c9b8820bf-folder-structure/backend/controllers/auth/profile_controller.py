from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.auth.profile_service import ProfileService
import logging

logger = logging.getLogger(__name__)
profile_bp = Blueprint('profile', __name__)

profile_service = ProfileService()

@profile_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user = current_user
    user_data = {
        "email": user.email,
        "name": user.name,
        "preferences": user.preferences
    }
    logger.info(f"Profile data retrieved for user {user.email}")
    return jsonify(user_data), 200

@profile_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    name = data.get('name')
    preferences = data.get('preferences')

    if not name:
        logger.warning("Name is required to update profile")
        return jsonify({"message": "Name is required"}), 400

    try:
        profile_service.update_profile(current_user.id, name, preferences)
        logger.info(f"Profile updated for user {current_user.email}")
        return jsonify({"message": "Profile updated successfully"}), 200
    except ValueError as e:
        logger.warning(f"Profile update failed: {str(e)}")
        return jsonify({"message": str(e)}), 400