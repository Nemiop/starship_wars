from abc import abstractmethod

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
