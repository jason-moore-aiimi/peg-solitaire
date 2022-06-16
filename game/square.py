class Square:
    def __init__(self, contains_peg: bool = False) -> None:
        self.__contains_peg = contains_peg

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Square):
            return self.__contains_peg == __o.__contains_peg
        return False

    def __bool__(self) -> bool:
        return self.__contains_peg

    @property
    def contains_peg(self) -> bool:
        return self.__contains_peg
