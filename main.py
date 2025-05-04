"""
zekorei

04/06/2025
unnamed gacha game v0.1
"""

from menus import MainMenu

def start_up() -> MainMenu:
    pass
    # TODO: load item data
    # TODO: load banner data
    # TODO: construct game context
    

# --- main
def main():
    game = start_up()

    while game.running:
        game.update_settings()

        try:
            game.display.print()
            game.display_cursor()
            cmd = input()

            match cmd:
                case "2":
                    game.settings()
                case "3":
                    game.help()
                case "4":
                    game.quit()

        except KeyboardInterrupt:
            game.update_settings()
            game.running = False


# ---
if __name__ == "__main__":
    main()
