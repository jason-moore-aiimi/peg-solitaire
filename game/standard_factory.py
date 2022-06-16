from .empty import Empty
from .peg import Peg
from .position import Position
from .square import Square
from .peg_solitaire_factory import PegSolitaireFactory


class StandardFactory(PegSolitaireFactory):
    def _get_position_squares(self) -> dict[Position, Square]:
        return {
            Position(2, 0): Peg(),
            Position(3, 0): Peg(),
            Position(4, 0): Peg(),
            Position(2, 1): Peg(),
            Position(3, 1): Peg(),
            Position(4, 1): Peg(),
            Position(0, 2): Peg(),
            Position(1, 2): Peg(),
            Position(2, 2): Peg(),
            Position(3, 2): Peg(),
            Position(4, 2): Peg(),
            Position(5, 2): Peg(),
            Position(6, 2): Peg(),
            Position(0, 3): Peg(),
            Position(1, 3): Peg(),
            Position(2, 3): Peg(),
            Position(3, 3): Empty(),
            Position(4, 3): Peg(),
            Position(5, 3): Peg(),
            Position(6, 3): Peg(),
            Position(0, 4): Peg(),
            Position(1, 4): Peg(),
            Position(2, 4): Peg(),
            Position(3, 4): Peg(),
            Position(4, 4): Peg(),
            Position(5, 4): Peg(),
            Position(6, 4): Peg(),
            Position(2, 5): Peg(),
            Position(3, 5): Peg(),
            Position(4, 5): Peg(),
            Position(2, 6): Peg(),
            Position(3, 6): Peg(),
            Position(4, 6): Peg(),
        }
