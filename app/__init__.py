from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from app.config import environment


app = Flask(__name__)
app.config.from_object(environment)

CORS(app)

authorization = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.1',
    description='RESTApi del Boilerplate',
    doc='/swagger-ui',
    authorizations=authorization
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail = Mail(app)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Permite cualquier origen
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    app.run(debug=True)