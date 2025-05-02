import os
from json import load, dumps
from os import PathLike
from typing import Any, TextIO, Literal

type SupportsJSON = dict | list | str | int | float | bool | None

INDENT_SIZE = 2


class Configs:
    MAIN = "data/menus/main_menu.json"
    SETTINGS = "data/parameters/settings.json"
    ITEM = "data/misc/item_data.json"


class FileTypeError(Exception):
    pass


class File:
    def __init__(self, file_path: str | PathLike[str]) -> None:
        self.full_path = os.path.normpath(file_path)

        self._path, self._file = os.path.split(self.full_path)
        self._name, self._extension = os.path.splitext(self._file)

    def __repr__(self):
        return (f"{self.__class__.__name__}(full_path={self.full_path}, "
                f"path={self._path}), file={self._file}, name={self._name}, "
                f"ext={self._extension})")

    # ---
    def open(self, mode = "r") -> TextIO:
        return open(self.full_path, mode)

    def write(self) -> TextIO:
        return self.open(mode="w")

    def read(self) -> TextIO:
        return self.open(mode="r")

    @property
    def path(self) -> str | PathLike[str]:
        return self._path

    @property
    def name(self) -> str:
        return self._name

    @property
    def extension(self) -> str:
        return self._extension


# TODO: generalize to a json object with path lookup
class JSON:
    # ---
    def __init__(self, file_path: str | PathLike[str]) -> None:
        self.file = File(file_path)

        if self.file.extension == ".json":
            self.data = self.load()
        else:
            raise FileTypeError(f"Unable to read file extension ({self.file.extension})")

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}(file={self.file!r}, data={self.data!r})"

    # TODO: implement directory search
    """
    Default __getitem__ override with path lookup. Use standard os delimiter to
    indicate subdirectories.
    """
    def __getitem__(self, path: str | PathLike[str]) -> SupportsJSON:
        path = os.path.normpath(path)
        process = self.data

        for entry in path.split(os.path.sep):
            process = process[entry]

        return process


    # ---
    def load(self) -> dict[SupportsJSON]:
        with self.file.read() as stream:
            json = load(stream)

        return json

    def save(self):
        with self.file.write() as stream:
            stream.write(dumps(self.data, indent=INDENT_SIZE))

    def update(self) -> None:
        self.data = self.load()
