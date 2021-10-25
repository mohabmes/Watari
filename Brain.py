from core.EventDispatcher import *
from core.Utils import *


class Brain:

    def __init__(self):
        event_dispatch = EventDispatcher()
        event_dispatch.notification()

        while 1:
            cmd = input('>>> ')
            if cmd != "":
                event_dispatch.command(cmd)


if __name__ == '__main__':
    Brain()
