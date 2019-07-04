from flask import Flask
from flask import jsonify
from sqlalchemy.sql import func

app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URL='sqlite:///people.db',
    SQLALCHEMY_TRACK_MODIFICATION=False,

    WTF_CSRF_ENABLED=False
)
