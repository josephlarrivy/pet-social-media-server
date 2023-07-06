from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import uuid
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

    id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    displayname = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(300), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __init__(self, username, displayname, avatar, password):
        self.id = 'user-' + str(uuid.uuid4())[:30]
        self.username = username
        self.displayname = displayname
        self.avatar = avatar
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def generate_token(self):
        payload = {
            'user_id': self.id,
            'username': self.username,
            'avatar': self.avatar,
            'displayname': self.displayname,
            'authenticated' : True
        }
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode())
        return encoded_payload

    @classmethod
    def test(cls, data):
        test_user = User(username='test_username', displayname='test_display_name', avatar='no_avatar', password='test_password')
        return test_user.generate_token()

    @classmethod
    def register(cls, username, displayname, avatar, password):
        user = cls(username, displayname, avatar, password)
        db.session.add(user)
        db.session.commit()
        return user.generate_token()

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            return user.generate_token()
        else:
            return None

    @classmethod
    def delete_user(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False