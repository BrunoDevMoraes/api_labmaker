import csv
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

users_path = f'{os.getenv("DATA_PATH")}/users.csv'

class UserModel():
  def login(data):
    with open(users_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
    
        for row in reader:
            if row['email'] == data['email']:
                if check_password_hash(row['password'], data['password']):
                    access_token = create_access_token(identity=row['email'])
                    return {"id": row['id'], 
                            "nome": row['nome'], 
                            "email": row['email'], 
                            "token": access_token}
                else:
                    return "Credenciais inválidas!"
        
        return "Credenciais inválidas!"