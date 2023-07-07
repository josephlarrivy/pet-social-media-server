from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Pet

pet_bp = Blueprint('pet_bp', __name__)

@pet_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'pets success'}), 200

################################################

@pet_bp.route('/', methods=['POST'])
def register_new_pet():
    data = request.get_json()

    owner_id = data.get('ownerId')
    name = data.get('name')
    avatar = data.get('avatar')

    existing_pet = Pet.query.filter_by(owner_id=owner_id, name=name).first()
    if existing_pet:
        return jsonify({'error': 'Duplicate pet'}), 409

    result = Pet.add_pet(owner_id, name, avatar)
    if result == 'success':
        return jsonify({'message': 'Pet registered successfully'}), 200
    else:
        return jsonify({'error': 'Failed to register pet'}), 500


@pet_bp.route('/auth', methods=['POST'])
def authenticate_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    token_bytes = User.authenticate(email, password)
    if token_bytes is None:
        return jsonify({'error': 'Invalid email or password'}), 401

    token_string = token_bytes.decode('utf-8')
    return jsonify({'token': token_string}), 200

@pet_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = User.delete_user(user_id)

    if deleted:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@pet_bp.route('/<user_id>', methods=['PATCH'])
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