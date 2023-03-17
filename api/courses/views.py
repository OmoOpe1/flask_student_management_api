from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from flask import request
from ..models.courses import Course


course_namespace=Namespace('courses', description="namespace for courses")
create_course_model=course_namespace.model(
    'Course', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'code': fields.String(required=True, description="A course code"),
        'teacher': fields.String(required=True, description="A teacher's name")
    })
course_model=course_namespace.model(
    'Course', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A username"),
        'code': fields.String(required=True, description="A course code"),
        'teacher': fields.String(required=True, description="A teacher's name"),
        'date_created': fields.String()
    })



@course_namespace.route('/courses')
class CreateCourse(Resource):

    @course_namespace.marshal_list_with(course_model)
    @jwt_required()
    def get(self):
        """
            Fetch courses.
        """
        courses = Course.query.all()

        return courses, HTTPStatus.OK

    @course_namespace.expect(create_course_model)
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def post(self):
        """
            Create a new course.
        """
        data = course_namespace.payload
        new_course = Course(
            name=data['name'],
            code=data['code'],
            teacher=data['teacher'])
        new_course.save()

        return new_course, HTTPStatus.CREATED


@course_namespace.route('/course/<int:course_id>')
class GetCourse(Resource):

    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def get(self, course_id):
        """
            Get course by id.
        """
        course = Course.get_by_id(course_id)

        return course, HTTPStatus.OK

@course_namespace.route('/course/<int:course_id>/students')
class CreateCourse(Resource):

    @jwt_required()
    def post(self, course_id):
        """
            Get course students by course id.
        """
        pass