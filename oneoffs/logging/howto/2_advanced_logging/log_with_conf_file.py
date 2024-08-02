import logging
import logging.config


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


logger.debug('debug out')
logger.info('just sayin...')
logger.warning('Im warning you...')
logger.error('does not compute')
logger.critical('I am explode')
