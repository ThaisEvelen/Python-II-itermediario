from app import db, login
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    remember = db.Column(db.Boolean, default=False)

    # 🔹 novos campos (Ex. 3)
    foto = db.Column(db.String(255))
    bio = db.Column(db.String(255))

    # 🔹 relacionamento (Ex. 4)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
