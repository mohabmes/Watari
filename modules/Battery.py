from core.Module import Module
from core.Utils import *
import psutil


class Battery(Module):
    priority = 10

    keywords = ['Battery', 'Charger']

    def __init__(self):
        self.battery = psutil.sensors_battery()

    def loop(self):
        plugged = self.battery.power_plugged
        percent = self.battery.percent
        plugged_str = "plugged in" if plugged else "not plugged in"

        if percent <= 25 and not plugged:
            return 'The battery is {}% and charger is {}.'.format(str(percent), plugged_str)
        elif percent <= 95 and plugged:
            return 'The battery is almost 100% and plug charger out {}.'.format(str(percent), plugged_str)


    def start(self, keyword):
        plugged = self.battery.power_plugged
        percent = self.battery.percent
        plugged = "plugged in" if plugged else "not plugged in"

        say('The battery is {}% and charger is {}.'.format(str(percent), plugged))

