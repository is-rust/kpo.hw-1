import _path  # pyright: ignore
import unittest

from items.contracts import Item
from items.catalog import K_Bicycle

from managers.catalog import SimpleManager
from storages.catalog import SimpleStorage


class FakeAuditor:

    def __init__(self, result: bool) -> None:
        self.result = result

    def audit(self, item: Item, /) -> bool:
        return self.result


class TestManagers(unittest.TestCase):

    def test_accepted_item(self) -> None:
        storage = SimpleStorage()
        manager = SimpleManager(auditor=FakeAuditor(True), storage=storage)
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)

        self.assertTrue(manager.store(item))
        self.assertEqual(storage.filter(lambda _: True), [item])

    def test_rejected_item(self) -> None:
        storage = SimpleStorage()
        manager = SimpleManager(auditor=FakeAuditor(False), storage=storage)
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)

        self.assertFalse(manager.store(item))
        self.assertEqual(storage.filter(lambda _: True), [])

    def test_audit_method(self) -> None:
        manager = SimpleManager(auditor=FakeAuditor(False), storage=SimpleStorage())
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)

        self.assertFalse(manager.audit(item))


if __name__ == '__main__':
    unittest.main()
