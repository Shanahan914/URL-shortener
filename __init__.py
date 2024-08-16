from flask import Flask
from .models import Url
from .extensions import db, migrate
from .routes import main

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app