from .GameObject import GameObject, Position, Direction, Velocity, Rotation


class SpaceShip(GameObject):
    def __init__(self, position: Position, direction: Direction, velocity: Velocity, rotation: Rotation):
        super().__init__(position, direction, velocity)
        self.rotation: Rotation = rotation

    def move(self):
        self.position.x = self.position.x + self.velocity.x
        self.position.y = self.position.y + self.velocity.y

        self.direction = self.direction + self.rotation
