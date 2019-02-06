import libtcodpy as libtcod

class Presenter:
    def __init__(self, window_width, window_height, window_title, font_path):
        self._window_width = window_width
        self._window_height = window_height

        libtcod.console_set_custom_font(str(font_path), libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(window_width, window_height, window_title, False)

