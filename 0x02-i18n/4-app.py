#!/usr/bin/env python3
"""Force locale with URL parameter"""
from flask iport Flask, request, render_template
from flack_babel import Babel


class Config(object):
    """Force a particular locale"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    app = Flask(__name__)
    app.config.from_object(Config)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        """Test different translations"""
        loc = request.args.get('locale')
        if loc in app.config['LANGUAGES']:
            return loc
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    @app.route('/')
    def index():
        """Route"""
        return render_template('4-index.html')

    if __name__ == '__main__':
        app.run(port='5000', host='0.0.0.0')
