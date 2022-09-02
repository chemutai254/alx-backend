#!/usr/bin/env python3
"""Changes get_local to use s preferred language"""
from flask import render_template, request, Flask
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def class Config(object):
    """Creating a user login system"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    app = Flask(__name__)
    app.config.from_object(Config)
    babel = Babel(app)

    def get_user():
        """
        returns a user dictionary or None if the ID cannot be found
        or if login_as was not passed
        """
        id = request.args.get('login_as', None)
        if id is not None and int(id) in users.keys():
            return users.get(int(id))
        return None

    @app.before_request
    def before_request():
        """ use get_user to find a user if any"""
        user = get_user()
        g.user = user

    @babel.localeselector
    def get_locale():
        """Selects particular locale"""
        loc = request.args.get('locale')
        if loc in app.config['LANGUAGES']:
            return loc
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    app = Flask(__name__)
    app.route('/')

    def index():
        """Route"""
        return render_template('6-index.html')

    if __name__ == '__main__':
        app.run(port="5000", host="0.0.0.0")
