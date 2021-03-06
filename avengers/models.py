from avengers import app, db

#import for Werrkzerg Security

from werkzeug.security import generate_password_hash, check_password_hash

#import date time module
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email =db.Column(db.String(150), nullable=False, unique=True)
    phone =db.Column(db.String(15), nullable=False, unique=True)
    password =db.Column(db.String(256), nullable=False)
    post = db.relationship('POST', backref='author', lazy=True)

    def __init__(self, username, email, phone, password):
        self.username = username
        self.email =email
        self.phone = phone
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return  f"{self.username} has been created with email: {self.email} and phone number: {self.phone}"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __inti__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"The title of the post is {self.title}\n and the content is {self.content}."