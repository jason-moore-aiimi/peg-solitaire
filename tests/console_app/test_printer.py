import pytest
from game.empty import Empty
from game.move import Move
from game.peg import Peg
from game.position import Position
from game.square import Square

from console_app.console_messages import INVALID_MOVE, UNPARSABLE_POSITION
from console_app.element_factory import ElementFactory
from console_app.printer import Printer
from console_app.row_factory import RowFactory

PEG = "X"
SQUARE = "O"
EMPTY = "  "
BORDER = "|"


@pytest.fixture
def printer() -> Printer:
    element_factory = ElementFactory(PEG, SQUARE, EMPTY)
    row_factory = RowFactory(element_factory, BORDER)
    return Printer(row_factory)


@pytest.mark.parametrize(
    "elements,expected",
    [
        (
            (
                (None, Peg(), Empty(), Peg(), None),
                (Peg(), Empty(), Peg(), Empty(), Peg()),
                (None, Empty(), Peg(), Empty(), None),
            ),
            (
                f"  0 1 2 3 4\n"
                f"0{EMPTY}{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}{EMPTY}\n"
                f"1{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}\n"
                f"2{EMPTY}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{EMPTY}\n"
            ),
        ),
        (
            (
                (None, Peg(), Empty()),
                (Peg(), Empty(), Peg(), Empty(), Peg()),
                (None, Empty(), Peg(), None),
            ),
            (
                f"  0 1 2 3 4\n"
                f"0{EMPTY}{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}\n"
                f"1{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}\n"
                f"2{EMPTY}{BORDER}{SQUARE}{BORDER}{PEG}{BORDER}{EMPTY}\n"
            ),
        ),
    ],
)
def test_print_grid_prints_the_correct_grid(
    capfd,
    elements: tuple[tuple[Square | None, ...], ...],
    expected: tuple[str, ...],
    printer: Printer,
) -> None:
    printer.print_grid(elements)

    out, _ = capfd.readouterr()
    assert out == expected


def test_print_unparsable_position_prints_correct_message(
    capfd, printer: Printer
) -> None:
    input = "x:x"
    printer.print_unparsable_position(input)

    out, _ = capfd.readouterr()
    assert out == f"{input} {UNPARSABLE_POSITION}\n"


def test_print_invalid_move_prints_correct_messages(capfd, printer: Printer) -> None:
    invalid_move = Move(Position(1, 1), Position(1, 1))
    valid_moves = (
        Move(Position(1, 1), Position(3, 1)),
        Move(Position(1, 1), Position(1, 3)),
        Move(Position(1, 1), Position(1, -3)),
        Move(Position(1, 1), Position(-3, 1)),
    )
    printer.print_invalid_move(invalid_move, valid_moves)

    out, _ = capfd.readouterr()
    valid_move_string = "".join(f"{valid_move}\n" for valid_move in valid_moves)
    expected = f"{invalid_move} {INVALID_MOVE}:\n{valid_move_string}"
    assert out == expected
