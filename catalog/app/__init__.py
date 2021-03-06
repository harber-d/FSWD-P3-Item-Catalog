from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')
csrf = CsrfProtect()
csrf.init_app(app)
db = SQLAlchemy(app)

from app import views, models
