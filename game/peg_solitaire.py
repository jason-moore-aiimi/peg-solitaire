from .square import Square
from .valid_moves import ValidMoves
from .empty import Empty
from .invalid_move_error import InvalidMoveError
from .move import Move
from .peg import Peg
from .position import Position
from .grid import Grid


class PegSolitaire:
    def __init__(self, grid: Grid) -> None:
        self.__grid = grid
        self.__valid_moves = ValidMoves(grid)
        self.__moves: list[Move] = []

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PegSolitaire):
            return self.moves == __o.moves and self.__grid == __o.__grid
        return False

    def move(self, current_position: Position, new_position: Position) -> None:
        move = Move(current_position, new_position)
        if move in self.__valid_moves:
            self.__set_positions(move)
            self.__valid_moves = ValidMoves(self.__grid)
            self.__moves.append(move)
        else:
            raise InvalidMoveError(move)

    def view(self) -> tuple[tuple[Square | None, ...], ...]:
        return tuple(square for square in self.__grid)

    def is_peg(self, position: Position) -> bool:
        return position in self.__grid.peg_positions

    def is_empty(self, position: Position) -> bool:
        return position in self.__grid.empty_positions

    @property
    def is_complete(self) -> bool:
        return len(self.__valid_moves) == 0

    @property
    def is_won(self) -> bool:
        return self.__grid.peg_count == 1

    @property
    def moves(self) -> tuple[Move, ...]:
        return tuple(self.__moves)

    def __set_positions(self, move):
        for position in move.positions:
            if position != move.new_position:
                self.__grid[position] = Empty()
            else:
                self.__grid[position] = Peg()
