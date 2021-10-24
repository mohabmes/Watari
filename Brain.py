from core.EventDispatcher import *
from core.Utils import *


class Brain:

    def __init__(self):
        event_dispatch = EventDispatcher()
        say("Watari Listening: ")

        while 1:
            cmd = input('>>> ')
            if cmd != "":
                event_dispatch.command(cmd)


Brain()
