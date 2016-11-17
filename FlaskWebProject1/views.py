"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app
from flask import render_template, request, session, abort
import exifTags
import uuid


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            print 403
            abort(403)


def generate_random_string():
    return str(uuid.uuid4())


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = generate_random_string()
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html'), 200


@app.route('/upload_file', methods=['POST'])
def upload_file():
    metaData = exifTags.getMetaData(request.files['file'], None)
    return render_template('results.html', metaData=metaData), 200


# ERROR HANDLING
@app.errorhandler(405)
def methodNotAllowed(e):
    return '<h1>The method is not allowed for the requested URL.</h1>'


@app.errorhandler(404)
def notFound(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(503)
def serviceUnavailable(e):
    return render_template('503.html'), 503
