import pytest

from game.move import Move
from game.position import Position


@pytest.fixture
def position1() -> Position:
    return Position(5, 8)


@pytest.fixture
def position2() -> Position:
    return Position(7, 6)


@pytest.fixture
def position3() -> Position:
    return Position(10, 11)


@pytest.fixture
def move12(position1: Position, position2: Position) -> Move:
    return Move(position1, position2)


@pytest.fixture
def move32(position3: Position, position2: Position) -> Move:
    return Move(position3, position2)


@pytest.fixture
def move23(position2: Position, position3: Position) -> Move:
    return Move(position2, position3)


@pytest.fixture
def move33(position3: Position) -> Move:
    return Move(position3, position3)


def test_moves_are_equal(
    move12: Move, position1: Position, position2: Position
) -> None:
    assert move12 == Move(position1, position2)


def test_moves_with_different_current_positions_are_not_equal(
    move12: Move, move32: Move
) -> None:
    assert not move12 == move32


def test_moves_with_different_new_positions_are_not_equal(
    move12: Move, move23: Move
) -> None:
    assert not move12 == move23


def test_moves_with_different_new_and_current_positions_are_not_equal(
    move12: Move, move33: Move
) -> None:
    assert not move12 == move33


@pytest.mark.parametrize(
    "move1,move2,expected",
    [
        (
            Move(Position(1, 1), Position(1, 1)),
            Move(Position(2, 2), Position(2, 2)),
            True,
        ),
        (
            Move(Position(1, 1), Position(-1, -1)),
            Move(Position(1, 1), Position(1, 1)),
            True,
        ),
        (
            Move(Position(2, 1), Position(1, 1)),
            Move(Position(2, 2), Position(2, 2)),
            True,
        ),
        (
            Move(Position(1, 1), Position(2, 2)),
            Move(Position(2, 2), Position(2, 2)),
            True,
        ),
        (
            Move(Position(1, 1), Position(1, 1)),
            Move(Position(1, 1), Position(1, 1)),
            False,
        ),
        (
            Move(Position(3, 3), Position(1, 1)),
            Move(Position(1, 1), Position(1, 1)),
            False,
        ),
        (
            Move(Position(1, 1), Position(3, 3)),
            Move(Position(1, 1), Position(1, 1)),
            False,
        ),
        (
            Move(Position(3, 3), Position(3, 3)),
            Move(Position(1, 1), Position(1, 1)),
            False,
        ),
        (
            Move(Position(2, 3), Position(-1, -5)),
            Move(Position(1, 1), Position(-1, -1)),
            False,
        ),
        (
            Move(Position(2, 4), Position(9, 10)),
            Move(Position(3, 1), Position(2, 1)),
            True,
        ),
    ],
)
def test_move_is_less_than_move(move1: Move, move2: Move, expected: bool) -> None:
    assert (move1 < move2) == expected


def test_moves_are_sorted_by_current_position_then_new_position() -> None:
    moves = [
        Move(Position(1, 1), Position(1, 1)),
        Move(Position(1, 1), Position(-1, -1)),
        Move(Position(2, 3), Position(-1, -5)),
        Move(Position(2, 4), Position(1, 1)),
        Move(Position(2, 3), Position(10, 11)),
        Move(Position(1, 1), Position(2, 2)),
        Move(Position(2, 3), Position(6, 4)),
        Move(Position(3, 1), Position(2, 10)),
        Move(Position(3, 1), Position(2, 3)),
        Move(Position(2, 4), Position(-1, -1)),
        Move(Position(2, 4), Position(9, 10)),
        Move(Position(3, 1), Position(2, 1)),
    ]

    expected = [
        Move(Position(1, 1), Position(-1, -1)),
        Move(Position(1, 1), Position(1, 1)),
        Move(Position(1, 1), Position(2, 2)),
        Move(Position(2, 3), Position(-1, -5)),
        Move(Position(2, 3), Position(6, 4)),
        Move(Position(2, 3), Position(10, 11)),
        Move(Position(2, 4), Position(-1, -1)),
        Move(Position(2, 4), Position(1, 1)),
        Move(Position(2, 4), Position(9, 10)),
        Move(Position(3, 1), Position(2, 1)),
        Move(Position(3, 1), Position(2, 3)),
        Move(Position(3, 1), Position(2, 10)),
    ]
    assert sorted(moves) == expected


@pytest.mark.parametrize(
    "current_position,new_position,expected",
    [
        (
            Position(0, 0),
            Position(0, 4),
            (
                Position(0, 0),
                Position(0, 1),
                Position(0, 2),
                Position(0, 3),
                Position(0, 4),
            ),
        ),
        (
            Position(0, 0),
            Position(0, -4),
            (
                Position(0, 0),
                Position(0, -1),
                Position(0, -2),
                Position(0, -3),
                Position(0, -4),
            ),
        ),
        (
            Position(0, 0),
            Position(4, 0),
            (
                Position(0, 0),
                Position(1, 0),
                Position(2, 0),
                Position(3, 0),
                Position(4, 0),
            ),
        ),
        (
            Position(0, 0),
            Position(-4, 0),
            (
                Position(0, 0),
                Position(-1, 0),
                Position(-2, 0),
                Position(-3, 0),
                Position(-4, 0),
            ),
        ),
        (Position(0, 0), Position(4, 4), (Position(0, 0), Position(4, 4))),
        (Position(0, 0), Position(4, -4), (Position(0, 0), Position(4, -4))),
        (Position(0, 0), Position(4, -4), (Position(0, 0), Position(4, -4))),
        (Position(0, 0), Position(-4, -4), (Position(0, 0), Position(-4, -4))),
    ],
)
def test_positions_returns_the_correct_positions_for_the_move(
    current_position: Position, new_position: Position, expected: tuple[Position, ...]
) -> None:
    move = Move(current_position, new_position)

    assert move.positions == expected


@pytest.mark.parametrize(
    "current_position,new_position",
    [
        (Position(1, 1), Position(1, 1)),
        (Position(2, 1), Position(1, 1)),
        (Position(1, 2), Position(1, 1)),
        (Position(1, 1), Position(2, 1)),
        (Position(1, 1), Position(1, 2)),
        (Position(6, 9), Position(1, 1)),
        (Position(1, 1), Position(6, 9)),
    ],
)
def test_move_is_converted_to_string_properly(
    current_position: Position, new_position: Position
) -> None:
    assert (
        f"{Move(current_position, new_position)}"
        == f"{current_position} -> {new_position}"
    )
