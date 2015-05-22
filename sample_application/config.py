"""
Configuration file. Please prefix application specific config values with
the application name.
"""

SAMPLE_APPLICATION_PARAM = {
    'message': 'config params should be prefixed with the application name',
    'reason': 'this will allow easier integration if this app is incorporated'
              ' as a python module',
}

# General log settings
# Levels allowed: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
SAMPLE_APPLICATION_LOGGING_LEVEL = 'CRITICAL'
# Allowed handlers: file, console, syslog
SAMPLE_APPLICATION_LOGGING_HANDLERS = ['file', 'console', 'syslog']
# Only valid for 'file' handler type
SAMPLE_APPLICATION_LOGGING_FILE_PATH = '/tmp/app.log'

SQLALCHEMY_DATABASE_URI = 'sqlite://'

# These values are necessary only if the app needs to be a client of the API
SAMPLE_APPLICATION_ADSWS_API_TOKEN = 'this is a secret api token!'
SAMPLE_APPLICATION_ADSWS_API_URL = 'https://api.adsabs.harvard.edu'
