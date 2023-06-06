import importlib
from flask_migrate import Migrate
from dotenv import dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

MODULES = ('authentication', 'level', 'guess', 'option', 'questions')

db = SQLAlchemy()

from app.authentication.models import *
from app.level.models import *
from app.guess.models import *
from app.option.models import *
from app.questions.models import *

def configure_database(app):
    # app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config = dotenv_values('.env')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASEURL']

    db.init_app(app)
    # migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

def register_modules(app):
    for module_name in MODULES:
        module = importlib.import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app():
    app = Flask(__name__)

    register_modules(app)
    configure_database(app)
    return app