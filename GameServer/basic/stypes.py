from typing import NewType

from GameServer.basic.Coordinates import Coordinates
from GameServer.basic.Position import  Position
from GameServer.basic.Velocity import Velocity

Direction = NewType("Direction", int)
Rotating = NewType("Rotating", int)