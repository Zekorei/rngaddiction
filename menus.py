"""
Contains all functions for menus
"""

from interface import Menu
from config.config import Config, SETTINGS_CONFIG
from config.settings import Settings

main_config = Config("data/menus/main_menu.json")

class MainMenu:
    def __init__(self):
        self.display = Menu[str](main_config["name"], main_config["options"])
        self.settings = Settings(SETTINGS_CONFIG)
        self._running = True

    # ---
    def play(self) -> ...:
        pass

    def settings(self) -> ...:
        pass

    def help(self) -> ...:
        pass

    def quit(self) -> None:
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self.settings.save()
        self._running = value

