from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
from flask import request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required
from ..models.users import User

student_namespace=Namespace('students', description="namespace for students")
new_user_model=student_namespace.model(
    'User', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description="A password")
    })  

user_model=student_namespace.model(
    'User', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'date_created': fields.String()
    })  


@student_namespace.route('/students')
class CreateStudent(Resource):

    @jwt_required()
    @student_namespace.marshal_with(user_model)
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
        data = request.get_json()
        new_student = User(
            name=data.get('name'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
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
        student = User.query.get(student_id)

        return student, HTTPStatus.OK

    @jwt_required()
    def put(self, student_id):
        """
            Update student by id.
        """
        pass

    @jwt_required()
    def delete(self, student_id):
        """
            Delete student by id.
        """
        pass