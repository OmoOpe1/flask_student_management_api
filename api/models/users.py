from datetime import datetime
from sqlalchemy.orm import relationship
from ..utils import db
from .user_courses import UserCourse

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    
    courses = relationship("Course", secondary="user_course", viewonly=True)
    # coursess = db.relationship('Course', back_populates='studentss')

    def __repr__(self) -> str:
        return f"<User {self.name}>"
    
    def save(self): 
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def register_courses(self, items):
        for course, score in items:
            self.user_courses.append(UserCourse(student=self, course=course, score=score))
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

