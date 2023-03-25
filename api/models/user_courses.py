from ..utils import db
from datetime import datetime
from sqlalchemy.orm import backref, relationship

class UserCourse(db.Model):
    __tablename__='user_course'
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), primary_key=True)
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'), primary_key=True)
    score = db.Column(db.Integer())

    student = relationship("User", backref=backref("user_courses", cascade="all, delete-orphan" ))
    course = relationship("Course", backref=backref("user_courses", cascade="all, delete-orphan" ))

    def __init__(self, student=None, course=None, score=None):
        self.student = student
        self.course = course
        self.score = score
    