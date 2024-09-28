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
        print(current_user_email)

        client = get_gspread_client()
        sheet = client.open("TrabModelagemSistemas").worksheet("users")

        rows = sheet.get_all_records()

        is_admin = False
        last_row = None
        for row in rows:
            last_row = row
            if row['email'] == current_user_email and row['role'] == "admin":
                is_admin = True

        if is_admin:
            for row in rows:
                if row['email'] == data['email']:
                    return "Usuário já cadastrado!"
        else:
            return "Você não pode realizar esta ação!"

        new_id = int(last_row['id']) + 1

        hash_password = generate_password_hash(data['password'])

        sheet.insert_row([new_id, data['name'], data['email'], data['role'], hash_password], new_id + 1)

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
            if row['email'] == data['email']:
                if check_password_hash(row['password'], data['password']):
                    access_token = create_access_token(identity=row['email'])
                    return {"id": row['id'], 
                            "name": row['name'], 
                            "email": row['email'],
                            "role": row['role'], 
                            "token": access_token}
                else:
                    return "Credenciais inválidas!"
            
        return "Credenciais inválidas!"
    