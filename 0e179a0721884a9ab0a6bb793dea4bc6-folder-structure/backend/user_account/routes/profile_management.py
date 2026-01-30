# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.profile_service import ProfileService
from flask_login import login_required, current_user

profile_management_bp = Blueprint('profile_management', __name__)
profile_service = ProfileService()

@profile_management_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    user_id = current_user.get_id()
    profile = profile_service.get_profile(user_id)
    if profile:
        return jsonify(profile), 200
    return jsonify({"error": "Profile not found"}), 404

@profile_management_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    user_id = current_user.get_id()
    response = profile_service.update_profile(user_id, data)
    if response.get("error"):
        return jsonify(response), 400
    return jsonify(response), 200