"""
Utility functions for the blueprint
"""

from logging import StreamHandler, config
from logging.handlers import TimedRotatingFileHandler, SysLogHandler


class Logging(object):
    """
    Very thin wrappepr class for Flask application logging

    Within the config there should exist a dictionary that defines the types
    of logging.
    """

    def __init__(self, app=None):
        """
        Class constructor. Default values can be set here if we do not want
        them within config.py
        """

        self.logging_dict = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '%(levelname)s\t%(process)d '
                              '[%(asctime)s]:\t%(message)s',
                    'datefmt': '%m/%d/%Y %H:%M:%S',
                }
            },
            'handlers': {
                'file': {
                    'formatter': 'default',
                    'level': 'DEBUG',
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'filename': '/tmp/app.log',
                },
                'console': {
                    'formatter': 'default',
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler'
                },
                'syslog': {
                    'formatter': 'default',
                    'level': 'DEBUG',
                    'class': 'logging.handlers.SysLogHandler',
                    'address': '/dev/log'
                }
            },
            'loggers': {
                '': {
                    'handlers': ['file', 'console', 'syslog'],
                    'level': 'DEBUG',
                    'propagate': True,
                },
            },
        }

        # Some sane defaults
        self.level = 'DEBUG'
        self.handlers = ['console']
        self.file_path = '/tmp/app.log'

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialises the handlers

        :param app: Flask application instance

        :return: no return
        """

        # Load the configured settings
        level = app.config.get('SAMPLE_APPLICATION_LOGGING_LEVEL', 'DEBUG')
        handlers = app.config.get('SAMPLE_APPLICATION_LOGGING_HANDLERS',
                                  ['file', 'console', 'syslog'])

        # Reset the level if the one given is not supported by logging
        if level not in \
                ['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:

            print('Level defined "{level}" is not supported, defaulting to: '
                  '"{new_level}"'.format(level=level, new_level=self.level))

            level = self.level

        # Remove any undefined handlers
        for handler in handlers:
            if handler not in self.logging_dict['handlers'].keys():
                print('Handler type "{handler}", is not supported.'
                      .format(handler=handler))
                handlers.remove(handler)

        # If the user gave only undefined handlers, default to console
        if not handlers:
            print('No defined handlers given, defaulting to console logging.')
            handlers = self.handlers

        if 'file' in handlers:
            file_path = app.config.get('SAMPLE_APPLICATION_LOGGING_FILE_PATH',
                                       self.file_path)

        self.logging_dict['loggers']['']['handlers'] = handlers
        self.logging_dict['loggers']['']['level'] = level
        self.logging_dict['handlers']['file']['filename'] = file_path

        self.set_config()

    def set_config(self):
        """
        Initialises the dictionary config for all the loggers

        :return: none
        """
        
        config.dictConfig(self.logging_dict)