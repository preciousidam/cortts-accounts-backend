from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def initializeDB(app):
    db.init_app(app)


def initializeJWT(app):
    jwt.init_app(app)