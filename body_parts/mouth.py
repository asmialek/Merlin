import logging
import pyttsx3 as pyttsx
from singleton_decorator import singleton


@singleton
class Mouth(object):
    def __init__(self, voice):
        self.logger = logging.getLogger(self.__class__.__name__)
        # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
        self.speech_engine = pyttsx.init('sapi5')
        rate = self.speech_engine.getProperty('rate')
        self.speech_engine.setProperty('rate', rate)
        self.voice = voice

    def say(self, text):
        self.logger.debug('Mówię: ' + text)
        if self.voice:
            self.speech_engine.say(text)
            self.speech_engine.runAndWait()

    def test(self, text):
        for voice in self.speech_engine.getProperty('voices'):
            print(voice.id)
            self.speech_engine.setProperty('voice', voice.id)
            print(self.speech_engine.getProperty('voice'))
            self.speech_engine.say(text)
            self.speech_engine.runAndWait()

    def greet(self, name='Adam'):
        self.say('Cześć ' + name)


if __name__ == '__main__':
    mouth = Mouth(True)
    mouth.test('Cześć Świecie')
