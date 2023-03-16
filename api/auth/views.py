from flask_restx import Namespace, Resource, fields
from flask import request
from http import HTTPStatus
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from ..models.users import User
from ..students.views import user_model, new_user_model


auth_namespace=Namespace('auth', description="namespace for authentication")
signup_model=new_user_model
login_model=auth_namespace.model(
    'Login', {
        'password': fields.String(required=True, description="A password"),
        'email': fields.String(required=True, description="An email")
    })  

@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
            Create a new user account
        """
        data = request.get_json()
        new_user = User(
            name=data.get('name'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
        )
        new_user.save()
        return new_user, HTTPStatus.CREATED
        

@auth_namespace.route('/login')
class Login(Resource):

    
    @auth_namespace.expect(login_model)
    def post(self):
        """
            Log in an existing user
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email = email).first()
        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.email)
            refresh_token = create_refresh_token(identity=user.email) 
            response = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response, HTTPStatus.OK


@auth_namespace.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
            Refresh a JWT
        """
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)

        return { 'access_token': access_token }, HTTPStatus.OK