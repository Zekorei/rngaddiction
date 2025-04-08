from os import PathLike

from config.config import Config
from style import set_style, Style

class Settings(Config):
    def __init__(self, path: str | PathLike[str]):
        super().__init__(path)

        self.settings = self.data

    @property
    def cursor(self):
        cursor = self.settings["cursor"]["icon"]

        return set_style(cursor, Style.BOLD, Style.BOLD)

    @cursor.setter
    def cursor(self, cursor: chr):
        self.settings["cursor"]["icon"] = cursor
        self.save()
