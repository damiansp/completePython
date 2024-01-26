import logging
import logging.config



logging_config = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'my_app.log',
            'formatter': 'my_formatter'}},
    'loggers': {'my_logger': {'handlers': ['file'], 'level': 'DEBUG'}},
    'formatters': {
        'my_formatter': {'format': '%(asctime)s - %(name)s - %(message)s'}}}
logging.config.dictConfig(logging_config)
logger = logging.getLogger('my_logger')
handler = logging.FileHandler('my_app2.log')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
logger.handlers.pop()  # remove old handler
logger.addHandler(handler)

logger.debug('Send me to my_app2.log, please!')

