"""
class file for item related functions
"""

from typing import Final

from file_handling import Configs, JSON
from style import Style
# from style import style, styleBundle, Style, set_style, hex_to_rgb, rgb

item_config = JSON(Configs.ITEM)

# process item data
RARITY_COLOR: Final[list[Style]] = [Style.from_hex(h) for h in item_config["color"]]
RARITY_NAME: Final[list[str]] = item_config["rarity"]


class Item:
    def __init__(self, name: str, rarity: int = 0) -> None:
        self.name = name
        self._rarity = rarity

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}({self.name}: {self.get_rarity(self)})"

    def __str__(self) -> str:
        return f"{self.get_rarity(self, is_item=True)}"

    @property
    def rarity(self) -> int:
        return self._rarity

    @rarity.setter
    def rarity(self, value) -> None:
        self._rarity = value

    @staticmethod
    def get_rarity(item: "Item", is_item: bool = False) -> str:
        # TODO: remove or fix cuz i have no idea what this is

        pass
        # - previous code -
        # rarity = item.rarity
        # styles = [Style.BOLD, RARITY_COLOR[rarity]]
        #
        # name = item.name if is_item else RARITY_NAME[rarity]
        #
        # return set_style(name, style_bundle=styles)
        # ---


class ItemPool:
    # ---
    def __init__(self, pool: list[Item]) -> None:
        self._pool = pool

    # ---
    @property
    def pool(self) -> list[Item]:
        return self._pool

    def insert(self, item: Item) -> None:
        self._pool.append(item)
