"""
zekorei

04/06/2025
unnamed gacha game v0.1
"""

from menus import MainMenu

# --- main
def main():
    main_menu = MainMenu()

    while main_menu.running:
        main_menu.update()

        try:
            main_menu.display.print()
            print(f"{main_menu.get_cursor()} ", end="")
            cmd = input()

            match cmd:
                case "2":
                    main_menu.settings_info()
                case "3":
                    main_menu.help()
                case "4":
                    main_menu.quit()

        except KeyboardInterrupt:
            main_menu.update()
            main_menu.running = False


# ---
if __name__ == "__main__":
    main()
