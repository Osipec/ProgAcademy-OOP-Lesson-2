import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler(__name__)
filehandler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(file_formatter)
consolehandler = logging.StreamHandler()
consolehandler.setLevel(logging.WARNING)
cons_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consolehandler.setFormatter(cons_formatter)

logger.addHandler(filehandler)
logger.addHandler(consolehandler)
