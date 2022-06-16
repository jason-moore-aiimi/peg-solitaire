import pytest

from game.position import Position


@pytest.fixture
def x() -> int:
    return 6


@pytest.fixture
def y() -> int:
    return 7


def test_positions_with_different_x_values_return_false(y: int) -> None:
    position1 = Position(5, y)
    position2 = Position(10, y)

    assert not position1 == position2


def test_positions_with_the_same_x_and_y_values_return_false(x: int, y: int) -> None:
    position1 = Position(x, y)
    position2 = Position(x, y)

    assert position1 == position2


def test_positions_with_different_y_values_return_false(x: int) -> None:
    position1 = Position(x, 5)
    position2 = Position(x, 10)

    assert not position1 == position2


def test_hash_returns_the_hash_of_xy(x: int, y: int) -> None:
    position = Position(x, y)

    assert position.__hash__() == hash(f"{x}{y}")


@pytest.mark.parametrize(
    "position1,position2,expected",
    [
        (Position(1, 1), Position(5, 1), True),
        (Position(1, 1), Position(1, 5), True),
        (Position(1, 1), Position(5, 5), True),
        (Position(2, 4), Position(3, 1), True),
        (Position(-1, -1), Position(1, 1), True),
        (Position(5, 1), Position(1, 1), False),
        (Position(1, 5), Position(1, 1), False),
        (Position(5, 5), Position(1, 1), False),
        (Position(1, 1), Position(1, 1), False),
    ],
)
def test_position_is_less_than_other_position(
    position1: Position, position2: Position, expected: bool
) -> None:
    assert (position1 < position2) == expected


def test_positions_are_ordered_correctly() -> None:
    unordered = [
        Position(1, 2),
        Position(1, 3),
        Position(2, 3),
        Position(1, 1),
        Position(3, 3),
        Position(2, 1),
        Position(3, 2),
        Position(2, 2),
        Position(3, 1),
    ]

    ordered = [
        Position(1, 1),
        Position(1, 2),
        Position(1, 3),
        Position(2, 1),
        Position(2, 2),
        Position(2, 3),
        Position(3, 1),
        Position(3, 2),
        Position(3, 3),
    ]
    assert sorted(unordered) == ordered


def test_positions_added_together_returns_correct_position() -> None:
    position1 = Position(5, 4)
    position2 = Position(11, 9)

    assert position1 + position2 == Position(16, 13)


def test_positions_subtracted_together_returns_correct_position() -> None:
    position1 = Position(5, 4)
    position2 = Position(11, 9)

    assert position2 - position1 == Position(6, 5)


@pytest.mark.parametrize("x, y", [(1, 1), (6, 9), (6, 1), (1, 9)])
def test_position_converts_to_string_correctly(x: int, y: int) -> None:
    assert f"{Position(x, y)}" == f"({x}, {y})"
