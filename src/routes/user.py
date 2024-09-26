from flask import Blueprint
from controllers.user import UserController

UserBlueprint = Blueprint('user', __name__)

UserBlueprint.route('/login', methods=['POST'])(UserController.login)