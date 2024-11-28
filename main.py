from app import app, db
from app.routers import roles_router
from app.routers import users_router
from app.routers import auth_router
from app.routers import health_router
from app.routers import centros_comerciales_router
from app.models import BaseModel
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


BaseModel.set_session(db.session)

