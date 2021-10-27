from core.CommandFactory import *
from core.ModulePriority import *
from core.ModuleLoader import *
from core.Notify import *

class EventDispatcher:

    def __init__(self):
        self.keywords = None
        self.cmdFactory = CommandFactory()
        self.custom_modules = ModuleLoader().load()

    def get_modules(self):
        return self.custom_modules

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

            # say('launching {}...'.format(get_class_name(module)), time=True)
            module.start(self.keywords)
            # say('Ready.')

        except Exception as e:
            display_error(e)
