from game.empty import Empty
from game.peg import Peg


def test_peg_converts_to_true():
    assert bool(Peg())


def test_peg_is_equal_to_peg() -> None:
    assert Peg() == Peg()


def test_peg_is_not_equal_empty() -> None:
    assert not Peg() == Empty()
