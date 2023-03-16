from ..utils import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Colum(db.String(), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)