from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from src.models import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import os
from dotenv import load_dotenv
from src.config import config
from flask_migrate import Migrate
#db = SQLAlchemy()
load_dotenv()
migrate = Migrate()
def create_app():

    app = Flask(__name__)
    app.config.from_object(config[os.getenv("CONFIG_MODE")])
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URL")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app
