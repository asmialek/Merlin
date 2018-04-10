from os import path, remove
import logging

# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile(path.join('local', 'Merlin.log')):
    remove(path.join('local', 'Merlin.log'))

# Create the Handler for logging data to a file
file_handler = logging.FileHandler(path.join('local', 'Merlin.log'))
file_handler.setLevel(logging.DEBUG)

# Create the Handler for logging data to a file
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Create and set a Formatter for formatting the log messages
logger_formatter = logging.Formatter('|  %(asctime)s  |  %(name)s \t|  %(levelname)s \t|  %(message)s')
file_handler.setFormatter(logger_formatter)
stream_handler.setFormatter(logger_formatter)

# Initialise the Logger
logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, stream_handler])

# Exclude other libraries from logging
logging.getLogger('urllib3.connectionpool').setLevel(logging.FATAL)
