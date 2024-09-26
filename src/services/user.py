from src.models.user import UserModel

class UserService:
    @staticmethod
    def login(data):
        user = UserModel.login(data)
        return user
