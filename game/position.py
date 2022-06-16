from __future__ import annotations


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            return __o.x == self.x and __o.y == self.y
        return NotImplemented

    def __hash__(self) -> int:
        return hash(f"{self.x}{self.y}")

    def __lt__(self, __o: object) -> bool:
        if isinstance(__o, Position):
            if self.x != __o.x:
                return self.x < __o.x
            if self.y != __o.y:
                return self.y < __o.y
        return False

    def __add__(self, __o: object) -> Position:
        if isinstance(__o, Position):
            sum_x = self.x + __o.x
            sum_y = self.y + __o.y
            return Position(sum_x, sum_y)
        raise NotImplementedError

    def __sub__(self, __o: object) -> Position:
        if isinstance(__o, Position):
            sub_x = self.x - __o.x
            sub_y = self.y - __o.y
            return Position(sub_x, sub_y)
        raise NotImplementedError

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
