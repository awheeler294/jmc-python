from pathlib import Path

import tcod as libtcodpy

from presenter import Presenter

def main():
    window_width = 80
    window_height = 50
    window_title = "Janus Mining Colony"
    font_path = Path("fonts/libtcod/dejavu16x16_gs_tc.png")

    presenter = Presenter(window_width, window_height, window_title, font_path)

    while presenter.is_window_open():
        presenter.put_tile(1, 1, '@', libtcodpy.white)
        presenter.present()

        key = libtcodpy.console_check_for_keypress()

        if key.vk == libtcodpy.KEY_ESCAPE:
            return True

if __name__ == '__main__':
    main()
