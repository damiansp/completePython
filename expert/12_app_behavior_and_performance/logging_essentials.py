from datetime import datetime, timedelta
import logging


logger = logging.getLogger(__name__)
logging.basicConfig()

logger.log(logging.CRITICAL, 'a critical message')
logger.error('an error msg')
logger.warning('and a warning')
logger.info('basic info')


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt=(
        '%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | '
        '% (message)s'))
handler = logging.handlers.TimedRotatingHandler(
    filename='app.log', when='D', backupCount=28)
handler.setFormatter(formatter)
root_logger.addHandler(handler)


acme_logger = logging.getLogger('acme.utils')
acme_logger.disabled = True
acme_logger.handlers.clear()
acme_logger.setLevel(logging.CRITICAL)
