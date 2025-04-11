"""
zekorei

04/06/2025
unnamed gacha game v0.1
"""

from config.settings import Settings
from config.config import SETTINGS_CONFIG
from interface import Menu, Inventory
from items import Item


OPTIONS = ["temp", "settings", "help", "quit"]


# --- main
def main():
    running = True
    settings = Settings(SETTINGS_CONFIG)
    inventory = Inventory[Item]("Inventory")
    main_menu = Menu[str]("Main Menu", OPTIONS)

    while running:
        try:
            main_menu.print()

            print(f"{settings.cursor} ", end="")
            cmd = input()

            print(cmd)

        except KeyboardInterrupt:
            settings.save()
            running = False


# ---
if __name__ == "__main__":
    main()
