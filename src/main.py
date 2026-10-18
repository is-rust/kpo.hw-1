from typing import Self
from functools import cached_property

from items.contracts import Item
from items.catalog import *

from auditor.contracts import Auditor
from auditor.catalog import BrandAuditor

from storage.contracts import Storage
from storage.catalog import SimpleStorage

from manager.contracts import Manager
from manager.catalog import SimpleManager

# import sys


class Container:

    @cached_property
    def auditor(self: Self) -> Auditor:
        return BrandAuditor(['samsung'])

    @cached_property
    def storage(self: Self) -> Storage:
        return SimpleStorage()

    @cached_property
    def manager(self: Self) -> Manager:
        return SimpleManager(
            auditor=self.auditor,
            storage=self.storage,
        )


def get_total_energy_consumption(storage: Storage, /):
    return sum(map(lambda item: isinstance(item, EnergyConsumer) and item.amount, storage.filter(lambda item, /: isinstance(item, EnergyConsumer))))

def get_beginner_friendly_vehicles_list(storage: Storage, /) -> list[Item]:
    return storage.filter(lambda item, /: isinstance(item, Vehicle) and item.ease >= 6)

def get_all_items_list(storage: Storage, /) -> list[Item]:
    return storage.filter(lambda item, /: True)


def main() -> None:
    context = Container()

    storage = context.storage
    manager = context.manager

    manager.store(E_Bicycle(brand='samsung', model='M0', uuid='1', ease=5, amount=5))
    manager.store(E_Bicycle(brand='xiaomi', model='M0', uuid='2', ease=3, amount=10))
    manager.store(E_Bicycle(brand='xiaomi', model='M1', uuid='3', ease=10, amount=7))

    items = get_all_items_list(storage)
    print(f'Всего предметов ({len(items)}): {items}')

    items = get_beginner_friendly_vehicles_list(storage)
    print(f'Устройства для новичков ({len(items)}): {items}')

    amount = get_total_energy_consumption(storage)
    print(f'Суммарное потребление парка: {amount}')


if __name__ == '__main__':
    main()
