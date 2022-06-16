from game import Position
from .unparsable_position_error import UnparsablePositionError


class PositionParser:
    def __init__(self, separator: str = ",") -> None:
        self.separator = separator

    def parse(self, input: str) -> Position:
        try:
            x, y = input.split(self.separator)
            return Position(int(x), int(y))
        except (ValueError):
            raise UnparsablePositionError(input)
