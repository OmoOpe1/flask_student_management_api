from ..utils import db, user_course
from datetime import datetime

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    courses = db.relationship('Course', secondary=user_course, backref='userss')

    def __repr__(self) -> str:
        return f"<User {self.name}>"
    
    def save(self): 
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
