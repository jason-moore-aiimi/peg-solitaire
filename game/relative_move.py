from .position import Position
from .move import Move


class RelativeMove(Move):
    def __init__(self, peg_position: Position, relative_position: Position) -> None:
        final_position = peg_position + relative_position
        super().__init__(peg_position, final_position)
