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

#############################################



