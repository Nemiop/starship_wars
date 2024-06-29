from typing import List, NewType


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
