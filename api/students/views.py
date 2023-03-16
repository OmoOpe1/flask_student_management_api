from flask_restx import Namespace, Resource


student_namespace=Namespace('students', description="namespace for students")


@student_namespace.route('/students')
class CreateStudent(Resource):

    def get(self):
        """
            Fetch students.
        """
        pass

    def post(self):
        """
            Create a new Student.
        """
        pass

@student_namespace.route('/student/<int:student_id>')
class GetUpdateDeleteStudent(Resource):

    def get(self, student_id):
        """
            Get student by id.
        """
        pass

    def put(self, student_id):
        """
            Update student by id.
        """
        pass

    def delete(self, student_id):
        """
            Delete student by id.
        """
        pass