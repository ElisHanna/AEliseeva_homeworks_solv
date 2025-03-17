import os
import logging
from logging.handlers import TimedRotatingFileHandler

os.system('cls')

logger = logging.getLogger('exellent_logger')
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    filename='everyday_actions.log',
    when='midnight',
    interval=1,
    backupCount=7
    )
handler.suffix = '%Y-%m-%d'

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Test message')
