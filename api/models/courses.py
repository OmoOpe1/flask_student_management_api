from ..utils import db, user_course
from datetime import datetime

class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(6), nullable = False, unique=True)
    teacher = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    students = db.relationship('User', secondary=user_course, backref='coursess')
    
    def __repr__(self) -> str:
        return f"<Course {self.code}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()