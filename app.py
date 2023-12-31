import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from routes.user_routes import user_bp
from routes.pet_routes import pet_bp
from routes.pet_type_routes import pet_type_bp
from routes.post_routes import post_bp

load_dotenv('.env')
secret_key = os.getenv('SECRET_KEY')

def connect_db(app):
    db.app = app
    db.init_app(app)

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet-social-media-development-db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = secret_key
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db = SQLAlchemy()
connect_db(app)

#############################################

@app.route('/test/app', methods=['GET'])
def testing_api_get():
    return jsonify({'status' : 'connected'})

@app.route('/test/app', methods=['POST'])
def testing_api_post():
    data = request.get_json()
    return data

#############################################

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(pet_bp, url_prefix='/pets')
app.register_blueprint(pet_type_bp, url_prefix='/types')
app.register_blueprint(post_bp, url_prefix='/posts')


if __name__ == '__main__':
    app.run(debug=True)