import logging
from flask import Blueprint
from flask_restful import Api
from com_py_emp_api.resources.home import Home
from com_py_emp_api.resources.item import Item, Items
from ccom_py_emp_api.resources.user import User, Users, Auth, Access

home = Blueprint('home', __name__, url_prefix='/api')
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
auth = Blueprint('auth', __name__, url_prefix='/api/auth')
access = Blueprint('access', __name__, url_prefix='/api/access')
cabbage = Blueprint('item', __name__, url_prefix='/api/item')

api = Api(home)
api = Api(user)
api = Api(users)
api = Api(auth)
api = Api(access)
api = Api(item)


def initialize_routes(api):
    
    api.add_resource(Home, '/api')
    api.add_resource(Item, '/api/item/<string:id>')
    api.add_resource(Items,'/api/items')
    api.add_resource(User, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@item.errorhandler(500)
def item_api_error(e):
    logging.exception('An error occurred during item request. %s' % str(e))
    return 'An internal error occurred.', 500