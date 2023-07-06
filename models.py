import json
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import uuid
import base64
from datetime import datetime

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from datetime import datetime, timedelta


secret_key = 'qwhdu&*UJdwqdqw'
bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

###########################################################


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(70), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_username = db.Column(db.String(50), unique=True, nullable=False)
    owner_name = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(300), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    initialization_date_time = db.Column(db.String(100), nullable=False)
    login_count = db.Column(db.Integer, default=0)
    last_login = db.Column(db.Integer, default='none')

    def __init__(self, email, pet_name, pet_username, owner_name, avatar, password):
        self.id = 'user-' + str(uuid.uuid4())[:30]
        self.email = email
        self.pet_name = pet_name
        self.pet_username = pet_username
        self.owner_name = owner_name
        self.avatar = avatar
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.initialization_date_time = datetime.now()
        self.last_login = datetime.now()

    def generate_token(self):
        payload = {
            'userId': self.id,
            'email': self.email,
            'petName': self.pet_name,
            'petUsername': self.pet_username,
            'ownerName': self.owner_name,
            'avatar': self.avatar,
            'authenticated' : True
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode())
        return encoded_payload

    @classmethod
    def register(cls, email, pet_name, pet_username, owner_name, avatar, password):
        user = cls(email, pet_name, pet_username, owner_name, avatar, password)
        user.initialization_date_time = datetime.now()
        user.last_login = datetime.now()
        db.session.add(user)
        db.session.commit()
        return user.generate_token()

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            user.login_count += 1
            user.last_login = datetime.now()
            db.session.add(user)
            db.session.commit()
            return user.generate_token()
        else:
            return None

