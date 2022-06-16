from game.move import Move
from game.position import Position

from console_app.element_factory import ElementFactory
from console_app.move_input import MoveInput
from console_app.position_input import PositionInput
from console_app.position_parser import PositionParser
from console_app.printer import Printer
from console_app.row_factory import RowFactory


def test_get_move_returns_correct_move(mocker) -> None:
    element_factory = ElementFactory()
    row_factory = RowFactory(element_factory)
    printer = Printer(row_factory)
    position_parser = PositionParser()
    position_input = PositionInput(printer, position_parser)
    peg_position = Position(3, 4)
    move_to_position = Position(6, 9)
    move_input = MoveInput(position_input)
    mocker.patch(
        "console_app.position_input.PositionInput.get_peg_position",
        lambda _: peg_position,
    )
    mocker.patch(
        "console_app.position_input.PositionInput.get_move_to_position",
        lambda _: move_to_position,
    )

    assert move_input.get_move() == Move(peg_position, move_to_position)
