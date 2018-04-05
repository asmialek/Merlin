import logging
import sys
import datetime
from synapses import *
from singleton_decorator import singleton


@singleton
class Brain(object):
    """Acts as a list of possible Merlin actions.

    If Merlin has to do something, add a method for it in here.

    """
    def __init__(self, ears, mouth):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ears = mouth
        self.mouth = mouth
        self.weather_synapse = weather.WeatherSynapse()
        self.who = 'Adam'

    def greet(self, **kwargs):
        self.mouth.say('Cześć ' + self.who)
        self.who = 'Dominika'

    def get_weather(self, **kwargs):
        if 'location' in kwargs.keys():
            location = kwargs['location']
        else:
            location = 'Warszawie'

        if 'datetime' in kwargs.keys():
            mytime = kwargs['datetime']
            timelist = [int(mytime[0:4]), int(mytime[5:7]), int(mytime[8:10]),
                        int(mytime[11:13]), int(mytime[14:16]),
                        int(mytime[17:19])]
            date_and_time = datetime.datetime(*timelist)
        else:
            date_and_time = datetime.datetime.now()

        status, temp, temp_min, temp_max = self.weather_synapse.get_weather(
                                                        location,
                                                        date_and_time)
        temp = str(temp).rstrip('0').rstrip('.')

        if date_and_time.date() == datetime.date.today():
            self.mouth.say('Dzisiaj w {} prognoza to {}'.format(location,
                                                                status))
        else:
            self.mouth.say('Dnia {} w {} prognoza to {}'.format(
                date_and_time.date(), location, status))
        self.mouth.say('Temperatura to ' + temp + ' stopni Celciusza')

    def shutdown(self, **kwargs):
        self.logger.info('Wyłączam system...')
        self.mouth.say('Wyłączam system...')
        self.mouth.say('Do zobaczenia...')
        sys.exit(0)
