from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URL='sqlite:///people.db',
    SQLALCHEMY_TRACK_MODIFICATION=False,

    WTF_CSRF_ENABLED=False
)
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    job = db.Column(db.String(50))

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'job': self.job
        }
