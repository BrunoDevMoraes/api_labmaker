from flask import g
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials_dict = {
  "type": "service_account",
  "project_id": "trabmodelagemsistemas",
  "private_key_id": "b90431f0e91432b83a517564506cab5cfe2c35fe",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCcBqarxFUkqhir\nhkHnd0xhxKWwbX5dkEJZSdmd23EEdC/aN9fIVOruGMYLemaw13JbelVJdL+QiaIy\nUOqZ+/2/lIIpRFrBMtCFxSenf4FPdHQaE+MwNzmrif4SkNS6dIxgYH7RYcG+HwrY\ncACyIsitiYGAmIdDzrKbMPtz/J9DtmbUT1URTwxrxnPOw9OjpK2j/+ZanQRRQ/IZ\nSB9GeotosAJ/RgpCOgprxXH7U4g5l25aagpx9Bo/oFlxrCBLlzCwzQKKcohPlSw+\ntk0mRBORrNSz9AbvfP3RS2l/usOFsmiFdiYGH+niZqm7O0PUI45wmf23gZfIaCNQ\nlQU2Iq77AgMBAAECggEAFyzbu97FQNVtJakjB+UN+OWzMLIK143ydP3Fr69lKaKy\naujpic2nOad/XzwWncTarSDOI0OOosL2zx96wVWPOtItxUBsdI7+Lyh6O+RyCiHD\njw4OLF6/l62/CfXuSyW9piEfJS2uj/VfcIeuasdE5JXsoPPG/7jniaqsZu2KoI1v\ncxfovVZP78DxfbYylmyfkL1d44YzH/0ry9Oi/JQqu87ztyqonI3/4u8jgiFc2mOi\no4vUr4UoyBm6W4t2xLbXfEGxrhdI7E2oMxgbAhGimHXkrl5i3efiwTYLiFLxPH8r\nvc8CYwXLAqiInevCPjKAflb3xWpAjtLGKUP7Y2AOxQKBgQDNOqsoLEJd2jgdl2Hf\nV/6eDXEEgY4E972f/Ij1b1BneFXbexOyMibmtexkR+foYmVJ7CDp1rlxz2nkYw4o\nDQ6bOJyjuIFLhVLyaFhWVHN+JUBDsRFDX80L4ws6QKT2R7QAePT60/A3NI5BbMbF\nrLwbxPyACJ09cSCdyI48PYL9fQKBgQDCn+dsnzn10mW9MjJpkbb4jfJ/GdeH1R5X\n3yUZqVKhpR8Ii/pIMwkK4vY4QehUue0fNLF/t8DtwOv0nAOeAqmpagJt147UQ/b5\nN06yAXagVbPlij2vDdwHn8g4BTQVIUPyINA3TjcqcUQoO2e/OuJ3SjUmXO7Yumo4\n9op+4TTn1wKBgC46+BFNnwmbPabU0hRIsy+RYZMdSAuwbwPaFFQNZjRYtCaD3BT5\nHTA9bOnOFNyRRbXYPjXOy+lqSrVK5wZ4ooCuyQJMbru/Zcb7YGLaFUYmSAq3mWbu\n7ratx3qw0zgzQMYWeUEDewpEiYMNaN1gouMyhZql1h3gHPPOGNRTGu3VAoGBAKZP\nxJACxKG2yC/TrFagKS3fBsDsEUzGpmZKjkaOdckh9BH2o8p8qhZ+eg766xEzzFhl\nS+Sq3peMy1U82K528gqOR0Mb97aV2X9/bqUYMQm0EsVsy2dCvapaNNsCP05rHcfT\nmHoaQXPoVGjY0sAMDqgHZsHAmm3jZpAExbbEtdQDAoGAX4gw+5VtKQvgPlANBf8b\nzcuDOgNcAzgjbOnjWn2QS/TQBoEf4EY9nZeGrVsZQ3KsJau+/iVYlJBGYhg/yihb\nbWdZ3lxHwLz8ZzPntkMtKvljQkQ76sIKtYocS6FO4iTy7+UWXuxMOrvGZz5Vtp/F\nVIWV/2JYt2mKKdzvUVjapHM=\n-----END PRIVATE KEY-----\n",
  "client_email": "teste-349@trabmodelagemsistemas.iam.gserviceaccount.com",
  "client_id": "103770524764685147505",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/teste-349%40trabmodelagemsistemas.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
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