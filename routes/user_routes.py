from flask import Blueprint, request, jsonify
from datetime import datetime
from models import User  # adjust this import as necessary

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'success'}), 200

################################################

@user_bp.route('/', methods=['POST'])
def register_new_user():
    data = request.get_json()

    email = data.get('email')
    pet_name = data.get('petName')
    pet_username = data.get('petUsername')
    owner_name = data.get('ownerName')
    avatar = data.get('avatar')
    password = data.get('password')
    initialization_date_time  = datetime.now()

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'duplicate email'}), 409
    
    token_bytes = User.register(email, pet_name, pet_username, owner_name, avatar, password)
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