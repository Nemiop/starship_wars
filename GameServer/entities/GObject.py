from abc import ABC, abstractmethod
from typing import Any

# Game Object interface
class GObject(ABC):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]
