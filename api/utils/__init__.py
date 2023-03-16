from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
user_course = db.Table('user_course',
                    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
                    db.Column('course_id', db.Integer(), db.ForeignKey('courses.id')),
                    db.Column('score', db.Integer())
                    )