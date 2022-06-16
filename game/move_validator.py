from .grid import Grid
from .empty import Empty
from .peg import Peg
from .square import Square
from .move import Move


class MoveValidator:
    def __init__(
        self,
        grid: Grid,
        valid_moves: tuple[tuple[Square, ...], ...] = (
            (Peg(), Peg(), Empty()),
            (Empty(), Peg(), Peg()),
        ),
    ) -> None:
        self.__grid = grid
        self.__valid_moves = valid_moves

    def validate(self, move: Move) -> bool:
        move_squares = tuple(self.__grid[position] for position in move.positions)
        return move_squares in self.__valid_moves
