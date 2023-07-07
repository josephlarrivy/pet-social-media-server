from flask import Blueprint, request, jsonify, make_response
from models import PetType

pet_type_bp = Blueprint('pet_type_bp', __name__)

@pet_type_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'pet types success'}), 200

################################################

@pet_type_bp.route('/', methods=['POST'])
def register_new_type():
    data = request.get_json()

    name = data.get('name')

    existing_type = PetType.query.filter_by(type_name=name).first()
    if existing_type:
        return jsonify({'error': 'Duplicate type'}), 409

    result = PetType.add_type(name)
    if result == 'success':
        return jsonify({'message': 'Type added successfully'}), 200
    else:
        return jsonify({'error': 'Failed to radd type'}), 500

@pet_type_bp.route('/<type_id>', methods=['DELETE'])
def delete_type(type_id):
    deleted = PetType.delete_type(type_id)

    if deleted:
        return jsonify({'message': 'Type deleted successfully'}), 200
    else:
        return jsonify({'error': 'Type not found'}), 404

@pet_type_bp.route('/<type_id>', methods=['PATCH'])
def update_type(type_id):
    pet_type = PetType.query.get(type_id)

    if not pet_type:
        return jsonify({'error': 'Type not found'}), 404

    data = request.get_json()
    column_name = data.get('columnName')
    new_value = data.get('newValue')

    if not column_name or not new_value:
        return jsonify({'error': 'Invalid request data'}), 400

    updated = pet_type.update_column(type_id, column_name, new_value)

    if updated:
        return jsonify({'message': 'Type updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update type'}), 500

@pet_type_bp.route('/', methods=['GET'])
def get_all_types():
    try:
        types = PetType.get_all()
        return jsonify({'data': types})
    except Exception as e:
        return make_response(jsonify({"error": "Failed to get types: " + str(e)}), 500)

@pet_type_bp.route('/<type_id>', methods=['GET'])
def get_type(type_id):
    try:
        pet_type = PetType.get_type_by_id(type_id)
        return jsonify({'data': pet_type})
    except Exception as e:
        return make_response(jsonify({"error": "Failed to get type: " + str(e)}), 500)