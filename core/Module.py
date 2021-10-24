import json
from abc import ABC, abstractmethod
from core.Utils import *

class Module(ABC):
    disable = False
    priority = 0
    keywords = []

    def get_priority(self):
        return self.priority

    def get_keywords(self):
        return self.keywords

    def loop(self):
        pass

    def get_config(self, key=None):
        try:
            config = open('config/config.json')

            data = json.load(config)
            classname = self.__class__.__name__

            if classname in data:
                if key is None:
                    return data[classname]
                elif key in data[classname]:
                    return data[classname][key]
                else:
                    raise Exception('Key \'{}\' is not found'.format(key))

            raise Exception('\'{}\' config is missing'.format(classname))

        except Exception as e:
            display_error(e)

    @abstractmethod
    def start(self, keyword):
        raise NotImplementedError("An operation is not implemented.")
