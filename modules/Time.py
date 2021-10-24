import datetime
from core.Module import Module
from core.Utils import *


class Time(Module):
    priority = 1000

    keywords = ['Time', 'clock', 'date', 'today']

    def __init__(self):
        self.data_format = self.get_config("date_format")
        self.time_format = self.get_config("time_format")

    def loop(self):
        x = datetime.datetime.now()
        time = x.strftime(self.time_format)
        return "It's {} now.".format(time)

    def start(self, keyword):
        x = datetime.datetime.now()
        date = x.strftime(self.data_format)
        time = x.strftime(self.time_format)
        say("It's {} today and {} now.".format(date, time))

