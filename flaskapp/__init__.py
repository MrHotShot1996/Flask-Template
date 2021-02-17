# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app instance
app = Flask(__name__)

# configurations
app.config['SECRET_KEY'] = 'Enter long complicated key here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from flaskapp import routes