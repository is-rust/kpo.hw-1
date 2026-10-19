import _path  # pyright: ignore
import unittest

from app import App


class TestApp(unittest.TestCase):

    def test_available_items(self) -> None:
        app = App()

        self.assertIn('k-bicycle', app.items)
        self.assertIn('e-bicycle', app.items)
        self.assertIn('s-helmet', app.items)
        self.assertIn('c-charger', app.items)
        self.assertEqual(len(app.items), 8)


if __name__ == '__main__':
    unittest.main()
