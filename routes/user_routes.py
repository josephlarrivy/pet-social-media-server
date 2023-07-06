from flask import Blueprint, request, jsonify
from models import User  # adjust this import as necessary

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'success'}), 200

