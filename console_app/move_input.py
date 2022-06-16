from .position_input import PositionInput
from game import Move


class MoveInput:
    def __init__(self, position_input: PositionInput) -> None:
        self.__position_input = position_input

    def get_move(self) -> Move:
        current_position = self.__position_input.get_peg_position()
        new_position = self.__position_input.get_move_to_position()
        return Move(current_position, new_position)
