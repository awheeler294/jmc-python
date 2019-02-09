import unittest

from ecs.entity import Entity

class TestEntity(unittest.TestCase):
    def test_getter_gets_set_values(self):
        e = Entity()
        expected = IntComponent(13)
        e.set(expected)

        actual = e.get(IntComponent)
        self.assertEqual(actual, expected)

    def test_set_overwrites_previous_value(self):
        e = Entity()
        expected = IntComponent(13)

        e.set(IntComponent(1888))
        e.set(expected)

        actual = e.get(IntComponent)
        self.assertEqual(actual, expected)

    def test_has_returns_true_if_component_exists(self):
        # Note: doesn't work for subclasses of the component
        e = Entity(IntComponent(77))
        self.assertTrue(e.has(IntComponent))
        self.assertFalse(e.has(StringComponent))

class IntComponent:
    def __init__(self, value):
        self.__inin__value = value


class StringComponent:
    def __init__(self, value):
        self.__init__value = str(value)


if __name__ == '__main__':
    unittest.main()
    #from pudb import set_trace; set_trace()
