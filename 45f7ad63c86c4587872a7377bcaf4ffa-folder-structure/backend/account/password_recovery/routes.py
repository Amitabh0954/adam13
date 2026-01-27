# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, url_for
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from models import User  # Assuming models.py contains a User model
from database import db_session
from mail import mail  # Assuming mail is configured using Flask-Mail
import datetime

password_recovery_bp = Blueprint('password_recovery_bp', __name__)
s = URLSafeTimedSerializer('Thisisasecret!')

@password_recovery_bp.route('/recover', methods=['POST'])
def recover():
    data = request.get_json()
    email = data.get('email')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
        token = s.dumps(email, salt='password_recovery')

        # URL to confirm the password reset action
        link = url_for('password_recovery_bp.reset_with_token', token=token, _external=True)
        send_email(email, link)
        
        return jsonify({'message': 'Password recovery link has been sent to your email address.'}), 200
    return jsonify({'message': 'Email not found'}), 404

@password_recovery_bp.route('/reset/<token>', methods=['POST'])
def reset_with_token(token):
    try:
        email = s.loads(token, salt='password_recovery', max_age=86400)  # Token expires in 24 hours
    except:
        return jsonify({'message': 'The password reset link is invalid or has expired.'}), 400
    
    data = request.get_json()
    new_password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user:
        user.password = generate_password_hash(new_password)
        db_session.commit()
        return jsonify({'message': 'Your password has been updated successfully.'}), 200
    
    return jsonify({'message': 'User not found'}), 404

def send_email(to_email: str, link: str):
    msg = Message('Password Reset', recipients=[to_email])
    msg.body = f'Your link to reset your password is {link}. This link will expire in 24 hours.'
    mail.send(msg)