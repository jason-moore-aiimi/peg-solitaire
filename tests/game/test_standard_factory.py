from game.empty import Empty
from game.peg import Peg
from game.standard_factory import StandardFactory


def test_create_returns_correct_board() -> None:
    standard_factory = StandardFactory()
    peg_solitare = standard_factory.create()

    expected = (
        (None, None, Peg(), Peg(), Peg(), None, None),
        (None, None, Peg(), Peg(), Peg(), None, None),
        (Peg(), Peg(), Peg(), Peg(), Peg(), Peg(), Peg()),
        (Peg(), Peg(), Peg(), Empty(), Peg(), Peg(), Peg()),
        (Peg(), Peg(), Peg(), Peg(), Peg(), Peg(), Peg()),
        (None, None, Peg(), Peg(), Peg(), None, None),
        (None, None, Peg(), Peg(), Peg(), None, None),
    )
    assert peg_solitare.view() == expected
