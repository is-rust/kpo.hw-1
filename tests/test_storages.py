import _path  # pyright: ignore
import unittest

from items.catalog import K_Bicycle, S_Helmet
from storages.catalog import SimpleStorage


class TestStorages(unittest.TestCase):

    def test_store_item(self) -> None:
        storage = SimpleStorage()
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)

        self.assertTrue(storage.store(item))
        self.assertEqual(storage.filter(lambda _: True), [item])

    def test_duplicate_uuid(self) -> None:
        storage = SimpleStorage()
        first = K_Bicycle('1', 'xiaomi', 'm1', 7)
        second = S_Helmet('1', 'xiaomi', 'm2')

        self.assertTrue(storage.store(first))
        self.assertFalse(storage.store(second))
        self.assertEqual(storage.filter(lambda _: True), [first])

    def test_filter_items(self) -> None:
        storage = SimpleStorage()

        bicycle = K_Bicycle('1', 'xiaomi', 'm1', 7)
        storage.store(bicycle)
        
        helmet = S_Helmet('2', 'xiaomi', 'm2')
        storage.store(helmet)

        self.assertEqual(storage.filter(lambda item: item.uuid == '2'), [helmet])
        self.assertEqual(storage.filter(lambda item: item.uuid == '3'), [])


if __name__ == '__main__':
    unittest.main()
