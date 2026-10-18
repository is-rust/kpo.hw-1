from typing import Self, final

from items.protocols import Item
from storage.protocols import Storage


@final
class SimpleStorage(Storage):
    """ """
    items: list[Item]

    def __init__(self: Self, /) -> None:
        self.items = []

    def store(self: Self, item: Item, /) -> bool:
        self.items.append(item)
        return True
