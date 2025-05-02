"""
Contains all functions for menus
"""

from file_handling import JSON, Configs
from interface import Inventory, Menu
from items import Item
from style import Style

config = JSON(Configs.MAIN)

# TODO: context object to store all necessary runtime information; can be return by main on demand

class MainMenu:
    CURSOR_PATH = "cursor/icon"
    CURSOR_COLOR = "cursor/color"

    def __init__(self):
        self.display = Menu[str](config["name"], config["options"])
        self.inventory = Inventory[Item]("Inventory")
        self._settings = JSON(Configs.SETTINGS)
        self._running = True

    # ---
    def update(self):
        self._settings.save()

    # TODO: make game functional
    def play(self) -> ...:
        pass

    # add more settings details
    def settings(self) -> ...:
        print("Settings:\n"
              f"- Cursor [{self._settings[self.CURSOR_PATH]}]\n"
              f"- Color: {self._settings[self.CURSOR_COLOR]}")

    def help(self) -> None:
        print("Help Stuff: \n To be added...")

    def quit(self) -> None:
        self._running = False

    def get_cursor(self) -> str:
        return self._settings[self.CURSOR_PATH]

    def display_cursor(self) -> None:
        color = Style.from_hex(self._settings[self.CURSOR_COLOR])

        Style.st_print(self.get_cursor() + " ", color, end="")

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self._running = value
