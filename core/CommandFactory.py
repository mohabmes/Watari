from core.CommandCompatibility import *


class CommandFactory:

    def __init__(self):
        self.handlers = []
        self.custom_modules = []

    def get_handler(self, custom_modules, keyword):
        self.handlers = []
        support = CommandCompatibility()

        for module in custom_modules:
            if support.check(keyword, module().get_keywords()):
                self.handlers.append(module())

        return self.handlers

