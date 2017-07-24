import logging
import os
import sys


def _create_logger():
    log_level_str = os.environ['LOG_LEVEL']
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - {%(pathname)s:L%(lineno)d} - %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.level = log_level
    return logger


app_logger = _create_logger()
