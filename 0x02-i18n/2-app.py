#!/usr/bin/env python3
"""Use fuctions such as getlocale"""
from flask import Flask, request, render_template
from app import app
from flask_babel import Babel


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
