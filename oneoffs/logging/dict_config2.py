import logging
import logging.config



logging_config = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'my_formatter'},
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'my_app.log',
            'level': 'INFO',
            'formatter': 'my_formatter'}},
    'loggers': {
        'my_app': {
            'handlers': ['conosle', 'file'],
            'level': 'DEBUG',
            'propogate': False}},
    'formatters': {
        'my_formatter': {
            'format': '%(asctime)s - %(name)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'}}}
logging.config.dictConfig(logging_config)
logger = logging.getLogger('my_app')
