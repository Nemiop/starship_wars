from abc import ABC, abstractmethod
from typing import List

import numpy as np

from GameServer.entities.GObject import GObject
from GameServer.basic.stypes import Position, Velocity


class IMovable(ABC):

    @abstractmethod
    def get_position(self) -> Position:
        pass

    @abstractmethod
    def get_velocity(self) -> Velocity:
        pass

    def set_position(self, new_position: Position) -> None:
        pass


class MovableAdapter(IMovable):

    def __init__(self, g: GObject):
        self.g = g

    def get_position(self) -> Position:
        return self.g["position"]

    def get_velocity(self) -> Velocity:
        return self.g["velocity"]

    def set_position(self, new_position: Position) -> None:
        self.g["position"] = new_position


class Move:

    def __init__(self, moveable: IMovable):
        self.movable: IMovable = moveable

    def execute(self):
        pose = self.movable.get_position().array
        vel = self.movable.get_velocity().array
        new_position = Position((pose + vel).tolist())
        self.movable.set_position(new_position)
