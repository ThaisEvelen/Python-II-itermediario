from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "PD12345678"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/microblog.db'

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

from app import routes
from app.models import models
