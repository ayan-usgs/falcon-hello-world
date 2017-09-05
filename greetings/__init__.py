import logging
import os
import sys


__version__ = '1.8.0dev'


def _create_logger():
    """
    Create a logger object with
    a handler and formatter.

    :return: logger
    :rtype: logging.logger

    """
    log_level_str = os.environ.get('log_level', '')
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - {%(pathname)s:L%(lineno)d} - %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.level = log_level
    return logger


app_logger = _create_logger()
