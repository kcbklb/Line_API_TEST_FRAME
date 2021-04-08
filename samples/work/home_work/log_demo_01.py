import logging

logger = logging.getLogger('work_01')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

fromatter = logging.Formatter('%(asctime)s  %(levelno)s  %(levelname)s  %(pathname)s  %(filename)s  %(funcName)s  %(lineno)d  %(thread)d  %(threadName)s  %(process)d  %(message)s')
console_handler.setFormatter(fromatter)

logger.addHandler(console_handler)

logger.info('hello world')