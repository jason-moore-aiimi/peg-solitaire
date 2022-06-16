from game.move import Move
from game.position import Position
from game.relative_move import RelativeMove


def test_relative_move_is_created_correctly():
    position = Position(5, 5)
    relative_position = Position(2, 5)

    expected = Move(position, Position(7, 10))
    assert RelativeMove(position, relative_position) == expected
