from abc import abstractmethod
from dataclasses import dataclass
from typing import NewType, List

import numpy as np


class Coordinates:
    coordinates: List[int]

    @property
    def x(self) -> int:
        return self.coordinates[0]

    @x.setter
    def x(self, new_x: int):
        self.coordinates[0] = new_x

    @property
    def y(self) -> int:
        return self.coordinates[1]

    @y.setter
    def y(self, new_y: int):
        self.coordinates[1] = new_y


@dataclass
class Position(Coordinates):
    pass


@dataclass
class Velocity(Coordinates):
    pass


Direction = NewType("Direction", float)
Rotation = NewType("Rotation", float)


class GameObject:
    def __init__(self, position:Position, direction:Direction, velocity:Velocity):
        self.position: Position = position
        self.direction: Direction = direction
        self.velocity: Velocity = velocity

    @abstractmethod
    def move(self):
        pass


class SpaceShip(GameObject):
    def __init__(self, position:Position, direction:Direction, velocity:Velocity, rotation:Rotation):
        super().__init__(position, direction, velocity)
        self.rotation: Rotation = rotation

    def move(self):
        x_new = self.position.x + self.velocity.x
        y_new = self.position.y + self.velocity.y
        self.position = Position(x_new, y_new)

        self.direction = self.direction.angle + self.rotation.angular_speed


class Torpedo(GameObject):
    pass


class Meteorite(GameObject):
    pass

