# coding=utf-8

import logging

from fabric.api import task
from .vars.defaults import *


def set_logging(lvl=logging.INFO, log_file_name=None):
    """
    Init logging module
    :param lvl: Define Log level.
    :param log_file_name: Define Log file name.
    :type lvl: Logging level object
    :type log_file_name: String
    """

    # Create log formatter object
    log_fmt = logging.Formatter('[%(levelname)s] - %(asctime)s - %(message)s', datefmt=LOG_DATE_FORMAT)

    try:
        # Create logger with navitia_deployer name.
        logger = logging.getLogger('navitia_deployer')
        logger.setLevel(lvl)

        # Create console handler
        c_logger = logging.StreamHandler()
        c_logger.setLevel(lvl)
        c_logger.setFormatter(log_fmt)

        # Create file handler
        f_logger = logging.FileHandler(log_file_name)
        f_logger.setLevel(lvl)
        f_logger.setFormatter(log_fmt)

        # Add logger to handler
        logger.addHandler(f_logger)
        logger.addHandler(c_logger)

    except Exception:
        # Create default logger.
        logger = logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    return logger


@task
def deploy_on(platform_name, log_lvl=None):
    """
    Load environment variable file.
    :param platform_name: Platform Name
    :param log_lvl: Log level.
    :type platform_name: String
    :type log_lvl: Logging level object.
    """

    # Init logger
    logger = set_logging(log_lvl)

    logger.info("Deploy Navitia on {}.".format(platform_name))

