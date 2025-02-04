import coverage
import unittest
from unittest.mock import MagicMock, patch

from GameServer.entities.GObject import GObject
from GameServer.mechanics.Move import IMovable, Move, MovableAdapter
from GameServer.mechanics.Rotate import IRotable, Rotate, RotableAdapter
from GameServer.basic.stypes import Position, Velocity, Direction, Rotating

class TestMove(unittest.TestCase):

    def test_move(self):
        mock_movable = MagicMock(spec=IMovable)

        mock_movable.get_position.return_value = Position([12, 5])
        mock_movable.get_velocity.return_value = Velocity([-7, 3])

        Move(mock_movable).execute()

        # Verify that get_position and get_velocity were called correctly
        mock_movable.get_position.assert_called_once()
        mock_movable.get_velocity.assert_called_once()

        exp_result_position = Position([5, 8])
        mock_movable.set_position.assert_called_once_with(exp_result_position)

    def test_position_unreadable(self):
        mock_movable = MagicMock(spec=IMovable)

        mock_movable.get_position.side_effect = Exception("get_position failed")
        mock_movable.get_velocity.return_value = Velocity([-7, 3])

        move = Move(mock_movable)
        with self.assertRaises(Exception) as context:
            move.execute()
        self.assertIn("get_position failed", str(context.exception.args[0]))

        mock_movable.get_position.assert_called_once()

    def test_velocity_unreadable(self):
        mock_movable = MagicMock(spec=IMovable)

        mock_movable.get_position.return_value = Position([12, 5])
        mock_movable.get_velocity.side_effect = Exception("get_velocity failed")

        move = Move(mock_movable)
        with self.assertRaises(Exception) as context:
            move.execute()

        self.assertIn("get_velocity failed", str(context.exception.args[0]))

        mock_movable.get_velocity.assert_called_once()

    def test_set_position_failed(self):
        mock_movable = MagicMock(spec=IMovable)

        mock_movable.get_position.return_value = Position([12, 5])
        mock_movable.get_velocity.return_value = Velocity([-7, 3])
        mock_movable.set_position.side_effect = Exception("set_position failed")

        with self.assertRaises(Exception) as context:
            Move(mock_movable).execute()

        self.assertIn("set_position failed", str(context.exception.args[0]))

        # Verify that get_position and get_velocity were called correctly
        mock_movable.get_position.assert_called_once()
        mock_movable.get_velocity.assert_called_once()


class TestRotate(unittest.TestCase):

    def test_rotation(self):
        mock_rotable = MagicMock(spec=IRotable)

        mock_rotable.get_direction.return_value = Direction(90)
        mock_rotable.get_rotating.return_value = Rotating(-10)

        rotate = Rotate(mock_rotable)
        rotate.execute()

        mock_rotable.get_direction.assert_called_once()
        mock_rotable.get_rotating.assert_called_once()

        exp_result = Direction(80)
        mock_rotable.set_direction.assert_called_once_with(exp_result)

    def test_direction_failed(self):
        mock_rotable = MagicMock(spec=IRotable)

        mock_rotable.get_direction.side_effect = Exception("get_direction failed")
        mock_rotable.get_rotating.return_value = Rotating(-10)

        rotate = Rotate(mock_rotable)
        with self.assertRaises(Exception) as context:
            rotate.execute()
        self.assertIn("get_direction failed", str(context.exception.args[0]))

        mock_rotable.get_direction.assert_called_once()

    def test_rotating_failed(self):
        mock_rotable = MagicMock(spec=IRotable)

        mock_rotable.get_direction.return_value = Direction(90)
        mock_rotable.get_rotating.side_effect = Exception("get_rotating failed")

        rotate = Rotate(mock_rotable)
        with self.assertRaises(Exception) as context:
            rotate.execute()
        self.assertIn("get_rotating failed", str(context.exception.args[0]))

        mock_rotable.get_rotating.assert_called_once()


    def test_set_direction_failed(self):
        mock_rotable = MagicMock(spec=IRotable)

        mock_rotable.get_direction.return_value = Direction(90)
        mock_rotable.get_rotating.return_value = Rotating(-10)
        mock_rotable.set_direction.side_effect = Exception("set_direction failed")

        rotate = Rotate(mock_rotable)
        with self.assertRaises(Exception) as context:
            rotate.execute()
        self.assertIn("set_direction failed", str(context.exception.args[0]))

        mock_rotable.get_direction.assert_called_once()
        mock_rotable.get_rotating.assert_called_once()


class TestMovableAdapter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_gobject = MagicMock(spec=GObject)
        cls.items = {"position": Position([1,2]),
                     "velocity": Velocity([-3,-4])}
        cls.mock_gobject.__getitem__.side_effect = cls.items.__getitem__
        cls.move_adapter = MovableAdapter(cls.mock_gobject)

    def test_get_position(self):
        p = self.move_adapter.get_position()
        self.assertEqual(p, self.items["position"])

    def test_get_velocity(self):
        v = self.move_adapter.get_velocity()
        self.assertEqual(v, self.items["velocity"])

    def test_set_position(self):
        new_position = Position([0, 1])
        self.move_adapter.set_position(new_position)
        self.mock_gobject.__setitem__.assert_called_once_with('position', new_position)


class TestRotableAdapter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_gobject = MagicMock(spec=GObject)
        cls.items = {"direction": Direction(90),
                     "rotating": Rotating(-30)}
        cls.mock_gobject.__getitem__.side_effect = cls.items.__getitem__
        cls.rotate_adapter = RotableAdapter(cls.mock_gobject)

    def test_get_direction(self):
        d = self.rotate_adapter.get_direction()
        self.assertEqual(d, self.items["direction"])

    def test_get_rotating(self):
        r = self.rotate_adapter.get_rotating()
        self.assertEqual(r, self.items["rotating"])

    def test_set_direction(self):
        new_direction = Direction(60)
        self.rotate_adapter.set_direction(new_direction)
        self.mock_gobject.__setitem__.assert_called_once_with('direction', new_direction)


if __name__ == '__main__':
    unittest.main()
