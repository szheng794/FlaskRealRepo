from flask import Flask
from database import db
from flask_sqlalchemy import SQLAlchemy
s\
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note-app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username