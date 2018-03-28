import logging
from head import Head


class Body(object):
    """Acts as a collection of main organ groups.

    Innit shall be as most extensive as possible initialisation method.

    Todo:
        Consider moving logging initialisation from `__init__.py` to Body.

    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info('Zaczynam działać!')
        self.head = Head()
