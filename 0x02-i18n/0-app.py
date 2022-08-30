#!/usr/bin/env python3
"""Creates a single route and an index html template"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html')
