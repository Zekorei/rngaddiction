"""
class file for item related functions
"""
from enum import IntEnum
from os import PathLike
from typing import Final

from file_handling import Configs, JSON
from style import Style

item_config = JSON(Configs.RARITIES)

class Rarity(IntEnum):
    BASIC = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

# process item data
RARITY_COLOR: Final[list[Style]] = [Style.from_hex(h) for h in item_config["color"]]
RARITY_NAME: Final[list[str]] = item_config["rarity"]


class Item:
    def __init__(self, name: str, rarity: Rarity = Rarity.BASIC) -> None:
        self._name = name
        self._rarity = rarity

    @classmethod
    def from_json(cls, path: str | PathLike[str]) -> 'Item':
        item_dat = JSON(path)

        return cls(item_dat["name"], Rarity(item_dat["rarity"]))

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}(name={self.name}, rarity={self._rarity})"

    def __str__(self) -> str:
        return f"{self._name}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def rarity(self) -> int:
        return self._rarity

    @rarity.setter
    def rarity(self, value) -> None:
        self._rarity = value


# TODO: Item banner with weights and ability to draw an item
#  - store items in a way that has weights and qty dropped
#  - pity system
#  - rarity up events etc.
#  - populate or random draw
"""
static system

class:
    items: tuple[Item, int, int] - list(Item, weight, qty)
    pity_count: int
    
    
"""
