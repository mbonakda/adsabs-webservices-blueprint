"""
Configuration file. Please prefix application specific config values with
the application name.
"""

import sys

SAMPLE_APPLICATION_PARAM = {
    'message': 'config params should be prefixed with the application name',
    'reason': 'this will allow easier integration if this app is incorporated'
              ' as a python module',
}

# General log settings
LOGGING_LOG_LEVEL = 'DEBUG'
LOGGING_LOG_FORMAT = '%(levelname)s\t%(process)d [%(asctime)s]:\t%(message)s'
LOGGING_DATE_FORMAT = '%m/%d/%Y %H:%M:%S'
# Allowed types: DISK, SYSLOG, STDOUT
LOGGING_LOG_TYPES = ['STDOUT']

# Logging preferences
LOGGING_STDOUT_SETTINGS = dict(stream=sys.stdout)
LOGGING_SYSLOG_SETTINGS = dict(address='/dev/log')
LOGGING_DISK_PATH = '/tmp/app.log'
LOGGING_DISK_SETTINGS = dict(filename=LOGGING_DISK_PATH,
                             when='h',
                             interval=1,
                             backupCount=0,
                             encoding=None,
                             delay=False,
                             utc=False)

SQLALCHEMY_DATABASE_URI = 'sqlite://'

# These values are necessary only if the app needs to be a client of the API
SAMPLE_APPLICATION_ADSWS_API_TOKEN = 'this is a secret api token!'
SAMPLE_APPLICATION_ADSWS_API_URL = 'https://api.adsabs.harvard.edu'
