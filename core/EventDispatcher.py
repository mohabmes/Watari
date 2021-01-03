import threading
import time
from core.CommandFactory import *
from core.ModulePriority import *
from core.ModuleLoader import *
from core.Voice import *
from core.Utils import *
from queue import Queue


class EventDispatcher:

    def __init__(self):
        self.keywords = None
        self.queue = Queue()
        self.cmdFactory = CommandFactory()

        all_modules = ModuleLoader().load()
        modules_priority = ModulePriority(all_modules)

        self.custom_modules = modules_priority.get_modules()

        self.notification()


    def command(self, keywords):
        try:
            self.keywords = keywords
            handlers = self.cmdFactory.get_handler(self.custom_modules, self.keywords)

            if not handlers:
                raise Exception('Command Not Found')

            if len(handlers) == 1:
                module = handlers[0]
            elif len(handlers) > 1:
                choices = map(lambda handlers : handlers.get_keywords()[0], handlers)
                selected_option = multi_choice_dialog(choices)
                module = handlers[selected_option]

            say('launching {}...'.format(get_class_name(module)), time=True)
            module.start(self.keywords)
            say('Ready.')

        except Exception as e:
            display_error(e)

    def module_loop(self):
        while 1:
            time.sleep(60*30)
            for module in self.custom_modules:
                response = module().loop("")
                if response:
                    print('\n# {}: '.format(get_class_name(module())), end="")
                    say(response)

    def notification(self):
        notify = threading.Thread(target=self.module_loop, args=())
        notify.start()
