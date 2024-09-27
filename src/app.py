from flask import Flask
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager

load_dotenv()

if os.getenv('ENV') == "development":
  from routes.user import UserBlueprint
else:
  from src.routes.user import UserBlueprint

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400

jwt = JWTManager(app)

@app.get('/')
def index():
    return "API Labmaker funcionando..."

app.register_blueprint(UserBlueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)