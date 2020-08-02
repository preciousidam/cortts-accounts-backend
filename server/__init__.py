import os
from flask import Flask, render_template
from flask_cors import CORS

from server.models.User import User
from server.util.instances import db, initializeDB, initializeJWT
from server.routes.auth import authRoute
    


def create_app(test_config=None):
    # create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
   
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=False)
        #app.config.from_envvar('APP_CONFIG')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #initialize Database
    initializeDB(app)

    #initialize JWT 
    initializeJWT(app)
   
    #app.json_encoder = JSONEncoder


    #Register Blueprints
    app.register_blueprint(authRoute)


    @app.route('/createDB')
    def create():
        user = User(username="EbubeIdam", 
                    name="Ebube Idam", 
                    email="ebube@cortts.com", 
                    phone="08162300796", 
                    password="pbkdf2:sha256:150000$eGO8fIQ6$8c390d52bd557b4e3a4e1521efe103be9a5cb9cb4db3d0d2dfe3cc29e40ecd41")
        #db.create_all()
        db.session.add(user)
        db.session.commit()
        return 'ok'


    return app