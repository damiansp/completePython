import logging.config


log_config = {
    'version': 1,
    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'formatter': 'standard'}},
    'loggers': {
        'my_logger': {
            'handlers': ['file_handler'],
            'level': 'DEBUG',
            'propagate': False}},
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'}}}
logging.config.dictConfig(log_config)
my_logger = logging.getLogger('my_logger')
my_logger.debug('Debug msg')
