class UnparsablePositionError(Exception):
    def __init__(self, input: str) -> None:
        super().__init__(input)
