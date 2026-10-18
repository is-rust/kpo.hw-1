from typing import Protocol, Self
from items.protocols import Item


class Storage(Protocol):
    """ """

    def store(self: Self, item: Item, /) -> bool: ...
