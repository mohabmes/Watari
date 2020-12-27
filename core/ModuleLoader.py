import inspect
import importlib
from core.Utils import *
from core.Module import *


class ModuleLoader:

    def __init__(self):
        self.custom_modules = []

    def load(self):
        imported_modules = importlib.import_module('modules')
        modules = inspect.getmembers(imported_modules)
        count = 0
        for module in modules:
            class_obj = module[1]
            if get_class(class_obj) is type(Module):
                if gcm(class_obj) is not gcm(Module):
                    print('Loading {} Module ...'.format(gcm(class_obj)))
                    self.custom_modules.append(class_obj)
                    count += 1

        print("Loaded {} Modules \n".format(count))
        return self.custom_modules
