import os
from flask import Blueprint, Flask
from flask import Flask, g
from views import blueprint, Resources, UnixTime, PrintArg, ExampleApiUsage
from middleware import APITokenMiddleware
from flask.ext.restful import Api
from client import Client

def create_app():
  api = Api(blueprint)
  api.add_resource(Resources, '/resources')
  api.add_resource(UnixTime, '/time')
  api.add_resource(PrintArg,'/print/<string:arg>')
  api.add_resource(ExampleApiUsage,'/search')

  app = Flask(__name__, static_folder=None) 
  app.url_map.strict_slashes = False
  app.config.from_object('sample_application.config')
  try:
    app.config.from_object('sample_application.local_config')
  except ImportError:
    pass
  app.register_blueprint(blueprint)
  app.client = Client(app.config['CLIENT'])
  return app