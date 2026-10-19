import _path  # pyright: ignore
import unittest

from items.catalog import K_Bicycle
from auditors.catalog import BrandAuditor


class TestAuditors(unittest.TestCase):

    def test_allowed_brand(self) -> None:
        auditor = BrandAuditor(['samsung'])
        item = K_Bicycle('1', 'xiaomi', 'm1', 7)
        self.assertTrue(auditor.audit(item))

    def test_banned_brand(self) -> None:
        auditor = BrandAuditor(['samsung'])
        item = K_Bicycle('1', 'samsung', 'm1', 7)
        self.assertFalse(auditor.audit(item))


if __name__ == '__main__':
    unittest.main()
