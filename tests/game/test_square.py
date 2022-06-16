import pytest

from game.square import Square


@pytest.mark.parametrize(
    "square,expected", [(Square(False), False), (Square(True), True)]
)
def test_square_converts_to_bool_correctly(square, expected):
    assert bool(square) == expected
