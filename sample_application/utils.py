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

import os
PROJECT_HOME = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../')
)
import logging
from cloghandler import ConcurrentRotatingFileHandler


def setup_logging_handler(level='DEBUG'):
    """
    Sets up generic logging to a file with rotating files on disk
    :param level: the level of the logging DEBUG, INFO, WARN

    :return: logging instance
    """

    # Get the log level based on the user input
    level = getattr(logging, level)

    # Define the format of the output
    logfmt = '%(levelname)s\t%(process)d [%(asctime)s]:\t%(message)s'
    datefmt = '%m/%d/%Y %H:%M:%S'
    formatter = logging.Formatter(fmt=logfmt, datefmt=datefmt)

    file_name_path = os.path.join(
        os.path.dirname(__file__), PROJECT_HOME, 'logs'
    )

    # Make the logging directory if it does not exist
    if not os.path.exists(file_name_path):
        os.makedirs(file_name_path)

    # Construct the output path for the logs
    file_name = os.path.join(file_name_path, 'app.log')

    # Instantiate the file handler for logging
    # Rotate every 2MB
    rotating_file_handler = ConcurrentRotatingFileHandler(
        filename=file_name,
        maxBytes=2097152,
        backupCount=5,
        mode='a',
        encoding='UTF-8'
    )

    # Add the format and log level
    rotating_file_handler.setFormatter(formatter)
    rotating_file_handler.setLevel(level)

    return rotating_file_handler
