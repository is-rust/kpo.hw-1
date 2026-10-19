import _path  # pyright: ignore
import unittest

from items.contracts import Item, Vehicle, EnergyConsumer
from items.catalog import (
    K_Bicycle, E_Bicycle, K_Scooter, E_Scooter,
    S_Helmet, FF_Helmet, C_Charger, S_Charger,
)


class TestItems(unittest.TestCase):

    def test_vehicle_types(self) -> None:
        bicycle = E_Bicycle('1', 'xiaomi', 'm1', 6, 5)

        self.assertIsInstance(bicycle, Item)
        self.assertIsInstance(bicycle, Vehicle)
        self.assertIsInstance(bicycle, EnergyConsumer)

    def test_things_are_not_vehicles(self) -> None:
        helmet = S_Helmet('2', 'xiaomi', 'm2')
        charger = C_Charger('3', 'xiaomi', 'm3', 3)

        self.assertNotIsInstance(helmet, Vehicle)
        self.assertNotIsInstance(charger, Vehicle)
        self.assertIsInstance(charger, EnergyConsumer)

    def test_other_item_types(self) -> None:
        items = [
            K_Scooter('5', 'xiaomi', 'm5', 7),
            E_Scooter('6', 'xiaomi', 'm6', amount=3, ease=6),
            FF_Helmet('7', 'xiaomi', 'm7'),
            S_Charger('8', 'xiaomi', 'm8', 2),
        ]

        for item in items:
            self.assertIn(item.name, repr(item))

    def test_item_representation(self) -> None:
        bicycle = K_Bicycle('4', 'xiaomi', 'm4', 7)
        self.assertEqual(repr(bicycle), '{k-bicycle #4 // (xiaomi, m4)}')


if __name__ == '__main__':
    unittest.main()
