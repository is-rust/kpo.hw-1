import _path  # pyright: ignore
import unittest

from di import Container
from items.catalog import K_Bicycle


class TestContainer(unittest.TestCase):

    def test_shared_dependencies(self) -> None:
        context = Container()
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)

        self.assertIs(context.storage, context.storage)
        self.assertIs(context.manager, context.manager)
        self.assertTrue(context.manager.store(item))
        self.assertEqual(context.storage.filter(lambda _: True), [item])


if __name__ == '__main__':
    unittest.main()
