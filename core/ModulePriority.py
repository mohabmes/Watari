from core.CommandCompatibility import *
from operator import methodcaller, itemgetter


class ModulePriority:

    def __init__(self, custom_modules):
        self.modules = custom_modules
        self.sort_by_priority()
        self.remove_disabled()

    def get_modules(self):
        return self.modules

    def sort_by_priority(self):
        self.modules = sorted(self.modules, key=lambda x: x().get_priority(), reverse=True)

    def remove_disabled(self):
        for module in self.modules:
            if module().disable:
                self.modules.remove(module)

