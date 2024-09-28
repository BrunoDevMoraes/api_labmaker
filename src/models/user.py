import csv
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

if os.getenv('ENV') == "development":
  from utils.google_api import get_gspread_client
else:
  from src.utils.google_api import get_gspread_client

users_path = f'{os.getenv("DATA_PATH")}/users.csv'

class UserModel():
    @staticmethod
    @jwt_required()
    def create(data):
        current_user_email = get_jwt_identity()

        is_admin = False
        last_row = None
        with open(users_path, mode='r') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                last_row = row
                if row['email'] == current_user_email and row['role'] == "admin":
                    is_admin = True
            
            file.seek(0)
            reader = csv.DictReader(file, delimiter=';')

            if is_admin:
                for row in reader:
                    if row['email'] == data['email']:
                        return "Usuário já cadastrado!"
            else:
                return "Você não pode realizar esta ação!"
            
        with open(users_path, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            
            new_id = int(last_row['id']) + 1

            hash_password = generate_password_hash(data['password'])

            writer.writerow([new_id, data['email'], data['name'], data['role'], hash_password])

        return {
            "id": new_id,
            "email": data['email'],
            "name": data['name'],
            "role": data['role'],
        }

    @staticmethod
    def login(data):
        client = get_gspread_client()
        sheet = client.open("TrabModelagemSistemas").worksheet("users")
        
        for row in sheet.get_all_records():
            print(row['email'], data['email'])
            if row['email'] == data['email']:
                if check_password_hash(row['password'], data['password']):
                    access_token = create_access_token(identity=row['email'])
                    return {"id": row['id'], 
                            "name": row['name'], 
                            "email": row['email'], 
                            "token": access_token}
                else:
                    return "Credenciais inválidas!"
            
        return "Credenciais inválidas!"
    