#!/usr/bin/env python3
"""Creates a single route and an index html template"""
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
