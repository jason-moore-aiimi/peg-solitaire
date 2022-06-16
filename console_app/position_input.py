from .printer import Printer
from .position_parser import PositionParser
from .unparsable_position_error import UnparsablePositionError
from .console_messages import (
    ASK_WHAT_PEG_TO_MOVE,
    ASK_WHERE_TO_MOVE_PEG,
)
from game import Position


class PositionInput:
    def __init__(self, printer: Printer, position_parser: PositionParser) -> None:
        self.__position_parser = position_parser
        self.__printer = printer

    def get_peg_position(self) -> Position:
        return self.__get_position(ASK_WHAT_PEG_TO_MOVE)

    def get_move_to_position(self) -> Position:
        return self.__get_position(ASK_WHERE_TO_MOVE_PEG)

    def __get_position(self, prompt):
        while True:
            try:
                input_str = input(prompt)
                return self.__position_parser.parse(input_str)
            except (UnparsablePositionError):
                self.__printer.print_unparsable_position(input_str)
