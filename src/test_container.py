import unittest

from ecs.container import Container
from ecs.entity import Entity

class TestContainer(unittest.TestCase):
    def test_add_system_adds_systems(self):
        s1 = DummySystem()
        s2 = DummySystem()
        c = Container()
        c.add_system(s1)

        self.assertIn(s1, c._systems)
        self.assertNotIn(s2, c._systems)

    def test_add_entity_adds_it_to_entities(self):
        e = Entity()
        c = Container()
        c.add_entity(e)

        self.assertIn(e, c._entities)

    def test_update_calls_update_on_all_systems(self):
        c = Container()
        s1 = DummySystem()
        c.add_system(s1)
        c.update()

        s2 = DummySystem()
        c.add_system(s2)
        c.update()
        self.assertEqual(s1.update_calls, 2)
        self.assertEqual(s2.update_calls, 1)


class DummySystem():
    def __init__(self):
        self.update_calls = 0

    def update(self, entities):
        self.update_calls += 1


if __name__ == '__main__':
    unittest.main()
