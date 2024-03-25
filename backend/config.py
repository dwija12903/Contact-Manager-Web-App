# Conatains main configuration of application 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# allows to send request from URL and protcts from different URL
app = Flask(__name__)
CORS(app) # Cross Origin Resource Sharing

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to avoid warning

db = SQLAlchemy(app)


