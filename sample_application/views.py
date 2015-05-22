"""
Views
"""

from flask import current_app
from flask.ext.restful import Resource
from flask.ext.discoverer import advertise
from client import client
import time


class UnixTime(Resource):
    """
    Returns the unix timestamp of the server
    """
    decorators = [advertise('scopes', 'rate_limit')]
    scopes = ['scope1', 'scope2']
    rate_limit = [1000, 60*60*24]

    def get(self):
        """
        HTTP GET request
        :return: the unix time now
        """

        current_app.logger.info('Example of logging within the app.')
        return {'now': time.time()}, 200


class PrintArg(Resource):
    """
    Returns the :arg in the route
    """
    decorators = [advertise('scopes', 'rate_limit')]
    scopes = ['scope1', 'scope2']
    rate_limit = [1000, 60*60*24]

    def get(self, arg):
        """
        HTTP GET request that returns the string passed
        :param arg: string to send as return

        :return: argument given to the resource
        """
        return {'arg': arg}, 200


class ExampleApiUsage(Resource):
    """
    This resource uses the client.session.get() method to access an api that
    requires an oauth2 token, such as our own adsws
    """
    decorators = [advertise('scopes', 'rate_limit')]
    scopes = ['scope1']
    rate_limit = [1000, 60*60*24]

    def get(self):
        """
        HTTP GET request using the apps client session defined in the config

        :return: HTTP response from the API
        """

        r = client().get(
            current_app.config.get('SAMPLE_APPLICATION_ADSWS_API_URL')
        )
        return r.json()
