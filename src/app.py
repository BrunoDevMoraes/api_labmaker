from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv('ENV') == "development":
  from routes.user import UserBlueprint
else:
  from src.routes.user import UserBlueprint

app = Flask(__name__)

@app.get('/')
def index():
    return "API Labmaker funcionando..."

app.register_blueprint(UserBlueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)