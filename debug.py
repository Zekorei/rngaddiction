"""
Debugging tools

"""

from datetime import datetime
from style import Style

DEBUG_RED = "#E6000D"
DEBUG_RED_S = Style.from_hex(DEBUG_RED)

def log(contents: str) -> None:
    Style.st_print(contents, DEBUG_RED_S, bold=True, end="")


def time(newline=False) -> None:
    now = datetime.now()

    timestamp = "[" + now.strftime("%H:%M:%S") + "]"
    timestamp += "\n" if newline else ""

    log(timestamp)

def tlog(contents: str) -> None:
    time()
    log(": " + contents)
