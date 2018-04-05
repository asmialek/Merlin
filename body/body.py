import logging
from singleton_decorator import singleton

from head import Head


@singleton
class Body(object):
    """Acts as a collection of main organ groups.

    Innit shall be as most extensive as possible initialisation method.

    Todo:
        Consider moving logging initialisation from `__init__.py` to Body.

    """
    def __init__(self, voice=True):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info('Zaczynam działać!')
        self.head = Head(voice)
