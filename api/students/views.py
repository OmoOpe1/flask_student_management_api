from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from flask import request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required
from ..models.users import User
from ..models.courses import Course
from ..models.user_courses import UserCourse
from ..utils import db, get_grade, get_grade_points

student_namespace=Namespace('students', description="namespace for students")
new_user_model=student_namespace.model(
    'User', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description="A password")
    }) 

edit_user_model=student_namespace.model(
    'User', {
        'name': fields.String(required=False, description="A username"),
        'email': fields.String(required=False, description="An email")
    })  

user_model=student_namespace.model(
    'User', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'date_created': fields.String(),
        'courses': fields.List(fields.String())
    }) 


@student_namespace.route('/students')
class CreateStudent(Resource):

    @jwt_required()
    @student_namespace.marshal_list_with(user_model)
    def get(self):
        """
            Fetch students.
        """
        students = User.query.all()
        return students, HTTPStatus.OK

    @jwt_required()
    @student_namespace.expect(new_user_model)
    @student_namespace.marshal_with(user_model)
    def post(self):
        """
            Create a new Student.
        """
        data = student_namespace.payload
        new_student = User(
            name=data['name'],
            email=data['email'],
            password_hash=generate_password_hash(data['password'])
        )
        new_student.save()
        return new_student, HTTPStatus.CREATED


@student_namespace.route('/student/<int:student_id>')
class GetUpdateDeleteStudent(Resource):

    @jwt_required()
    @student_namespace.marshal_with(user_model)
    def get(self, student_id):
        """
            Get student by id.
        """
        student = User.get_by_id(student_id)

        return student, HTTPStatus.OK

    @jwt_required()
    @student_namespace.marshal_with(user_model)
    @student_namespace.expect(edit_user_model)
    def put(self, student_id):
        """
            Update student by id.
        """
        student = User.get_by_id(student_id)
        data = student_namespace.payload
        if ('name' in data):
            student.name = data['name']
        if ('email' in data):
            student.email = data['email']

        db.session.commit()
        return student, HTTPStatus.OK

    @jwt_required()
    def delete(self, student_id):
        """
            Delete student by id.
        """
        student = User.get_by_id(student_id)
        student.delete()
        return { 'message': f"user {student.email} deleted successfully"}, HTTPStatus.OK
    
@student_namespace.route('/student/<int:student_id>/gpa')
class GetStudentGpa(Resource):

    @jwt_required()
    # @student_namespace.marshal_with(user_model)
    def get(self, student_id):
        """
            Get student by id.
        """
        student = User.get_by_id(student_id)
        courses = student.courses

        tnu = 0
        tgp = 0
        for course in courses:
            result = UserCourse.query.filter_by(course_id=course.id, user_id=student_id).first()
            grade = get_grade(result.score)
            gp = get_grade_points(grade, course.units)
            tgp += gp
            tnu += course.units

        return {
            "student_id": student.id,
            "name": student.name,
            "tnu": tnu,
            "tgp": tgp,
            "gpa": round(tgp/tnu, 2)
        }, HTTPStatus.OK

@student_namespace.route('/student/<int:student_id>/courses/register')
class StudentRegisterCourse(Resource):

    @jwt_required()
    @student_namespace.marshal_with(user_model)
    def post(self, student_id):
        """
            Get student with id to course with id.
        """
        student = User.get_by_id(student_id)
        data = student_namespace.payload
        student.register_courses(data)

        return student, HTTPStatus.OK
    
@student_namespace.route('/student/<int:student_id>/course/<int:course_id>/grade')
class StudentGetGrade(Resource):

    @jwt_required()
    # @student_namespace.marshal_with(student_course_model)
    def get(self, student_id, course_id):
        """
            Get student with id to course with id.
        """
        student = User.get_by_id(student_id)
        course = Course.get_by_id(course_id)
        print(student, 'student')

        student_course = UserCourse.query.filter_by(course_id=course_id, user_id=student_id).first()
        grade = get_grade(student_course.score)
        return { 
            "score": student_course.score,
            "grade": grade,
            "grade_units": course.units,
            "grade_points": get_grade_points(grade, course.units)

        }, HTTPStatus.OK
