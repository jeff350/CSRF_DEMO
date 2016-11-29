from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .nav import nav

login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
nav.init_app(app)
login_manager.init_app(app)

from app import views
