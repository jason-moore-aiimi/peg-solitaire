import pytest
from game.position import Position

from console_app.position_parser import PositionParser
from console_app.unparsable_position_error import UnparsablePositionError


@pytest.mark.parametrize(
    "separator,input,expected",
    [
        (",", "1,0", Position(1, 0)),
        (",", "10,9", Position(10, 9)),
        (",", " 20 , 4 ", Position(20, 4)),
        (":", "20:4", Position(20, 4)),
    ],
)
def test_position_is_parsed_correctly(
    separator: str, input: str, expected: Position
) -> None:
    position_parser = PositionParser(separator)

    assert position_parser.parse(input) == expected


@pytest.mark.parametrize(
    "separator,input",
    [
        (",", "x,0"),
        (",", "0,y"),
        (",", "x,y"),
        (",", "0:0"),
    ],
)
def test_parse_raises_unparsable_position_error(separator: str, input: str) -> None:
    position_parser = PositionParser(separator)

    with pytest.raises(UnparsablePositionError):
        position_parser.parse(input)
