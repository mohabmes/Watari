import datetime
from core.Module import Module
from core.Utils import *


class Time(Module):
    priority = 1000

    disable = False

    def __init__(self):
        self.keywords = ['Time', 'clock', 'date', 'today']

    def get_keywords(self):
        return self.keywords

    def get_priority(self):
        return self.priority

    def loop(self, keyword):
        x = datetime.datetime.now()
        time = x.strftime("%I:%M")
        return "It's {} now.".format(time)

    def start(self, keyword):
        try:
            x = datetime.datetime.now()
            date = x.strftime("%B %d %Y")
            time = x.strftime("%I:%M")
            say("It's {} today and {} now.".format(date, time))

        except Exception as e:
            print("ERROR: {}: {}".format(self.__class__.__name__, e))
