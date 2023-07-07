import os
import json
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import uuid
import base64
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('.env')
secret_key = os.getenv('SECRET_KEY')

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
    owner_name = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(300), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    initialization_date_time = db.Column(db.Date, nullable=False)
    login_count = db.Column(db.Integer, default=0)
    last_login = db.Column(db.Date, default='none')

    def __init__(self, email, owner_name, avatar, password):
        self.id = 'user-' + str(uuid.uuid4())[:30]
        self.email = email
        self.owner_name = owner_name
        self.avatar = avatar
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.initialization_date_time = datetime.now()
        self.last_login = datetime.now()

    def generate_token(self):
        payload = {
            'userId': self.id,
            'email': self.email,
            'ownerName': self.owner_name,
            'avatar': self.avatar,
            'authenticated' : True
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode())
        return encoded_payload

    @classmethod
    def register(cls, email, owner_name, avatar, password):
        user = cls(email, owner_name, avatar, password)
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

    @classmethod
    def delete_user(cls, user_id):
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def update_column(cls, user_id, column_name, value):
        user = cls.query.get(user_id)

        if user:
            setattr(user, column_name, value)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def get_all(cls):
        users = cls.query.all()
        all_users = []

        for user in users:
            serialized_user = {
                'id': user.id,
                'email': user.email,
                'owner_name': user.owner_name,
                'avatar': user.avatar,
                'initialization_date_time': user.initialization_date_time
            }
            all_users.append(serialized_user)

        return all_users

    @classmethod
    def get_user_by_id(cls, user_id):
        user = cls.query.get(user_id)
        serialized_user = {
            'id': user.id,
            'email': user.email,
            'owner_name': user.owner_name,
            'avatar': user.avatar,
            'initialization_date_time': user.initialization_date_time
        }
        return serialized_user


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.String(35), primary_key=True, unique=True, nullable=False)
    owner_id = db.Column(db.String(35), db.ForeignKey('users.id'), nullable=False)
    type_id = db.Column(db.String(35), db.ForeignKey('pet_types.id'))
    name = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(300), nullable=False)
    initialization_date_time = db.Column(db.Date, nullable=False)

    pet_type = db.relationship('PetType', backref=db.backref('pets', lazy=True))

    def __init__(self, owner_id, type_id, name, avatar):
        self.id = 'pet-' + str(uuid.uuid4())[:30]
        self.owner_id = owner_id
        self.type_id = type_id
        self.name = name
        self.avatar = avatar
        self.initialization_date_time = datetime.now()

    @classmethod
    def add_pet(cls, owner_id, type_id, name, avatar):
        try:
            pet = cls(owner_id=owner_id, type_id=type_id, name=name, avatar=avatar)
            pet.initialization_date_time = datetime.now()
            db.session.add(pet)
            db.session.commit()
            return 'success'
        except Exception as e:
            print(str(e))
            return 'error'

    @classmethod
    def delete_pet(cls, pet_id):
        pet = cls.query.get(pet_id)
        if pet:
            db.session.delete(pet)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def update_column(cls, pet_id, column_name, value):
        pet = cls.query.get(pet_id)

        if pet:
            setattr(pet, column_name, value)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def get_all(cls):
        pets = cls.query.all()
        all_pets = []

        for pet in pets:
            serialized_pet = {
                'id': pet.id,
                'owner_id': pet.owner_id,
                'name': pet.name,
                'avatar': pet.avatar,
                'pet_type': pet.pet_type.type_name if pet.pet_type else None,
                'initialization_date_time': pet.initialization_date_time
            }
            all_pets.append(serialized_pet)

        return all_pets

    @classmethod
    def get_pets_by_user_id(cls, user_id):
        pets = cls.query.filter_by(owner_id=user_id).all()
        user_pets = []

        for pet in pets:
            serialized_pet = {
                'id': pet.id,
                'owner_id': pet.owner_id,
                'name': pet.name,
                'avatar': pet.avatar,
                'pet_type': pet.pet_type.type_name if pet.pet_type else None,
                'initialization_date_time': pet.initialization_date_time
            }
            user_pets.append(serialized_pet)

        return user_pets



    @classmethod
    def get_pet_by_id(cls, pet_id):
        pet = cls.query.get(pet_id)
        serialized_pet = {
            'id': pet.id,
            'owner_id': pet.owner_id,
            'name': pet.name,
            'avatar': pet.avatar,
            'initialization_date_time': pet.initialization_date_time
        }
        return serialized_pet

class PetType(db.Model):
    __tablename__ = 'pet_types'

    id = db.Column(db.String(35), primary_key=True, unique=True, nullable=False)
    type_name = db.Column(db.String(50), nullable=False)

    def __init__(self, type_name, description=None):
        self.id = 'type-' + str(uuid.uuid4())[:30]
        self.type_name = type_name

    @classmethod
    def add_type(cls, type_name):
        try:
            pet_type = cls(type_name)
            db.session.add(pet_type)
            db.session.commit()
            return 'success'
        except Exception as e:
            print(str(e))
            return 'error'

    @classmethod
    def delete_type(cls, type_id):
        pet_type = cls.query.get(type_id)
        if pet_type:
            db.session.delete(pet_type)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def update_column(cls, type_id, column_name, value):
        pet_type = cls.query.get(type_id)

        if pet_type:
            setattr(pet_type, column_name, value)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def get_all(cls):
        types = cls.query.all()
        all_types = []

        for pet_type in types:
            serialized_type = {
                'id': pet_type.id,
                'type_name': pet_type.type_name
            }
            all_types.append(serialized_type)

        return all_types

    @classmethod
    def get_type_by_id(cls, type_id):
        pet_type = cls.query.get(type_id)
        serialized_type = {
            'id': pet_type.id,
            'type_name': pet_type.type_name
        }
        return serialized_type