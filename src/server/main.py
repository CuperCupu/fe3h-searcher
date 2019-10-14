import os

from flask import Flask, render_template

from . import directory
from .gifts import gifts

app = Flask(
    'Fire Emblem 3 Houses',
    static_url_path='/static',
    template_folder=directory.get('web/templates'),
    static_folder=directory.get('web/static'),
)

app.register_blueprint(gifts, url_prefix='/gifts')


@app.route('/')
def home():
    return render_template('index.html')


def main():
    app.jinja_env.cache = None
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port='9090')
