import os
from flask import Blueprint
from flask import Flask, g
from views import Resources, UnixTime, PrintArg, ExampleApiUsage
from flask.ext.restful import Api
from client import Client

def _create_blueprint_():
  '''
  Returns a initialized Flask.Blueprint instance; 
  This should be in a closure instead of the top level of a module because
  a blueprint can only be registered once. Having it at the top level
  creates a problem with unittests in that the app is created/destroyed at every test,
  but its blueprint is still the same object which was already registered
  '''
  return Blueprint(
    'sample_application',
    __name__,
    static_folder=None,
  )

def create_app(blueprint_only=False):
  app = Flask(__name__, static_folder=None) 

  app.url_map.strict_slashes = False
  app.config.from_pyfile('config.py')
  try:
    app.config.from_pyfile('local_config.py')
  except IOError:
    pass

  blueprint = _create_blueprint_()
  api = Api(blueprint)
  api.add_resource(Resources, '/resources')
  api.add_resource(UnixTime, '/time')
  api.add_resource(PrintArg,'/print/<string:arg>')
  api.add_resource(ExampleApiUsage,'/search')

  if blueprint_only:
    return blueprint
  app.register_blueprint(blueprint)
  return app

if __name__ == "__main__":
  app = create_app()
  app.run()
