from .row_factory import RowFactory
from .console_messages import UNPARSABLE_POSITION, INVALID_MOVE
from game import Square, Move


class Printer:
    def __init__(self, row_factory: RowFactory) -> None:
        self.row_factory = row_factory

    def print_grid(self, grid: tuple[tuple[Square | None, ...], ...]) -> None:
        row_length = max(len(row) for row in grid)
        print(self.row_factory.get_columns(row_length))
        for row_number, row in enumerate(grid):
            row_str = self.row_factory.get_row(row)
            print(f"{row_number}{row_str}")

    def print_unparsable_position(self, input: str) -> None:
        print(f"{input} {UNPARSABLE_POSITION}")

    def print_invalid_move(
        self, invalid_move: Move, valid_moves: tuple[Move, ...]
    ) -> None:
        print(f"{invalid_move} {INVALID_MOVE}:")
        for valid_move in valid_moves:
            print(valid_move)
