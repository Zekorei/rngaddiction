import os
from json import load, dumps
from os import PathLike
from typing import Any


type JSONDict = dict[str, Any]

INDENT_SIZE = 2

SETTINGS_CONFIG = "settings.json"
ITEM_CONFIG = "item_data.json"


class File:
    def __init__(self, file_path: str | PathLike[str]) -> None:
        self._path = file_path
        self._name = self._path.split(os.pathsep)[-1]
        self._type = self._name.split(".")[-1]

    def __repr__(self):
        return f"{self.__class__.__name__}({self._path})"

    # ---
    @property
    def path(self) -> str | PathLike[str]:
        return self._path

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type


# TODO: generalize to a json object with path lookup
class Config:
    @staticmethod
    def load(file_path: str | PathLike[str]) -> JSONDict:
        with open(file_path, "r") as stream:
            data: JSONDict = load(stream)

        return data

    @staticmethod
    def file_name(file_path: str | PathLike[str]) -> str:
        return

    @staticmethod
    def file_type(file: str):
        return

    # ---
    def __init__(self, file_path: str | PathLike[str]) -> None:
        self.file = File(file_path)

        if self.file.type == "json":
            self.data = self.load(self.file.path)
        else:
            raise TypeError(f"Unable to read file (.{self.file.type})")

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}(path={self.file.path!r}, data={self.data!r})"

    def __getitem__(self, key: str) -> str | Any:
        return self.data[key]

    # ---
    def save(self):
        with open(self.file.path, "w") as stream:
            stream.write(dumps(self.data, indent=INDENT_SIZE))

    def update(self) -> None:
        self.data = self.load(self.file.path)
