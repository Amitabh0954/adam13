# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from backend.services.user_account.profile_service import ProfileService

profile_bp = Blueprint('profile', __name__)
profile_service = ProfileService()

@profile_bp.route('/api/user_account/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    response = profile_service.get_profile(int(user_id))
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@profile_bp.route('/api/user_account/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    preferences = data.get('preferences')

    if not user_id or not first_name or not last_name or not email:
        return jsonify({"error": "User ID, first name, last name, and email are required"}), 400

    response = profile_service.update_profile(user_id, first_name, last_name, email, preferences)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200