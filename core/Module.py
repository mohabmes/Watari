from abc import ABC, abstractmethod
from core.Config import *

class Module(ABC):
    priority = 0
    keywords = []

    def get_priority(self):
        return self.priority

    def get_keywords(self):
        return self.keywords

    def loop(self):
        pass

    def get_config(self, key=None):
        classname = get_class_name(self)
        return Config().get(classname, key)

    @abstractmethod
    def start(self, keyword):
        raise NotImplementedError("An operation is not implemented.")
