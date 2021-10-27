from core.EventDispatcher import *


class Brain:

    def __init__(self):
        event_dispatch = EventDispatcher()
        modules = event_dispatch.get_modules()

        self.notifier = Notify(modules)
        self.notifier.start_thread()

        say("Ready")

        while True:
            cmd = input('')
            if cmd:
                event_dispatch.command(cmd)


if __name__ == '__main__':
    Brain()
