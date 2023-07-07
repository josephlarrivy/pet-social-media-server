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

@pet_bp.route('/<pet_id>', methods=['DELETE'])
def delete_user(pet_id):
    deleted = Pet.delete_pet(pet_id)

    if deleted:
        return jsonify({'message': 'Pet deleted successfully'}), 200
    else:
        return jsonify({'error': 'Pet not found'}), 404

@pet_bp.route('/<pet_id>', methods=['PATCH'])
def update_user(pet_id):
    pet = Pet.query.get(pet_id)

    if not pet:
        return jsonify({'error': 'Pet not found'}), 404

    data = request.get_json()
    column_name = data.get('columnName')
    new_value = data.get('newValue')

    if not column_name or not new_value:
        return jsonify({'error': 'Invalid request data'}), 400

    updated = pet.update_column(pet_id, column_name, new_value)

    if updated:
        return jsonify({'message': 'Pet updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update pet'}), 500