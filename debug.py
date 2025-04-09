"""
Debugging tools

"""

from datetime import datetime
from style import Style, set_style, rgb, hex_to_rgb, style
from sys import stdout

DEBUG_RED: str = "#E6000D"
DB_RED_S: style = rgb(*hex_to_rgb(DEBUG_RED))


def log(contents: str) -> None:
    stdout.write(f"{set_style(contents, DB_RED_S, Style.BOLD)}")


def time(newline=False) -> None:
    now = datetime.now()

    timestamp = "[" + now.strftime("%H:%M:%S") + "]"
    timestamp += "\n" if newline else ""

    log(timestamp)

def tlog(contents: str) -> None:
    time()
    log(": " + contents)
