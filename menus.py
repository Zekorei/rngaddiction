"""
Contains all functions for menus
"""

from file_handling import JSON, Configs
from interface import Inventory, Menu
from items import Item
from style import set_style, hex_style

config = JSON(Configs.MAIN)

# TODO: context object to store all necessary runtime information; can be return by main on demand

class MainMenu:
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
    def settings_info(self) -> ...:
        print("Settings:\n"
              f"- Cursor [{self._settings['cursor/icon']}]\n"
              f"- Color: {self._settings['cursor/color']}")

    def help(self) -> None:
        print("Help Stuff: \n To be added...")

    def quit(self) -> None:
        self._running = False

    def get_cursor(self) -> str:
        color = hex_style(self._settings['cursor/color'])
        return set_style(self._settings['cursor/icon'], color)

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self._running = value
