import logging
from head import Head


class Body(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info('Zaczynam działać!')
        self.Head = Head()
