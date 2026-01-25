import logging
from datetime import datetime
from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash
from .models import db, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Not authorized'}), 403
    
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    profile_data = {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
        'address': user.address,
        'city': user.city,
        'country': user.country,
        'phone_number': user.phone_number
    }
    
    return jsonify(profile_data), 200

@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Not authorized'}), 403

    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.date_of_birth = datetime.strptime(data.get('date_of_birth'), '%Y-%m-%d') if data.get('date_of_birth') else None
    user.address = data.get('address')
    user.city = data.get('city')
    user.country = data.get('country')
    user.phone_number = data.get('phone_number')
    
    db.session.commit()

    logger.info(f"User {user.email} profile updated successfully")
    return jsonify({'message': 'Profile updated successfully'}), 200