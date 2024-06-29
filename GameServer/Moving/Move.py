from abc import ABC, abstractmethod
from typing import List

import numpy as np

from Position import Position
from Velocity import Velocity


class IMovable(ABC):

    @abstractmethod
    def get_position(self) -> Position:
        pass

    @abstractmethod
    def get_velocity(self) -> Velocity:
        pass

    def set_position(self, new_position: Position):
        pass


class Move:

    def __init__(self, moveable: IMovable):
        self.movable: IMovable = moveable

    def Execute(self):
        pose = self.movable.get_position().array
        vel = self.movable.get_velocity().array
        new_position = Position((pose + vel).tolist())
        self.movable.set_position(new_position)
