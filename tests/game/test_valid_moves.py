import pytest

from game.empty import Empty
from game.grid import Grid
from game.move import Move
from game.peg import Peg
from game.position import Position
from game.square import Square
from game.valid_moves import ValidMoves


@pytest.fixture
def valid_moves(grid: Grid) -> ValidMoves:
    return ValidMoves(grid)


@pytest.fixture
def grid(position_squares: dict[Position, Square]) -> Grid:
    return Grid(position_squares=position_squares)


@pytest.fixture
def position_squares():
    return {
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


def test_index_operator_returns_all_valid_moves(valid_moves: ValidMoves) -> None:
    expected = (
        Move(Position(2, 3), Position(2, 1)),
        Move(Position(2, 3), Position(2, 5)),
        Move(Position(3, 2), Position(1, 2)),
        Move(Position(3, 2), Position(5, 2)),
        Move(Position(3, 3), Position(1, 3)),
        Move(Position(3, 3), Position(3, 1)),
        Move(Position(3, 3), Position(3, 5)),
        Move(Position(3, 3), Position(5, 3)),
        Move(Position(3, 4), Position(1, 4)),
        Move(Position(3, 4), Position(5, 4)),
        Move(Position(4, 3), Position(4, 1)),
        Move(Position(4, 3), Position(4, 5)),
    )
    assert valid_moves[:] == expected


def test_index_operator_returns_all_valid_moves_in_range(
    valid_moves: ValidMoves,
) -> None:
    expected = (
        Move(Position(3, 3), Position(3, 1)),
        Move(Position(3, 3), Position(3, 5)),
        Move(Position(3, 3), Position(5, 3)),
        Move(Position(3, 4), Position(1, 4)),
        Move(Position(3, 4), Position(5, 4)),
        Move(Position(4, 3), Position(4, 1)),
        Move(Position(4, 3), Position(4, 5)),
    )
    assert valid_moves[5:] == expected


def test_index_operator_returns_valid_move_at_index(valid_moves: ValidMoves) -> None:
    assert valid_moves[5] == Move(Position(3, 3), Position(3, 1))


def test_len_returns_the_correct_number_of_valid_moves(valid_moves: ValidMoves) -> None:
    assert len(valid_moves) == 12


def test_valid_moves_are_equal_when_constructed_from_the_same_squares_and_relative_positions(
    valid_moves: ValidMoves, grid: Grid
) -> None:
    assert valid_moves == ValidMoves(grid)


def test_valid_moves_are_not_equal_when_constructed_from_the_same_squares_and_different_relative_positions(
    valid_moves: ValidMoves, grid: Grid
) -> None:
    assert not valid_moves == ValidMoves(grid, (Position(1, 1),))


def test_valid_moves_are_not_equal_when_constructed_from_differnet_squares_and_same_relative_positions(
    valid_moves: ValidMoves,
) -> None:
    grid = Grid(position_squares={Position(1, 1): Empty(), Position(2, 2): Peg()})
    assert not valid_moves == ValidMoves(grid)


def test_valid_moves_are_not_equal_when_constructed_from_differnet_squares_and_different_relative_positions(
    valid_moves: ValidMoves,
) -> None:
    grid = Grid(position_squares={Position(1, 1): Empty(), Position(2, 2): Peg()})
    assert not valid_moves == ValidMoves(grid, (Position(1, 1),))


@pytest.mark.parametrize(
    "move,expected",
    [
        (Move(Position(3, 3), Position(1, 3)), True),
        (Move(Position(3, 3), Position(3, 1)), True),
        (Move(Position(3, 3), Position(3, 5)), True),
        (Move(Position(3, 3), Position(5, 3)), True),
        (Move(Position(3, 3), Position(3, 3)), False),
        (Move(Position(3, 3), Position(6, 6)), False),
    ],
)
def test_contains_returns_correct_value(
    valid_moves: ValidMoves, move: Move, expected: bool
) -> None:
    assert (move in valid_moves) == expected
