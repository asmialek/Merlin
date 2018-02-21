from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from wit import Wit
import speech_recognition as sr
import time

# obtain audio from the microphone
r = sr.Recognizer()
client = Wit(token='QHNATOFV7VOCF7YWRR6N3EPCER2GTTS7')
with sr.Microphone() as source:
    # print("Say something!")
    # audio = r.listen(source)
    # with open("microphone-results.wav", "wb") as f:
    #     f.write(audio.get_wav_data())
    # with open("microphone-results.wav", "rb") as f:
    #     rtr = client.post_speech(f)
    rtr = client.get_message('Jaka dziś pogoda?')
    print(isinstance(rtr, dict))
    print(rtr)
    print(rtr['_text'])
    print(rtr['outcomes'][0]['entities']['intent'][0]['value'])
