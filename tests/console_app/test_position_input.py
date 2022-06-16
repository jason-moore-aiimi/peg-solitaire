import pytest
from game.position import Position
from tests.console_app.mock_input import MockInput

from console_app.console_messages import (
    ASK_WHAT_PEG_TO_MOVE,
    ASK_WHERE_TO_MOVE_PEG,
    UNPARSABLE_POSITION,
)
from console_app.element_factory import ElementFactory
from console_app.position_input import PositionInput
from console_app.position_parser import PositionParser
from console_app.printer import Printer
from console_app.row_factory import RowFactory


@pytest.fixture
def position_input():
    element_factory = ElementFactory()
    row_factory = RowFactory(element_factory)
    printer = Printer(row_factory)
    position_parser = PositionParser()
    return PositionInput(printer, position_parser)


@pytest.mark.parametrize(
    "input,position",
    [
        ("1,1", Position(1, 1)),
        ("1,5", Position(1, 5)),
        ("8,1", Position(8, 1)),
        ("6,9", Position(6, 9)),
    ],
)
def test_get_peg_posiiton_returns_the_correct_position(
    monkeypatch, input: str, position: Position, position_input: PositionInput
) -> None:
    mock_input = MockInput(
        ASK_WHAT_PEG_TO_MOVE,
        input,
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    assert position_input.get_peg_position() == position


def test_get_peg_posiiton_keeps_requesting_input_till_valid_input_is_provided(
    monkeypatch, position_input: PositionInput
) -> None:
    mock_input = MockInput(
        ASK_WHAT_PEG_TO_MOVE,
        "x,1",
        "1,y",
        "1:1",
        "x:y",
        "5,5",
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    actual = position_input.get_peg_position()

    assert actual == Position(5, 5)


def test_get_peg_posiiton_prints_unparsable_position_message_when_invalid_input_is_provided(
    monkeypatch, position_input: PositionInput, capfd
) -> None:
    mock_input = MockInput(
        ASK_WHAT_PEG_TO_MOVE,
        "x,1",
        "1,y",
        "1:1",
        "x:y",
        "5,5",
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    _ = position_input.get_peg_position()

    out, _ = capfd.readouterr()
    assert out == (
        f"x,1 {UNPARSABLE_POSITION}\n"
        f"1,y {UNPARSABLE_POSITION}\n"
        f"1:1 {UNPARSABLE_POSITION}\n"
        f"x:y {UNPARSABLE_POSITION}\n"
    )


@pytest.mark.parametrize(
    "input,position",
    [
        ("1,1", Position(1, 1)),
        ("1,5", Position(1, 5)),
        ("8,1", Position(8, 1)),
        ("6,9", Position(6, 9)),
    ],
)
def test_get_move_to_posiiton_returns_the_correct_position(
    monkeypatch, input: str, position: Position, position_input: PositionInput
) -> None:
    mock_input = MockInput(
        ASK_WHERE_TO_MOVE_PEG,
        input,
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    assert position_input.get_move_to_position() == position


def test_get_move_to_posiiton_keeps_requesting_input_till_valid_input_is_provided(
    monkeypatch, position_input: PositionInput
) -> None:
    mock_input = MockInput(
        ASK_WHERE_TO_MOVE_PEG,
        "x,1",
        "1,y",
        "1:1",
        "x:y",
        "5,5",
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    actual = position_input.get_move_to_position()

    assert actual == Position(5, 5)


def test_get_move_to_posiiton_prints_unparsable_position_message_when_invalid_input_is_provided(
    monkeypatch, position_input: PositionInput, capfd
) -> None:
    mock_input = MockInput(
        ASK_WHERE_TO_MOVE_PEG,
        "x,1",
        "1,y",
        "1:1",
        "x:y",
        "5,5",
    )
    monkeypatch.setattr("builtins.input", mock_input.get_input)

    _ = position_input.get_move_to_position()

    out, _ = capfd.readouterr()
    assert out == (
        f"x,1 {UNPARSABLE_POSITION}\n"
        f"1,y {UNPARSABLE_POSITION}\n"
        f"1:1 {UNPARSABLE_POSITION}\n"
        f"x:y {UNPARSABLE_POSITION}\n"
    )
