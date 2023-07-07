from flask import Blueprint, request, jsonify
from datetime import datetime
from models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'users success'}), 200

################################################

@user_bp.route('/', methods=['POST'])
def register_new_user():
    data = request.get_json()

    email = data.get('email')
    owner_name = data.get('ownerName')
    avatar = data.get('avatar')
    password = data.get('password')
    initialization_date_time  = datetime.now()

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'duplicate email'}), 409
    
    token_bytes = User.register(email, owner_name, avatar, password)
    token_string = token_bytes.decode('utf-8')
    return jsonify({'token': token_string}), 200

@user_bp.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    token_bytes = User.authenticate(email, password)
    if token_bytes is None:
        return jsonify({'error': 'Invalid email or password'}), 401

    token_string = token_bytes.decode('utf-8')
    return jsonify({'token': token_string}), 200

@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = User.delete_user(user_id)

    if deleted:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@user_bp.route('/<user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    column_name = data.get('columnName')
    new_value = data.get('newValue')

    if not column_name or not new_value:
        return jsonify({'error': 'Invalid request data'}), 400

    updated = user.update_column(user_id, column_name, new_value)

    if updated:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update user'}), 500

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.get_all()
    return jsonify({'data': users})

@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    return jsonify({'data': user})