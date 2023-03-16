from flask_restx import Namespace, Resource, fields
from http import HTTPStatus
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

    @course_namespace.marshal_with(course_model)
    def get(self):
        """
            Fetch courses.
        """
        courses = Course.query.all()

        return courses, HTTPStatus.OK

    @course_namespace.expect(create_course_model)
    @course_namespace.marshal_with(course_model)
    def post(self):
        """
            Create a new course.
        """
        pass

@course_namespace.route('/course/<int:course_id>')
class GetCourse(Resource):

    def get(self, course_id):
        """
            Get course by id.
        """
        pass

@course_namespace.route('/course/<int:course_id>/students')
class CreateCourse(Resource):

    def post(self, course_id):
        """
            Get course students by course id.
        """
        pass