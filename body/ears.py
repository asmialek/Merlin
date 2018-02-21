import logging
import speech_recognition
from wit import Wit


class Ears(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.rec = speech_recognition.Recognizer()
        self.wit_token = 'QHNATOFV7VOCF7YWRR6N3EPCER2GTTS7'

    def listen(self):
        client = Wit(token=self.wit_token)
        with speech_recognition.Microphone() as source:
            self.logger.debug("Słucham!")
            audio = self.rec.listen(source)
            self.logger.debug("Myślę...")
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())
            with open("microphone-results.wav", "rb") as f:
                rtr = client.post_speech(f)
            # print(rtr)
            text = rtr['_text']
            intent = self.get_intent(rtr)
        # print(text, intent)
        return text, intent, rtr

    def get_intent(self, rtr):
        try:
            entities_dict = rtr['outcomes'][0]['entities']
            # print(outcomes_dict)
            intent = entities_dict['intent'][0]['value']
            # print(intent)
            return intent
        except (KeyError, IndexError):
            self.logger.debug('Nie zrozumiałem intencji...')
            return None

# ret = {'datetime': [{'confidence': 1, 'values': [{'value': '2018-02-21T00:00:00.000+01:00', 'grain': 'day', 'type': 'value'}], 'value': '2018-02-21T00:00:00.000+01:00', 'grain': 'day', 'type': 'value'}], 'intent': [{'confidence': 0.96330578927527, 'value': 'get_temperature'}]}
#
# ret = {'intent': [{'confidence': 0.99315341912659, 'value': 'greet'}]}
