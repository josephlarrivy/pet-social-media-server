import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import uuid


from models import db

secret_key = 'qwhdu&*UJdwqdqw'
bcrypt = Bcrypt()
db = SQLAlchemy()

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

connect_db(app)



#############################################



@app.route('/test', methods=['GET'])
def testing_api_get():
    return 'connected'

@app.route('/test', methods=['POST'])
def testing_api_post():
    data = request.get_json()
    return data












if __name__ == '__main__':
    app.run(debug=True)