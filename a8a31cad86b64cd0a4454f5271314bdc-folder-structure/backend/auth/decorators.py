# Epic Title: Product Catalog Management

from functools import wraps
from flask import request, jsonify, session

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_admin'):
            return jsonify({'message': 'Admins only!'}), 403
        return f(*args, **kwargs)
    return decorated_function