from game import Square, Peg


class ElementFactory:
    def __init__(
        self,
        peg: str = "X",
        square: str = "O",
        empty: str = "  ",
    ) -> None:
        self.peg = peg
        self.square = square
        self.empty = empty

    def get_element(self, square: Square | None) -> str:
        if square is None:
            return self.empty
        if isinstance(square, Peg):
            return self.peg
        return self.square
