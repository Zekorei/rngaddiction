from json import load, dumps
from os import PathLike
from typing import Any


type JSONDict = dict[str, Any]

INDENT_SIZE = 2

SETTINGS_CONFIG = "settings.json"
ITEM_CONFIG = "item_data.json"


class Config:
    @staticmethod
    def load(f_path: str | PathLike[str]) -> JSONDict:
        with open(f_path, "r") as stream:
            data: JSONDict = load(stream)

        return data

    # ---
    def __init__(self, path: str | PathLike[str]) -> None:
        self.path = path

        if path.endswith(".json"):
            self.data = self.load(path)
        else:
            raise TypeError("Unable to read file")

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}(path={self.path!r}, data={self.data!r})"

    def __getitem__(self, key: str) -> str | Any:
        return self.data[key]

    # ---
    def save(self):
        with open(self.path, "w") as stream:
            stream.write(dumps(self.data, indent=INDENT_SIZE))

    def update(self) -> None:
        self.data = self.load(self.path)
