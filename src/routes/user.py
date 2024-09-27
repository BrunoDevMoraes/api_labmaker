from flask import Blueprint
import os

if os.getenv('ENV') == "development":
  from controllers.user import UserController
else:
  from src.controllers.user import UserController

UserBlueprint = Blueprint('user', __name__)

UserBlueprint.route('/create', methods=['POST'])(UserController.create)
UserBlueprint.route('/login', methods=['POST'])(UserController.login)