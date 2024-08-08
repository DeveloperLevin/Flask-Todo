from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#intializing the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'

    #Intializes database with the app
    db.init_app(app)

    from .views import views
    from .auth import auth
    
    #registering databases
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix= '/')

    from .model import User, Note
    create_database(app)

    return app

#script to start up the database if it does not exist
def create_database(app):
    if not path.exists('app/database.db'):
        with app.app_context():
            db.create_all(app)
            print("Created database")