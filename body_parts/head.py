import logging
import sys
from singleton_decorator import singleton

from ears import Ears
from mouth import Mouth
from brain import Brain


@singleton
class Head(object):
    def __init__(self, voice):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ears = Ears(voice)
        self.mouth = Mouth(voice)
        self.brain = Brain(self.ears, self.mouth)

        # self.Mouth.greet()

    def think(self, voice=True):
        text, intent, entities = self.ears.listen()
        try:
            getattr(self.brain, intent, NotImplementedError)(**entities)
        except [NotImplementedError, self.ears.IntentError]:
            self.logger.info('Nie wiem jak mam to zrobić.')
