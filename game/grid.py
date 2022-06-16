from typing import Iterator
from .position import Position
from .square import Square


class Grid:
    def __init__(
        self,
        position_squares: dict[Position, Square],
    ) -> None:
        self.__position_squares = position_squares

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Grid):
            return all(
                square == __o[position]
                for position, square in self.__position_squares.items()
            )
        return False

    def __getitem__(self, position: Position) -> Square | None:
        if position in self.__position_squares:
            return self.__position_squares[position]
        return None

    def __setitem__(self, position: Position, square: Square) -> None:
        self.__position_squares[position] = square

    def __iter__(self) -> Iterator[tuple[Square | None, ...]]:
        return iter(
            tuple(
                tuple(self[Position(x, y)] for x in range(self.__max_x))
                for y in range(self.__max_y)
            )
        )

    @property
    def peg_count(self) -> int:
        return len(self.peg_positions)

    @property
    def peg_positions(self) -> tuple[Position, ...]:
        return self.__get_positions(True)

    @property
    def empty_positions(self) -> tuple[Position, ...]:
        return self.__get_positions(False)

    @property
    def __max_x(self) -> int:
        return max(position.x for position in self.__position_squares.keys()) + 1

    @property
    def __max_y(self) -> int:
        return max(position.y for position in self.__position_squares.keys()) + 1

    def __get_positions(self, contains_peg: bool) -> tuple[Position, ...]:
        return tuple(
            position
            for position, square in self.__position_squares.items()
            if square.contains_peg == contains_peg
        )
