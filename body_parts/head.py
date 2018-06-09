import logging
import sys
from singleton_decorator import singleton

from body_parts.ears import Ears
from body_parts.mouth import Mouth
from body_parts.brain import Brain


@singleton
class Head(object):
    def __init__(self, voice, home):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ears = Ears(voice)
        self.mouth = Mouth(voice)
        self.brain = Brain(self.ears, self.mouth, home)

        # self.Mouth.greet()

    def think(self, voice=True):
        try:
            text, intent, entities = self.ears.listen()
            getattr(self.brain, intent, NotImplementedError)(**entities)
        except (NotImplementedError, self.ears.IntentError):
            self.logger.info('Nie wiem jak mam to zrobić.')
