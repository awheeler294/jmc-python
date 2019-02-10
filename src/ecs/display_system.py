import tcod as libtcodpy

from ecs.components.display_component import DisplayComponent

class DisplaySystem:

    def __init__(self):
        self._root_console = libtcodpy.console_init_root(80, 50)

    def update(self, entities):
        self._root_console.clear()

        for e in entities:
            dc = e.get(DisplayComponent)
            self._root_console.draw_char(dc.x, dc.y, dc.character, dc.color)
