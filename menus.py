"""
Contains all functions for menus
"""

from config.config import Config, SETTINGS_CONFIG
from config.settings import Settings
from interface import Inventory, Menu
from items import Item

main_config = Config("data/menus/main_menu.json")

class MainMenu:
    def __init__(self):
        self.display = Menu[str](main_config["name"], main_config["options"])
        self.inventory = Inventory[Item]("Inventory")
        self._settings = Settings(SETTINGS_CONFIG)
        self._running = True

    # ---
    def play(self) -> ...:
        pass

    def settings_display(self) -> ...:
        print("Settings:\n"
              f"- Cursor [{self._settings.data['cursor']['icon']}]\n"
              f"- Color: {self._settings.data['cursor']['color']}")

    def help(self) -> None:
        print("Help Stuff: \n To be added...")

    def quit(self) -> None:
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    @property
    def settings(self) -> Settings:
        return self._settings

    @running.setter
    def running(self, value) -> None:
        self._settings.save()
        self._running = value

