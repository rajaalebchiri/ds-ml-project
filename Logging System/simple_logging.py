#!/usr/bin/env python
"""simple logging script"""
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(process)d - %(levelname)s - %(asctime)s - %(message)s', level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# passing dynamic data

name = "name"

logging.error("%s raised an error", name)


# Capturing Stack Traces

a = 5
b = 0

try:
    c  = a / b
except Exception as e:
    logging.exception("Exception occurred", exc_info=True)
    

logger = logging.getLogger("example_logger")
logger.warning("this is a warning message")

# using handler
logger_handler = logging.getLogger(__name__)

# create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger_handler.addHandler(c_handler)
logger_handler.addHandler(f_handler)

logger_handler.warning('this is a warning')
logger_handler.error('this is a error')
