from abc import abstractmethod
from .position import Position
from .square import Square
from .peg_solitaire import PegSolitaire
from .grid import Grid


class PegSolitaireFactory:
    @abstractmethod
    def _get_position_squares(self) -> dict[Position, Square]:
        pass

    def create(self) -> PegSolitaire:
        position_squares = self._get_position_squares()
        grid = Grid(position_squares)
        return PegSolitaire(grid)
