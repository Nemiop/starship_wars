import coverage
import unittest
from unittest.mock import MagicMock

from GameServer.entities.GObject import GObject
from GameServer.mechanics.Move import  IMovable, Move
from GameServer.mechanics.Rotate import  IRotable, Rotate
from GameServer.basic.stypes import Position, Velocity, Direction, Rotating


# Complexity Level #2:
# + 5. Реализован тест: Для объекта, находящегося в точке (12, 5) и движущегося со скоростью (-7, 3) движение меняет положение объекта на (5, 8)
# + 6. Реализован тест: Попытка сдвинуть объект, у которого невозможно прочитать положение объекта в пространстве,, приводит к ошибке
# + 7. Реализован тест: Попытка сдвинуть объект, у которого невозможно прочитать значение мгновенной скорости, приводит к ошибке
# + 8. Реализован тест: Попытка сдвинуть объект, у которого невозможно изменить положение в пространстве, приводит к ошибке
# + 9. Все тесты успешно выполняются

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


# Complexity Level #3:
# + 1. Реализованы тесты для поворота корабля вокруг собственной оси.
# 2. Настроен расчет покрытия кода тестами.
# 3. Настроен CI, который умеет собирать проект и прогонять тесты, вычислять покрытие кода тестами.
# 4. Покрытие кода тестами 100%.
# 5. Пайплайн “зеленый”

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

    def test_get_position(self):
        mock_gobject = MagicMock(spec=GObject)



if __name__ == '__main__':
    unittest.main()
