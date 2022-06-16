from .move import Move


class InvalidMoveError(Exception):
    def __init__(self, move: Move) -> None:
        super().__init__(move)
