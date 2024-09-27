from flask import jsonify, request
import os

if os.getenv('ENV') == "development":
  from services.user import UserService
else:
  from src.services.user import UserService
  
class UserController:
  @staticmethod
  def login():
    data = request.json

    user = UserService.login(data)
    if isinstance(user, dict):
        return jsonify({"message": "Login successful", "user": user}), 200
    return jsonify({"error": "Invalid email or password"}), 401
  
  @staticmethod
  def create():
    data = request.json

    user = UserService.create(data)
    if isinstance(user, dict):
        return jsonify({"message": "Create successful", "user": user}), 200
    return jsonify({"error": "Invalid user creation"}), 401
    