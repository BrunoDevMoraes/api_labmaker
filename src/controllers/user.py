from flask import jsonify, request
from services.user import UserService

class UserController:
    @staticmethod
    def login():
        data = request.json

        user = UserService.login(data)
        if isinstance(user, dict):
            return jsonify({"message": "Login successful", "user": user}), 200
        return jsonify({"error": "Invalid email or password"}), 401
    