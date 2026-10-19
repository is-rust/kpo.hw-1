import _path  # pyright: ignore
import unittest

from items.catalog import K_Bicycle, E_Bicycle, S_Helmet, C_Charger
from storages.catalog import SimpleStorage

from utils import (
    get_all_items_list,
    get_total_energy_consumption,
    get_beginner_friendly_vehicles_list,
)


class TestUtils(unittest.TestCase):

    def test_energy_consumption(self) -> None:
        storage = SimpleStorage()

        storage.add(E_Bicycle('1', 'xiaomi', 'm1', amount=5, ease=8))
        storage.add(K_Bicycle('2', 'xiaomi', 'm2', 7))
        storage.add(C_Charger('3', 'xiaomi', 'm3', 3))
        storage.add(S_Helmet('4', 'xiaomi', 'm4'))

        self.assertEqual(get_total_energy_consumption(storage), 8)

    def test_energy_consumption_empty(self) -> None:
        self.assertEqual(get_total_energy_consumption(SimpleStorage()), 0)

    def test_beginner_friendly_vehicles(self) -> None:
        storage = SimpleStorage()

        bicycle_5 = K_Bicycle('1', 'xiaomi', 'm1', 5)
        storage.add(bicycle_5)

        bicycle_6 = K_Bicycle('2', 'xiaomi', 'm2', 6)
        storage.add(bicycle_6)

        helmet = S_Helmet('3', 'xiaomi', 'm3')
        storage.add(helmet)

        self.assertEqual(get_beginner_friendly_vehicles_list(storage), [bicycle_6])

    def test_all_items(self) -> None:
        storage = SimpleStorage()
        
        bicycle = K_Bicycle('1', 'xiaomi', 'm1', 7)
        storage.add(bicycle)

        helmet = S_Helmet('2', 'xiaomi', 'm2')
        storage.add(helmet)

        self.assertEqual(get_all_items_list(storage), [bicycle, helmet])


if __name__ == '__main__':
    unittest.main()
