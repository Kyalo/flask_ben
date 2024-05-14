from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.static_folder = 'pyscripts'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://chatbot:chatbot@localhost/chatbot'

db = SQLAlchemy(app)