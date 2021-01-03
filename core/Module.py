import json
from abc import ABC, abstractmethod


class Module(ABC):
    priority = 0

    def get_priority(self):
        raise NotImplementedError("An operation is not implemented.")

    def get_keywords(self):
        raise NotImplementedError("An operation is not implemented.")

    def loop(self):
        raise NotImplementedError("An operation is not implemented.")

    def start(self):
        raise NotImplementedError("An operation is not implemented.")

    def get_config(self):
        config = open('config/config.json')

        data = json.load(config)
        classname = self.__class__.__name__

        return data[classname][0]
