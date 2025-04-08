"""
class file for item related functions
"""

from typing import Final

from config.config import Config, ITEM_CONFIG
from style import style, styleBundle, Style, set_style, hex_to_rgb, rgb

item_config = Config(ITEM_CONFIG)

RARITY_COLOR: Final[list[style]] = [rgb(*hex_to_rgb(h))
                                    for h in item_config.data["color"]]
RARITY_NAME: Final[list[str]] = item_config.data["rarity"]


class Item:
    def __init__(self, name: str, rarity: int = 0) -> None:
        self.name = name
        self._rarity = rarity

    def __repr__(self) -> str:
        return f"Item({self.name}: {self.get_rarity(self)})"

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
        rarity = item.rarity
        styles: styleBundle = [Style.BOLD, RARITY_COLOR[rarity]]

        name = item.name if is_item else RARITY_NAME[rarity]

        return set_style(name, style_bundle=styles)


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
