from abc import ABC, abstractmethod

from types import Direction, Rotation


class IRotatable(ABC):

    @abstractmethod
    def get_direction(self) -> Direction:
        pass

    @abstractmethod
    def get_angular_velocity(self) -> Rotation:
        pass

    def set_direction(self) -> Direction:
        pass


class Move:

    def __init__(self, rotatable: IRotatable):
        self.rotatable: IRotatable = rotatable

    def Execute(self):
        direction = self.rotatable.get_direction()
        angular_vel = self.rotatable.get_angular_velocity()
        new_direction = Direction(direction + angular_vel)
        self.rotatable.set_direction(new_direction)

