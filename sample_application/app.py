"""
Application
"""
import os
from flask import Blueprint
from flask import Flask
from views import UnixTime, PrintArg, ExampleApiUsage
from flask.ext.restful import Api
from flask.ext.discoverer import Discoverer
from models import db
from app_logging import Logging


def create_app():
    """
    Create the application and return it to the user

    :return: flask.Flask application
    """

    app = Flask(__name__, static_folder=None)

    app.url_map.strict_slashes = False
    app.config.from_pyfile('config.py')
    try:
        app.config.from_pyfile('local_config.py')
    except IOError:
        pass

    api = Api(app)
    api.add_resource(UnixTime, '/time')
    api.add_resource(PrintArg, '/print/<string:arg>')
    api.add_resource(ExampleApiUsage, '/search')

    db.init_app(app)

    Discoverer(app)

    logging = Logging()
    logging.init_app(app)

    discoverer = Discoverer(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
