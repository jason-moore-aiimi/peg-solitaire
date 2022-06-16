from game.empty import Empty
from game.peg import Peg


def test_empty_converts_to_false() -> None:
    assert not bool(Empty())


def test_empty_is_equal_to_empty() -> None:
    assert Empty() == Empty()


def test_empty_is_not_equal_peg() -> None:
    assert not Empty() == Peg()
