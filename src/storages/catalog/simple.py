from typing import Self, final, Callable

from items.contracts import Item
from storages.contracts import Storage


@final
class SimpleStorage(Storage):
    items: dict[str, Item]

    def __init__(self: Self, /) -> None:
        self.items = {}

    def store(self: Self, item: Item, /) -> bool:
        if item.uuid in self.items:
            return False
        
        self.items[item.uuid] = item
        return True

    def filter(self: Self, fn: Callable[[Item], bool]) -> list[Item]:
        return [*filter(fn, self.items.values())]
