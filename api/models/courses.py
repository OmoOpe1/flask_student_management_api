from ..utils import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(6), nullable = False, unique=True)
    teacher = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    
    students = relationship("User", secondary="user_course", viewonly=True)
    
    def __repr__(self) -> str:
        return f"<Course {self.code}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)