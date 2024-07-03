from .GObject import GameObject, Position, Direction, Velocity, Rotating


class SpaceShip(GameObject):
    def __init__(self, position: Position, direction: Direction, velocity: Velocity, rotation: Rotating):
        super().__init__(position, direction, velocity)
        self.rotation: Rotating = rotation

    def move(self):
        self.position.x = self.position.x + self.velocity.x
        self.position.y = self.position.y + self.velocity.y

        self.direction = self.direction + self.rotation
