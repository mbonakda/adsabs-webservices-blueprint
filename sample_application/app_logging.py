"""
Utility functions for the blueprint
"""

__author__ = 'J. Elliott'
__maintainer__ = 'J. Elliott'
__copyright__ = 'Copyright 2015'
__version__ = '1.0'
__email__ = 'ads@cfa.harvard.edu'
__status__ = 'Production'
__credit__ = ['V. Sudilovsky']
__license__ = 'GPLv3'

from logging import StreamHandler, Formatter
from logging.handlers import TimedRotatingFileHandler, SysLogHandler


class Logging(object):
    """
    Class for Flask application logging

    Supports three types of handlers:
      File handler
      Standard out
      System log
    """

    def __init__(self):
        """
        Class constructor. Default values can be set here if we do not want
        them within config.py
        """
        self.app = None
        self.level = None
        self.handlers = dict(
            DISK=TimedRotatingFileHandler,
            STDOUT=StreamHandler,
            SYSLOG=SysLogHandler,
        )
        self.log_types = None
        self.log_format = None
        self.date_format = None

    def init_app(self, app):
        """
        Initialises the handlers

        :param app: Flask application instance

        :return: no return
        """

        self.level = app.config['LOGGING_LOG_LEVEL']
        self.log_format = app.config['LOGGING_LOG_FORMAT']
        self.date_format = app.config['LOGGING_DATE_FORMAT']
        self.log_types = app.config['LOGGING_LOG_TYPES']

        formatter = Formatter(
            fmt=self.log_format,
            datefmt=self.date_format
        )

        app.logger.setLevel(self.level)

        for log_type in self.log_types:
            if log_type not in self.handlers:
                print('Ignoring handler: {0}'.format(log_type))
                continue

            handler = self.handlers[log_type](
                **app.config['LOGGING_{0}_SETTINGS'.format(log_type)]
            )

            handler.setLevel(self.level)
            handler.setFormatter(formatter)
            app.logger.addHandler(handler)