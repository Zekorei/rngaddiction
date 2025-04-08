"""
file for terminal text coloring
"""

from typing import NewType, Final, Iterable

# style types
style = NewType('style', str)
type styleBundle = Iterable[style]


class Style:
    # text style codes
    BOLD: Final[style] = "\033[1m"
    UNDERLINE: Final[style] = "\033[4m"

    END_C: Final[style] = "\033[39;49m" # reset colour
    END: Final[style] = "\033[0m" # reset all


def set_style(text: str, *styles: style, style_bundle: styleBundle = None) -> str:
    """
    Applies ANSI escape sequences to the input text.

    :param text: The input text
    :param styles: Any number of style sequences
    :param style_bundle: An iterable of style sequences
    :return: The input text with ANSI escape sequences applied
    """
    codes = ""

    for code in styles:
        codes += code

    if style_bundle is not None:
        for code in style_bundle:
            codes += code

    return codes + text + Style.END


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    """
    Converts a colour code in hex (#FFFFFF) to a rgb code.

    :param h: The colour code in hex (#FFFFFF)
    :return: The corresponding rgb code as a tuple of ints
    """

    h = h.lstrip("#")

    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb(r: int, g: int, b: int) -> style:
    """
    Takes the rgb values and outputs a style object with representing the color
    as an ANSI escape sequence.

    :param r: Value of red
    :param g: Value of green
    :param b: Value of blue
    :return: An ANSI escape code representing the rgb input
    """
    return style(f"\033[38;2;{r};{g};{b}m")


def colour_test8bit() -> None:
    """
    Prints out the 8-bit (256) ANSI escape codes in an 8 by 8 matrix.

    :return: None
    """
    for i in range(256):
        print(f"\033[38;5;{i}m {i: >3} {Style.END}", end="")

        if i % 16 == 15:
            print()

    print(Style.END)

    return None
