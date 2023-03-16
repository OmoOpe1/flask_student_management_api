from flask_restx import Namespace, Resource


course_namespace=Namespace('courses', description="namespace for courses")

@course_namespace.route('/courses')
class CreateCourse(Resource):

    def get(self):
        """
            Fetch courses.
        """
        pass

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