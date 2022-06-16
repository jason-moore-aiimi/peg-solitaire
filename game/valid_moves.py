from .grid import Grid
from .position import Position
from .move import Move
from .relative_move import RelativeMove
from .move_validator import MoveValidator


class ValidMoves:
    def __init__(
        self,
        grid: Grid,
        relative_positions: tuple[Position, ...] = (
            Position(2, 0),
            Position(-2, 0),
            Position(0, 2),
            Position(0, -2),
        ),
    ) -> None:
        self.__grid = grid
        self.__move_validator = MoveValidator(grid)
        self.__moves = self.__get_moves(grid, relative_positions)
        self.__relative_positions = relative_positions

    def __getitem__(self, key: slice | int) -> tuple[Move, ...] | Move:
        if isinstance(key, slice):
            return tuple(self.__moves[key])
        if isinstance(key, int):
            return self.__moves[key]

    def __len__(self) -> int:
        return len(self.__moves)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, ValidMoves):
            return (
                self.__relative_positions == __o.__relative_positions
                and self.__grid == __o.__grid
            )
        return False

    def __contains__(self, move: Move) -> bool:
        return move in self.__moves

    def __is_valid(self, peg_position: Position, relative_position: Position) -> bool:
        move = RelativeMove(peg_position, relative_position)
        return self.__move_validator.validate(move)

    def __get_moves(
        self, grid: Grid, relative_positions: tuple[Position, ...]
    ) -> list[Move]:
        return sorted(
            [
                RelativeMove(peg_position, relative_position)
                for peg_position in grid.peg_positions
                for relative_position in relative_positions
                if self.__is_valid(peg_position, relative_position)
            ]
        )
