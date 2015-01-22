from flask import current_app, Blueprint
from flask.ext.restful import Resource
from flask.ext.discoverer import advertise

import time
import inspect
import sys
import config

from client import Client
if not hasattr(config,'CLIENT'):
  config.CLIENT = None
client = Client(config.CLIENT)

class UnixTime(Resource):
  '''Returns the unix timestamp of the server'''
  decorators=[advertise('scopes','rate_limit')]
  scopes = ['oauth:sample_application:read','oauth:sample_application:logged_in'] 
  rate_limit = [1000,60*60*24]
  def get(self):
    return {'now': time.time()}, 200

class PrintArg(Resource):
  '''Returns the :arg in the route'''
  decorators=[advertise('scopes','rate_limit')]
  scopes = ['oauth:sample_application:read','oauth:sample_application:logged_in'] 
  rate_limit = [1000,60*60*24]
  def get(self,arg):
    return {'arg':arg}, 200

class ExampleApiUsage(Resource):
  '''This resource uses the app.client.session.get() method to access an api that requires an oauth2 token, such as our own adsws'''
  scopes = ['oauth:sample_application:read','oauth:sample_application:logged_in','oauth:api:search']
  decorators=[advertise('scopes','rate_limit')]
  rate_limit = [1000,60*60*24]
  def get(self):
    r = client.session.get('http://api.adslabs.org/v1/search')
    try:
      r = r.json()
      return {'response':r, 'api-token-which-should-be-kept-secret':client.token}, 200
    except: #For the moment, 401s are not JSON encoded; this will be changed in the future
      r = r.text
      return {'raw_response':r, 'api-token-which-should-be-kept-secret':client.token}, 401
