import logging
from logging.config import fileConfig


fileConfig('logging_config.ini')
logger = logging.getLogger(__name__)
logger.debug('often makes a very good meal of %s', 'visiting tourists')
