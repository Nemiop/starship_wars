from abc import abstractmethod
from dataclasses import dataclass

import numpy as np


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Direction:
    angle: float


class Velocity:
    speed_x: int
    speed_y: int


class Rotation:
    angular_speed: float


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
        x_new = self.position.x + self.velocity.speed_x
        y_new = self.position.y + self.velocity.speed_y
        self.position = Position(x_new, y_new)

        self.direction = self.direction.angle + self.rotation.angular_speed


class Torpedo(GameObject):
    pass


class Meteorite(GameObject):
    pass

