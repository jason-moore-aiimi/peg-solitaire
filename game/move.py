from .position import Position
from math import sqrt


class Move:
    def __init__(self, current_position: Position, new_position: Position) -> None:
        self.__current_position = current_position
        self.__new_position = new_position
        self.__unit_vector = self.___get_unit_vector()
        self.__end = self.__new_position + self.__unit_vector

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Move):
            return (
                self.__current_position == __o.__current_position
                and self.__new_position == __o.__new_position
            )
        return False

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Move):
            if self.__current_position != __o.__current_position:
                return self.__current_position < __o.__current_position
            if self.__new_position != __o.__new_position:
                return self.__new_position < __o.__new_position
        return False

    def __str__(self) -> str:
        return f"{self.__current_position} -> {self.__new_position}"

    @property
    def positions(self) -> tuple[Position, ...]:
        if self.__unit_vector.x != 0:
            direction = self.__unit_vector.x
            xs = range(self.current_position.x, self.__end.x, direction)
            return tuple(Position(x, self.__end.y) for x in xs)
        if self.__unit_vector.y != 0:
            direction = self.__unit_vector.y
            ys = range(self.current_position.y, self.__end.y, direction)
            return tuple(Position(self.__end.x, y) for y in ys)
        return (self.current_position, self.new_position)

    @property
    def current_position(self) -> Position:
        return self.__current_position

    @property
    def new_position(self) -> Position:
        return self.__new_position

    def ___get_unit_vector(self) -> Position:
        if self.current_position != self.new_position:
            position_diff = self.new_position - self.current_position
            magnitude = sqrt(position_diff.x ** (2) + position_diff.y ** (2))
            x = int(position_diff.x / magnitude)
            y = int(position_diff.y / magnitude)
            return Position(x, y)
        return Position(0, 0)
