from os import path
import logging
import speech_recognition
from wit import Wit, exceptions
from singleton_decorator import singleton


@singleton
class Ears(object):
    def __init__(self, voice):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.rec = speech_recognition.Recognizer()
        self.wit_token = 'QHNATOFV7VOCF7YWRR6N3EPCER2GTTS7'
        self.voice = voice

    def listen(self):
        client = Wit(self.wit_token)
        if self.voice:
            with speech_recognition.Microphone() as source:
                self.logger.debug("Słucham!")
                audio = self.rec.listen(source)
                self.logger.debug("Myślę...")
                with open(path.join('local', 'mic-results.wav'), 'wb') as f:
                    f.write(audio.get_wav_data())
                with open(path.join('local', 'mic-results.wav'), 'rb') as f:
                    try:
                        rtr = client.post_speech(f)
                    except exceptions.BadRequestError:
                        return None, None, None
        else:
            self.logger.debug("Czytam!")
            message = input('>>')
            self.logger.debug("Myślę...")
            rtr = client.get_message(message)
        # print('---')
        # print(rtr)
        # print('---')
        text = rtr['_text']
        intent, entities = self.get_wit_intent(rtr)
        # print(text, '->', intent)
        # print('---')
        # print(entities)
        # print('---')
        return text, intent, entities

    def get_wit_intent(self, rtr):
        try:
            entities_dict = rtr['outcomes'][0]['entities']
            intent = entities_dict['intent'][0]['value']
            kwargs_dict = {}
            for item in entities_dict:
                kwargs_dict[item] = entities_dict[item][0]['value']
            del kwargs_dict['intent']
            return intent, kwargs_dict
        except (KeyError, IndexError):
            self.logger.debug('Nie zrozumiałem intencji...')
            return None
