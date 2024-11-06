from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)




app.config['SECRET_KEY'] = 'cd1b5eede7d3dd4eb7950bf8b0602635'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), 'comunidade.db'))}"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from comunidadepython import routes
