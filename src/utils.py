from items.contracts import Item, EnergyConsumer, Vehicle
from storages.contracts import Storage


def get_total_energy_consumption(storage: Storage, /):
    items = storage.filter(lambda item, /: isinstance(item, EnergyConsumer))
    return sum(item.amount for item in items if isinstance(item, EnergyConsumer))


def get_beginner_friendly_vehicles_list(storage: Storage, /) -> list[Item]:
    return storage.filter(lambda item, /: isinstance(item, Vehicle) and item.ease >= 6)


def get_all_items_list(storage: Storage, /) -> list[Item]:
    return storage.filter(lambda item, /: True)
