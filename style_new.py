"""
file for terminal text coloring
"""
from enum import Enum
from itertools import chain
from re import compile, match
from typing import NewType, Final, Iterable, AnyStr

ANSI_FORMAT = compile(r"\033\[(?:[0-9]+;)*[0-9]+m")


class Style:
    # ---
    def __init__(self, ansi: str) -> None:
        if ANSI_FORMAT.match(ansi) is None:
            raise TypeError("Invalid ANSI code")

        self._code = ansi

    def __str__(self) -> str:
        return self._code

    def __radd__(self, other: AnyStr) -> AnyStr:
        return other + str(self)

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int) -> 'Style':
        return cls(f"\033[38;2;{r};{g};{b}m")

    @classmethod
    def from_rgb_t(cls, rgb: tuple[int, int, int]) -> 'Style':
        return cls.from_rgb(*rgb)

    @classmethod
    def from_hex(cls, h: str) -> 'Style':
        return cls.from_rgb_t(cls.hex_to_rgb(h))

    def __repr__(self):
        return f"{self.__class__.__name__}({self._code})"

    # ---
    @staticmethod
    def hex_to_rgb(h: str) -> tuple[int, int, int]:
        """
            Converts a colour code in hex (#FFFFFF) to a rgb code.

            :param h: The colour code in hex (#FFFFFF)
            :return: A tuple (r, g, b) of rgb values
            """
        h = h.lstrip("#")

        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

    @staticmethod
    def st_print(text: str,
                 *styles: 'Style',
                 style_list: Iterable['Style'] | None = None,
                 bold: bool = False,
                 end: str = "\n") -> None:
        """
        Applies ANSI escape sequences to the input text.

        :param text: input text.
        :param styles: any number of style sequences.
        :param style_list: an iterable of style sequences.
        :param bold: whether the text should be bold, default False.
        :param end: string appended after the last value, default a newline.
        :return: the input text with ANSI escape sequences applied.
        """
        out = "".join(str(style) for style in chain(styles, style_list))

        if bold:
            out += BOLD

        print(out + text + END, end=end)


# text styling
BOLD: Final[Style] = Style("\033[1m")
UNDERLINE: Final[Style] = Style("\033[4m")

END_C: Final[Style] = Style("\033[39;49m")  # reset colour
END: Final[Style] = Style("\033[0m")  # reset all


def colour_test8bit() -> None:
    """
    Prints out the 8-bit (256) ANSI escape codes in an 8 by 8 matrix.

    :return: None
    """
    for i in range(256):
        print(f"\033[38;5;{i}m {i: >3} {END}", end="")

        if i % 16 == 15:
            print()

    print(END)

    return None
