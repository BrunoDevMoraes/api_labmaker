import csv
import os
from werkzeug.security import generate_password_hash, check_password_hash

users_path = f'{os.getenv("DATA_PATH")}/users.csv'

class UserModel():
  def login(data):
    with open(users_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
    
        for row in reader:
            if row['email'] == data['email']:
                if check_password_hash(row['password'], data['password']):
                    return {"id": row['id'], "nome": row['nome'], "email": row['email']}
                else:
                    return "Credenciais inválidas!"
        
        return "Credenciais inválidas!"