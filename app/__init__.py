from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config 
from models import db as root_db, ma
from .api.routes import api

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

app.config.from_object(Config)
root_db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

