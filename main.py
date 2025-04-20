"""
zekorei

04/06/2025
unnamed gacha game v0.1
"""

# from config.settings import Settings
# from config.config import SETTINGS_CONFIG
# from interface import Menu, Inventory
# from items import Item
from menus import MainMenu


# --- main
def main():
    main_menu = MainMenu()
    settings = main_menu.settings

    while main_menu.running:
        settings.update()

        try:
            main_menu.display.print()
            print(f"{settings.cursor} ", end="")
            cmd = input()

            match cmd:
                case "2":
                    main_menu.settings_display()
                case "3":
                    main_menu.help()
                case "4":
                    main_menu.quit()

        except KeyboardInterrupt:
            settings.save()
            main_menu.running = False


# ---
if __name__ == "__main__":
    main()
