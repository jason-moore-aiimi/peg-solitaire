from .square import Square


class Empty(Square):
    def __init__(self) -> None:
        super().__init__(False)
