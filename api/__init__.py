from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed
from .auth.views import auth_namespace
from .students.views import student_namespace
from .courses.views import course_namespace
from .config.config import config_dict
from .utils import db
from .models.courses import Course
from .models.users import User


def create_app(config=config_dict['dev']):
    app=Flask(__name__)


    app.config.from_object(config)

    db.init_app(app)

    jwt=JWTManager(app)

    migrate=Migrate(app, db)

    api=Api(app)

    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"}, 404
    
    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(wrror):
        return {"error": "Method Not Allowed"}, 405

    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(student_namespace, path='/students')
    api.add_namespace(course_namespace, path='/courses')


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Course': Course
        }

    return app