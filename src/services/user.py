import os

if os.getenv('ENV') == "development":
  from models.user import UserModel
else:
  from src.models.user import UserModel

class UserService:
    @staticmethod
    def login(data):
        user = UserModel.login(data)
        print(user)
        return user
    
    @staticmethod
    def create(data):
        user = UserModel.create(data)
        return user
