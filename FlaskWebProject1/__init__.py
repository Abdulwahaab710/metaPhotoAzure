"""
The flask application package.
"""

from flask import Flask
from flask.ext.session import Session
app = Flask(__name__)
sess = Session()
UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess.init_app(app)

import FlaskWebProject1.views
