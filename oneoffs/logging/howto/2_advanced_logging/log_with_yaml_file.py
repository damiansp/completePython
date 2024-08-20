import logging
import logging.config

import yaml


with open('logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)
logger = logging.getLogger('dev')


logger.debug('debug out')
logger.info('just sayin...')
logger.warning('Im warning you...')
logger.error('does not compute')
logger.critical('I am explode')
