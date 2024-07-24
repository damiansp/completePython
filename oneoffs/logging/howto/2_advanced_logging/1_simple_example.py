import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# console handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    logger.debug('Debuggin')
    logger.info('Some info')
    logger.warning("I'm warning you")
    logger.error('Systems error...')
    logger.critical('I am explode')


if __name__ == '__main__':
    main()
