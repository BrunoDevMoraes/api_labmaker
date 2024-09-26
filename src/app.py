from flask import Flask
from src.routes.user import UserBlueprint

app = Flask(__name__)

@app.get('/')
def index():
    return "API Labmaker funcionando..."

app.register_blueprint(UserBlueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)