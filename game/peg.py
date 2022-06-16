from .square import Square


class Peg(Square):
    def __init__(self) -> None:
        super().__init__(True)
