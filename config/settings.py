from os import PathLike

from config.config import Config
from style import set_style, Style, hex_style

class Settings(Config):
    def __init__(self, path: str | PathLike[str]):
        super().__init__(path)

        self.settings = self.data

    @property
    def cursor(self):
        cursor_settings = self.settings["cursor"]

        return set_style(cursor_settings["icon"],
                         hex_style(cursor_settings["color"]))

    @cursor.setter
    def cursor(self, cursor: chr):
        self.settings["cursor"]["icon"] = cursor
        self.save()
