import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger.debug('This debug message to log file')
logger.info('This info msg, too')
logger.warning('And this warning')
logger.error('And this non-ASCII error: s = rθ')
                            
