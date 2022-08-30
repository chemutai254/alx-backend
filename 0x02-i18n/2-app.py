#!/usr/bin/env python3
"""Use fuctions such as getlocale"""
from flask import Flask, request, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config(object):
    """Declare defaults"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        """create get_local function"""
        return request.accept_languages.best_match('LANGUAGES')

    @app.route('/')
    @app.route('/index')
    def index():
        """routing"""
        return render_template('2-index.html')

    if __name__ == '__main__':
        app.run(port='5000', host='0.0.0.0')
