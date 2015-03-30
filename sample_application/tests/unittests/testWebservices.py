import sys, os
PROJECT_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../'))
sys.path.append(PROJECT_HOME)
from flask.ext.testing import TestCase
from flask import url_for, Flask
import unittest
import requests
import time
from httpretty import HTTPretty
import json

import app

class mock_adsws_api:
  def __init__(self,api_endpoint):
    self.api_endpoint = api_endpoint
    def request_callback(request,uri,headers):
      resp = json.dumps(
        {
          'api-response':'success',
          'token':request.headers.get('Authorization','No Authorization header passed!')
        }
      )
      return 200, headers, resp
    HTTPretty.register_uri(HTTPretty.GET, self.api_endpoint,
                       body=request_callback,
                       content_type="application/json")

  def __enter__(self):
    HTTPretty.enable()

  def __exit__(self,etype,value,traceback):
    HTTPretty.reset()
    HTTPretty.disable()


class TestWebservices(TestCase):
  '''Tests that each route is an http response'''
  
  def create_app(self):
    '''Create the wsgi application'''
    app_ = app.create_app()
    return app_

  def test_timeResource(self):
    '''Test the /time route'''
    url = url_for('sample_application.unixtime')
    r = self.client.get(url)
    self.assertEqual(r.status_code,200)
    self.assertIn('now',r.json)
    self.assertNotEqual(r.json.get('now'),time.time()) #The clocks should be (very) slightly different
  
  # def test_nonSpecificUrlRoutes(self):
  #   '''Iterates over each route that doesn't require an argument
  #   testing for http response code < 500'''
  #   for rule in self.app.url_map.iter_rules():
  #     if not rule.arguments: #only test routes that do not require arguments.
  #       url = url_for(rule.endpoint)
  #       with mock_adsws_api(self.app.config.get('SAMPLE_APPLICATION_ADSWS_API_URL')):
  #         r = self.client.get(url)
  #       self.assertTrue(r.status_code < 500,msg="URL: {0}".format(url))

  def test_ResourcesRoute(self):
    '''Tests for the existence of a /resources route, and that it returns properly formatted JSON data'''
    r = self.client.get('/resources')
    self.assertEqual(r.status_code,200)
    [self.assertIsInstance(k, basestring,msg="{0} is not a string".format(k)) for k in r.json] #Assert each key is a string-type

    for expected_field, _type in {'scopes':list,'methods':list,'description':basestring,'rate_limit':list}.iteritems():
      #Assert each resource is described has the expected_field
      [self.assertIn(expected_field,v,msg="{0} not in {1}".format(expected_field,v)) for v in r.json.values()]
      #Assert every expected_field has the proper type
      [self.assertIsInstance(v[expected_field],_type,msg="{0} is not type {1}".format(v[expected_field],_type)) for v in r.json.values()]
      

  def test_ExampleApiUsage(self):
    '''
    Test a route that acts as a client to the main adsws-api. Mocks the response from the adsws-api
    '''
    url = url_for('sample_application.exampleapiusage')
    with mock_adsws_api(self.app.config.get('SAMPLE_APPLICATION_ADSWS_API_URL')):
      r = self.client.get(url)
    self.assertStatus(r,200)
    self.assertEqual(r.json['api-response'],'success')
    self.assertEqual(r.json['token'],"Bearer {token}".format(token=self.app.config.get('SAMPLE_APPLICATION_ADSWS_API_TOKEN')))


if __name__ == '__main__':
  unittest.main(verbosity=2)
