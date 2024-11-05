from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



# lembrete pessoal - executar 'python' no terminal, depois 'import secrets' e 'secrets.token_hex(16), depois sair do python com 'exit()'
app.config['SECRET_KEY'] = 'cd1b5eede7d3dd4eb7950bf8b0602635'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

database = SQLAlchemy(app)

from comunidadepython import routes