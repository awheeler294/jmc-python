import tcod as libtcodpy

class Presenter:
    def __init__(self, window_width, window_height, window_title, font_path):
        self._window_width = window_width
        self._window_height = window_height

        libtcodpy.console_set_custom_font(str(font_path), libtcodpy.FONT_TYPE_GRAYSCALE | libtcodpy.FONT_LAYOUT_TCOD)

        libtcodpy.console_init_root(window_width, window_height, window_title, False)

    def is_window_open(self):
        return not libtcodpy.console_is_window_closed()

    def put_tile(self, x, y, symbol, color):
        libtcodpy.console_set_default_foreground(0, color)
        libtcodpy.console_put_char(0, x, y, symbol)

    def present(self):
        libtcodpy.console_flush()
