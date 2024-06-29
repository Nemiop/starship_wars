from abc import abstractmethod
import numpy as np

from Position import Position
from Velocity import Velocity
from types import Direction, Rotation


class GameObject:
    def __init__(self, position:Position, direction:Direction, velocity:Velocity):
        self.position: Position = position
        self.direction: Direction = direction
        self.velocity: Velocity = velocity

    @abstractmethod
    def move(self):
        pass


class SpaceShip(GameObject):
    def __init__(self, position: Position, direction: Direction, velocity: Velocity, rotation: Rotation):
        super().__init__(position, direction, velocity)
        self.rotation: Rotation = rotation

    def move(self):
        self.position.x = self.position.x + self.velocity.x
        self.position.y = self.position.y + self.velocity.y

        self.direction = self.direction + self.rotation


class Torpedo(GameObject):
    pass


class Meteorite(GameObject):
    pass

