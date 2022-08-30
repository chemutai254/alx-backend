#!/usr/bin/env python3
"""Creates a single route and an index html template"""
from flask import Flask, render_template
from app import app


@app.route('/')
def index():
    return render_template('0-index.html')
