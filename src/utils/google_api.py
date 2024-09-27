from flask import g
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials_dict = {
  "type": os.getenv("TYPE"),
  "project_id": os.getenv("PROJECT_ID"),
  "private_key_id": os.getenv("PRIVATE_KEY_ID"),
  "private_key": os.getenv("PRIVATE_KEY"),
  "client_email": os.getenv("CLIENT_EMAIL"),
  "client_id": os.getenv("CLIENT_ID"),
  "auth_uri": os.getenv("AUTH_URI"),
  "token_uri": os.getenv("TOKEN_URI"),
  "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
  "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"), 
  "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}

creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

client = gspread.authorize(creds)

sheet = client.open("TrabModelagemSistemas").sheet1

def get_gspread_client():
    """Autentica e retorna o cliente do gspread. Armazena em 'g' para reutilização."""
    if 'gspread_client' not in g:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
        g.gspread_client = gspread.authorize(creds)
    return g.gspread_client