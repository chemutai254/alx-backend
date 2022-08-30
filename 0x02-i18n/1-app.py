#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel
from app import app


class Config(object):
    """Use class config for the app"""
    LANGUAGES = ['en', 'fr']
    """sets local to english and timezone to UTC"""
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)
    babel = Babel(app)

    @app.route('/')
    @app.route('/index')
    def index():
        """Use routes"""
        return render_template("1-index.html")
