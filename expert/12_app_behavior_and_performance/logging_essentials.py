import logging


logger = logging.getLogger(__name__)
logging.basicConfig()

logger.log(logging.CRITICAL, 'a critical message')
logger.error('an error msg')
logger.warning('and a warning')
logger.info('basic info')
