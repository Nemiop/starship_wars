from abc import ABC, abstractmethod

from GameServer.entities.GObject import GObject
from GameServer.basic.stypes import Direction, Rotating


class IRotable(ABC):

    @abstractmethod
    def get_direction(self) -> Direction:
        pass

    @abstractmethod
    def get_rotating(self) -> Rotating:
        pass

    def set_direction(self, new_direction: Direction) -> None:
        pass


class RotableAdapter(IRotable):

    def __init__(self, g: GObject):
        self.g = g

    def get_direction(self) -> Direction:
        return self.g["direction"]

    def get_rotating(self) -> Rotating:
        return self.g["Rotating"]

    def set_direction(self, new_direction: Direction) -> None:
        self.g["direction"] = new_direction


class Rotate:

    def __init__(self, rotatable: IRotable):
        self.rotatable: IRotable = rotatable

    def execute(self):
        direction = self.rotatable.get_direction()
        angular_vel = self.rotatable.get_rotating()
        new_direction = Direction(direction + angular_vel)
        self.rotatable.set_direction(new_direction)

