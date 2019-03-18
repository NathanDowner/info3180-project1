from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://xxrfoktnsyjvee:5010e451d51f5efd6366ab8bb5aaa1e5abfaf4c3805202d28094267e5b750885@ec2-54-197-232-203.compute-1.amazonaws.com:5432/d1kt5o5s7ev59j"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


# UPLOAD_FOLDER = './app/static/images'
app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
