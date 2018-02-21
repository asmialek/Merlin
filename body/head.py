import logging, sys
from ears import Ears
from mouth import Mouth
# from brain import Brain


class Head(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.Ears = Ears()
        self.Mouth = Mouth()
        # self.Brain = Brain()

        # self.Mouth.greet()

    def think(self):
        text, intent, whole = self.Ears.listen()
        if intent == 'greet':
            self.Mouth.greet()
        elif intent == 'shutdown':
            sys.exit(0)
        else:
            self.logger.info('Nie wiem co mam robić.')


    # def chceck_intetnt(self, command):
    #     if
