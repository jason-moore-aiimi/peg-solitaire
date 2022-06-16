import pytest

from game.empty import Empty
from game.grid import Grid
from game.peg import Peg
from game.position import Position
from game.square import Square


@pytest.fixture
def position_squares():
    return {
        Position(1, 0): Peg(),
        Position(0, 1): Peg(),
        Position(1, 1): Empty(),
        Position(2, 1): Peg(),
        Position(1, 2): Peg(),
    }


@pytest.fixture
def grid(position_squares: dict[Position, Square]) -> Grid:
    return Grid(position_squares=position_squares)


def test_peg_positions_returns_a_tuple_of_correct_positions(grid: Grid) -> None:
    expected = (Position(1, 0), Position(0, 1), Position(2, 1), Position(1, 2))
    assert grid.peg_positions == expected


def test_empty_positions_returns_a_tuple_of_correct_positions(grid: Grid) -> None:
    expected = (Position(1, 1),)
    assert grid.empty_positions == expected


def test_remaining_pegs_returns_the_correct_value(grid: Grid) -> None:
    assert grid.peg_count == 4


def test_grids_made_from_equal_squares_are_equal(
    grid: Grid, position_squares: dict[Position, Square]
) -> None:
    assert grid == Grid(position_squares)


def test_grids_made_from_none_equal_squares_are_not_equal(grid: Grid) -> None:
    position_squares = {
        Position(0, 1): Peg(),
        Position(1, 1): Empty(),
        Position(2, 1): Peg(),
        Position(1, 2): Peg(),
    }
    assert not grid == Grid(position_squares)


@pytest.mark.parametrize(
    "position,square,expected",
    [
        (
            Position(1, 0),
            Empty(),
            Grid(
                position_squares={
                    Position(1, 0): Empty(),
                    Position(0, 1): Peg(),
                    Position(1, 1): Empty(),
                    Position(2, 1): Peg(),
                    Position(1, 2): Peg(),
                }
            ),
        ),
        (
            Position(1, 1),
            Peg(),
            Grid(
                position_squares={
                    Position(1, 0): Peg(),
                    Position(0, 1): Peg(),
                    Position(1, 1): Peg(),
                    Position(2, 1): Peg(),
                    Position(1, 2): Peg(),
                }
            ),
        ),
    ],
)
def test_set_item_sets_the_squares_in_grid(
    grid: Grid,
    position: Position,
    square: Square,
    expected: Grid,
) -> None:
    grid[position] = square

    assert grid == expected


@pytest.mark.parametrize(
    "position,square,expected",
    [
        (Position(1, 0), Empty(), 3),
        (Position(1, 1), Peg(), 5),
    ],
)
def test_set_item_updates_the_remaining_pegs(
    grid: Grid,
    position: Position,
    square: Square,
    expected: int,
) -> None:
    grid[position] = square

    assert grid.peg_count == expected


@pytest.mark.parametrize(
    "position,expected",
    [(Position(1, 1), Empty()), (Position(1, 0), Peg()), (Position(0, 0), None)],
)
def test_index_operator_returns_correct_square(
    position: Position, expected: Square | None, grid: Grid
):
    assert grid[position] == expected


def test_iter_returns_a_tuple_each_row(grid: Grid) -> None:
    expected = ((None, Peg(), None), (Peg(), Empty(), Peg()), (None, Peg(), None))
    assert tuple(square for square in grid) == expected
