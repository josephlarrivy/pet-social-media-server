from flask import Blueprint, request, jsonify, make_response
from models import Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'posts success'}), 200

################################################