"""
Operates all interface based functionalities
"""
from abc import abstractmethod
from typing import Generic, TypeVar, Any

from style_new import Style, UNDERLINE

# from style import Style, set_style

T = TypeVar('T')

def print_indexed_item(element: Any, index: int | None = None,
                       include_tab=False) -> None:
    if element.__str__ is object.__str__:
        raise NotImplemented(
            f"__str__ is not implemented for class {type(element)}.")

    if include_tab:
        print("\t", end="")

    Style.st_print(str(index), bold=True, end="")
    print(" " + str(element))


class Interface(Generic[T]):
    EMPTY = "[empty]" # TODO: make name more descriptive

    # ---
    def __new__(cls, *args, **kwargs):
        if T.__str__ is object.__str__:
            raise NotImplemented(f"__str__ is not implemented for class {T}.")

        return super().__new__(cls)

    def __init__(self, name: str, elements: list[T] = None) -> None:
        self._name = name

        if elements is None:
            self._elements = []
        else:
            self._elements = elements

    def __repr__(self):
        return f"{self.__class__.__name__}[{T}]"

    # ---
    def print_title(self) -> None:
        Style.st_print(self._name + ':', UNDERLINE)

    @property
    def elements(self) -> list[T]:
        return self._elements

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def print(self) -> None: ...


class Menu(Interface[T]):
    # ---
    def __init__(self, name: str, options: list[T]) -> None:
        super().__init__(name, options)

        self._options = self.elements

    # ---
    @property
    def options(self) -> list[T]:
        return self._options

    def print(self) -> None:
        self.print_title()

        if len(self.options) > 0:
            for i, option in enumerate(self.options):
                print_indexed_item(option, i + 1, include_tab=True)
        else:
            print(self.EMPTY)


class Inventory(Interface[T]):
    # ---
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.items = self.elements
        self._page = 1
        self._max_page_size = 6 # pseudo constant for now

    def __len__(self):
        return len(self._elements)

    @property
    def page(self):
        return self._page

    @property
    def max_page_size(self):
        return self._max_page_size
    # ---

    @page.setter
    def page(self, page: int) -> None:
        page = min(max(1, page), len(self) // self.max_page_size)

        self._page = page

    def print(self) -> None:
        self.print_title()

        # TODO: add pages to inventory display
        if len(self.items) > 0:
            for index, option in enumerate(self.elements):
                print(print_indexed_item(option, index + 1, include_tab=True))
        else:
            print(self.EMPTY)

    def insert(self, obj: T) -> None:
        self._elements.append(obj)
