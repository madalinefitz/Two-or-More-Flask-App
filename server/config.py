from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_session import Session
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# db = SQLAlchemy(app)
# migrate = Migrate(app)
# db.init_app(app)
# bcrypt = Bcrypt(app)
api = Api(app)