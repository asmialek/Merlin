import logging, sys
from singleton_decorator import singleton

from ears import Ears
from mouth import Mouth
from brain import Brain

@singleton
class Head(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ears = Ears()
        self.mouth = Mouth()
        self.brain = Brain()

        # self.Mouth.greet()

    def think(self, voice=True):
        text, intent, whole = self.ears.listen(voice)
        try:
            getattr(self.brain, intent, NotImplementedError)()
        except NotImplementedError:
            self.logger.info('Nie wiem jak mam to zrobić.')

        # Todo: Move this to the Brain
        if intent == 'greet':
            self.mouth.greet()
        elif intent == 'shutdown':
            self.logger.info('Wyłączam system...')
            sys.exit(0)
        else:
            pass


    # def chceck_intetnt(self, command):
    #     if
