import pytest
from game.empty import Empty
from game.peg import Peg
from game.square import Square

from console_app.element_factory import ElementFactory

PEG = "X"
EMPTY = "O"
BLANK = "  "


@pytest.fixture
def element_factory() -> ElementFactory:
    return ElementFactory(PEG, EMPTY, BLANK)


@pytest.mark.parametrize(
    "value,expected", [(Peg(), PEG), (Empty(), EMPTY), (None, BLANK)]
)
def test_element_factory_returns_correct_string(
    value: Square | None, expected: str, element_factory: ElementFactory
):
    assert element_factory.get_element(value) == expected
