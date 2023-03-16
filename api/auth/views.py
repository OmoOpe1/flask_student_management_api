from flask_restx import Namespace, Resource


auth_namespace=Namespace('auth', description="namespace for authentication")
    
@auth_namespace.route('/signup')
class SignUp(Resource):

    def post(self):
        """
            Create a new user account
        """
        pass

@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Log in an existing user
        """
        pass
