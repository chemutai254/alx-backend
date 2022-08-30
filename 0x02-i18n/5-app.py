#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Creating a user login system"""



    users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
