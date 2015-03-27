from flask import current_app, Blueprint
from flask.ext.restful import Resource
from flask.ext.discoverer import advertise

import time
import inspect
import sys
import config
from client import Client

if not hasattr(config,'ADSWS_API_TOKEN'):
  config.ADSWS_API_TOKEN = None
client = Client({'TOKEN':config.ADSWS_API_TOKEN})

class UnixTime(Resource):
  '''Returns the unix timestamp of the server'''
  decorators=[advertise('scopes','rate_limit')]
  scopes = ['scope1','scope2'] 
  rate_limit = [1000,60*60*24]
  def get(self):
    return {'now': time.time()}, 200

class PrintArg(Resource):
  '''Returns the :arg in the route'''
  decorators=[advertise('scopes','rate_limit')]
  scopes = ['scope1','scope2']
  rate_limit = [1000,60*60*24]
  def get(self,arg):
    return {'arg':arg}, 200

class ExampleApiUsage(Resource):
  '''This resource uses the client.session.get() method to access an api that requires an oauth2 token, such as our own adsws'''
  decorators=[advertise('scopes','rate_limit')]
  scopes = ['scope1']
  rate_limit = [1000,60*60*24]
  def get(self):
    r = client.session.get(current_app.config.get('SAMPLE_APPLICATION_ADSWS_API_URL'))
    return r.json()
