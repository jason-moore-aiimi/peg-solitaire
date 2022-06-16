import pytest
from game.empty import Empty
from game.peg import Peg

from console_app.element_factory import ElementFactory
from console_app.row_factory import RowFactory


def test_get_row_returns_the_correct_string() -> None:
    peg = "X"
    square = "O"
    empty = "  "
    border = "|"
    element_factory = ElementFactory(peg, square, empty)
    row_factory = RowFactory(element_factory, border)
    row = (None, None, Peg(), Empty(), Peg(), None, Peg())

    expected: str = f"{empty}{empty}{border}{peg}{border}{square}{border}{peg}{border}{empty}{border}{peg}{border}"
    assert row_factory.get_row(row) == expected


@pytest.mark.parametrize(
    "row_length,border,expected",
    [(8, "|", "  0 1 2 3 4 5 6 7"), (8, "|||", "    0   1   2   3   4   5   6   7")],
)
def test_get_columns_returns_the_correct_string(
    row_length: int, border: str, expected: str
) -> None:
    element_factory = ElementFactory()
    row_factory = RowFactory(element_factory, border)

    assert row_factory.get_columns(row_length) == expected
