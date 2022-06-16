from .element_factory import ElementFactory
from game import Square


class RowFactory:
    def __init__(self, element_factory: ElementFactory, border: str = "") -> None:
        self.element_factory: ElementFactory = element_factory
        self.border: str = border

    def get_row(self, row: tuple[Square | None, ...]) -> str:
        row_elements = [self.__get_column__(column) for column in row]
        row_str = "".join(row_elements)
        return row_str.replace(f"{self.border}{self.border}", self.border)

    def get_columns(self, row_length: int) -> str:
        column_numbers = [str(number) for number in range(row_length)]
        spaces = "".join(" " for _ in self.border)
        column_numbers.insert(0, " ")
        return spaces.join(column_numbers)

    def __get_column__(self, column: Square | None) -> str:
        element = self.element_factory.get_element(column)
        if column is None:
            return element
        return f"{self.border}{element}{self.border}"
