from abc import ABC
from typing import List, NewType

import numpy as np


class Coordinates(ABC):
    def __init__(self, coords: List[int]):
        self.coordinates = coords
    @property
    def array(self) -> np.array:
        return np.array(self.coordinates)

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return np.array_equal(self.array, other.array)
        return False

    @array.setter
    def array(self, new_array: np.array):
        self.coordinates = new_array.tolist()

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

    def __repr__(self):
        return self.coordinates.__repr__()

    def __str__(self):
        return self.coordinates.__str__()