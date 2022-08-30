#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """Default configurations"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app.config.from_object(Config)
    babel = Babel(app)

