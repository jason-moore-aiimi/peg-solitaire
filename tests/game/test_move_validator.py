import pytest

from game.empty import Empty
from game.grid import Grid
from game.move import Move
from game.move_validator import MoveValidator
from game.peg import Peg
from game.position import Position


@pytest.mark.parametrize(
    "move,expected",
    [
        # middle peg valid moves
        (Move(Position(3, 3), Position(1, 3)), True),
        (Move(Position(3, 3), Position(5, 3)), True),
        (Move(Position(3, 3), Position(3, 5)), True),
        (Move(Position(3, 3), Position(3, 1)), True),
        # middle peg invalid moves
        (Move(Position(3, 3), Position(1, 1)), False),
        (Move(Position(3, 3), Position(5, 1)), False),
        (Move(Position(3, 3), Position(5, 5)), False),
        (Move(Position(3, 3), Position(1, 5)), False),
        # neighbour moves to empty space
        (Move(Position(3, 2), Position(3, 1)), False),
        (Move(Position(4, 3), Position(5, 3)), False),
        (Move(Position(3, 4), Position(3, 5)), False),
        (Move(Position(2, 3), Position(1, 3)), False),
        # moves to peg
        (Move(Position(2, 2), Position(2, 4)), False),
        (Move(Position(4, 2), Position(2, 2)), False),
        (Move(Position(4, 4), Position(2, 4)), False),
        (Move(Position(2, 4), Position(4, 4)), False),
        # current position doesn't contain peg
        (Move(Position(1, 1), Position(4, 4)), False),
        # current position == new position
        (Move(Position(2, 2), Position(2, 2)), False),
        # current position is out of grid
        (Move(Position(0, 0), Position(4, 4)), False),
        # new position is out of grid
        (Move(Position(2, 2), Position(2, 0)), False),
        (Move(Position(4, 4), Position(4, 6)), False),
        # move is greater than next door but 1 neighbour
        (Move(Position(2, 2), Position(2, 5)), False),
    ],
)
def test_correct_result_is_returned_for_moves(move: Move, expected: bool) -> None:
    position_squares = {
        Position(1, 1): Empty(),
        Position(2, 1): Empty(),
        Position(3, 1): Empty(),
        Position(4, 1): Empty(),
        Position(5, 1): Empty(),
        Position(1, 2): Empty(),
        Position(2, 2): Peg(),
        Position(3, 2): Peg(),
        Position(4, 2): Peg(),
        Position(5, 2): Empty(),
        Position(1, 3): Empty(),
        Position(2, 3): Peg(),
        Position(3, 3): Peg(),
        Position(4, 3): Peg(),
        Position(5, 3): Empty(),
        Position(1, 4): Empty(),
        Position(2, 4): Peg(),
        Position(3, 4): Peg(),
        Position(4, 4): Peg(),
        Position(5, 4): Empty(),
        Position(1, 5): Empty(),
        Position(2, 5): Empty(),
        Position(3, 5): Empty(),
        Position(4, 5): Empty(),
        Position(5, 5): Empty(),
    }
    grid = Grid(position_squares=position_squares)
    move_validator = MoveValidator(grid)

    assert move_validator.validate(move) == expected
