import pytest

from game.empty import Empty
from game.grid import Grid
from game.invalid_move_error import InvalidMoveError
from game.move import Move
from game.peg import Peg
from game.peg_solitaire import PegSolitaire
from game.position import Position
from game.square import Square


@pytest.fixture
def position_squares() -> dict[Position, Square]:
    return {
        Position(0, 0): Peg(),
        Position(1, 0): Peg(),
        Position(2, 0): Empty(),
        Position(3, 0): Peg(),
        Position(4, 0): Empty(),
        Position(5, 0): Peg(),
        Position(6, 0): Empty(),
        Position(7, 0): Peg(),
        Position(8, 0): Empty(),
        Position(9, 0): Peg(),
        Position(10, 0): Empty(),
        Position(11, 0): Peg(),
        Position(12, 0): Empty(),
        Position(12, 1): Empty(),
    }


@pytest.fixture
def peg_solitaire(position_squares: dict[Position, Square]) -> PegSolitaire:
    return create_peg_solitaire(position_squares)


@pytest.fixture
def grid(position_squares: dict[Position, Square]) -> Grid:
    return create_grid(position_squares)


@pytest.mark.parametrize(
    "current_position,new_position,position_squares,expected",
    [
        (
            Position(0, 0),
            Position(2, 0),
            {Position(0, 0): Peg(), Position(1, 0): Peg(), Position(2, 0): Empty()},
            ((Empty(), Empty(), Peg()),),
        ),
        (
            Position(2, 0),
            Position(0, 0),
            {Position(0, 0): Empty(), Position(1, 0): Peg(), Position(2, 0): Peg()},
            ((Peg(), Empty(), Empty()),),
        ),
        (
            Position(0, 0),
            Position(0, 2),
            {Position(0, 0): Peg(), Position(0, 1): Peg(), Position(0, 2): Empty()},
            ((Empty(),), (Empty(),), (Peg(),)),
        ),
        (
            Position(0, 2),
            Position(0, 0),
            {Position(0, 0): Empty(), Position(0, 1): Peg(), Position(0, 2): Peg()},
            ((Peg(),), (Empty(),), (Empty(),)),
        ),
    ],
)
def test_move_updates_the_grid_if_move_is_valid(
    current_position: Position,
    new_position: Position,
    position_squares: dict[Position, Square],
    expected: tuple[tuple[Square | None, ...]],
) -> None:
    peg_solitaire = create_peg_solitaire(position_squares)

    peg_solitaire.move(current_position, new_position)

    assert peg_solitaire.view() == expected


def test_move_does_not_update_the_grid_if_move_is_invalid() -> None:
    position_squares = {
        Position(0, 0): Peg(),
        Position(1, 0): Peg(),
        Position(2, 0): Empty(),
    }
    peg_solitaire = create_peg_solitaire(position_squares)

    with pytest.raises(InvalidMoveError):
        peg_solitaire.move(Position(0, 0), Position(0, 2))


@pytest.mark.parametrize(
    "position_squares,expected",
    [
        (
            {
                Position(0, 0): Empty(),
                Position(1, 0): Peg(),
                Position(2, 0): Empty(),
            },
            True,
        ),
        (
            {
                Position(0, 0): Peg(),
                Position(1, 0): Peg(),
                Position(2, 0): Empty(),
            },
            False,
        ),
        (
            {
                Position(0, 0): Peg(),
                Position(1, 0): Empty(),
                Position(2, 0): Peg(),
            },
            True,
        ),
    ],
)
def test_is_complete_returns_the_correct_value(
    position_squares: dict[Position, Square], expected: bool
) -> None:
    peg_solitaire = create_peg_solitaire(position_squares)

    assert peg_solitaire.is_complete == expected


@pytest.mark.parametrize(
    "position_squares,expected",
    [
        (
            {
                Position(0, 0): Empty(),
                Position(1, 0): Peg(),
                Position(2, 0): Empty(),
            },
            True,
        ),
        (
            {
                Position(0, 0): Peg(),
                Position(1, 0): Peg(),
                Position(2, 0): Empty(),
            },
            False,
        ),
        (
            {
                Position(0, 0): Peg(),
                Position(1, 0): Empty(),
                Position(2, 0): Peg(),
            },
            False,
        ),
    ],
)
def test_is_won_returns_the_correct_value(
    position_squares: dict[Position, Square], expected: bool
) -> None:
    peg_solitaire = create_peg_solitaire(position_squares)

    assert peg_solitaire.is_won == expected


@pytest.mark.parametrize("number_of_moves", [(1), (2), (3), (4), (5), (6)])
def test_when_valid_moves_are_made_they_are_returned_by_moves(
    number_of_moves: int, peg_solitaire: PegSolitaire
) -> None:
    moves = create_moves(number_of_moves)

    for move in moves:
        peg_solitaire.move(move.current_position, move.new_position)

    assert peg_solitaire.moves == moves


def test_invalid_move_is_not_added_to_moves(peg_solitaire: PegSolitaire) -> None:
    with pytest.raises(InvalidMoveError):
        peg_solitaire.move(Position(1, 0), Position(3, 0))

    assert peg_solitaire.moves == tuple()


def test_peg_solitaire_with_the_same_grid_and_moves_are_equal(
    peg_solitaire: PegSolitaire, grid: Grid
) -> None:
    assert peg_solitaire == PegSolitaire(grid)


def test_peg_solitaire_with_the_same_grid_and_different_moves_are_not_equal(
    peg_solitaire: PegSolitaire, grid: Grid
) -> None:
    peg_solitaire.move(Position(0, 0), Position(2, 0))
    assert not peg_solitaire == PegSolitaire(grid)


def test_peg_solitaire_with_different_grid_and_same_moves_are_not_equal(
    peg_solitaire: PegSolitaire,
) -> None:
    position_squares = {
        Position(0, 0): Peg(),
        Position(1, 0): Peg(),
        Position(2, 0): Empty(),
    }
    assert not peg_solitaire == create_peg_solitaire(position_squares)


def test_peg_solitaire_with_different_grid_and_different_moves_are_not_equal(
    peg_solitaire: PegSolitaire,
) -> None:
    peg_solitaire.move(Position(0, 0), Position(2, 0))
    position_squares = {
        Position(0, 0): Peg(),
        Position(1, 0): Peg(),
        Position(2, 0): Empty(),
    }
    assert not peg_solitaire == create_peg_solitaire(position_squares)


def test_view_returns_the_correct_tuple() -> None:
    position_squares = {
        Position(0, 0): Peg(),
        Position(1, 0): Empty(),
        Position(2, 0): Peg(),
        Position(0, 1): Empty(),
        Position(1, 1): Peg(),
        Position(2, 1): Empty(),
        Position(0, 2): Peg(),
        Position(1, 2): Empty(),
        Position(2, 2): Peg(),
    }
    peg_solitaire = create_peg_solitaire(position_squares)

    expected = (
        (Peg(), Empty(), Peg()),
        (Empty(), Peg(), Empty()),
        (Peg(), Empty(), Peg()),
    )
    assert peg_solitaire.view() == expected


@pytest.mark.parametrize(
    "position,expected",
    [(Position(0, 0), True), (Position(2, 0), False), (Position(0, 1), False)],
)
def test_is_peg_returns_correct_result(
    position: Position, expected: bool, peg_solitaire: PegSolitaire
) -> None:
    assert peg_solitaire.is_peg(position) == expected


@pytest.mark.parametrize(
    "position,expected",
    [(Position(0, 0), False), (Position(2, 0), True), (Position(0, 1), False)],
)
def test_is_empty_returns_correct_result(
    position: Position, expected: bool, peg_solitaire: PegSolitaire
) -> None:
    assert peg_solitaire.is_empty(position) == expected


def create_moves(number_of_moves) -> tuple[Move, ...]:
    return tuple(
        Move(Position(move, 0), Position(move + 2, 0))
        for move in range(0, number_of_moves * 2, 2)
    )


def create_peg_solitaire(position_squares) -> PegSolitaire:
    grid = create_grid(position_squares)
    return PegSolitaire(grid)


def create_grid(position_squares):
    return Grid(position_squares=position_squares)
