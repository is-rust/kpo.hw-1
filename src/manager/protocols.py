from typing import Protocol, Self
from items.protocols import Item


class Manager(Protocol):
    """ """

    def audit(self: Self, item: Item, /) -> bool: ...
    def store(self: Self, item: Item, /) -> bool: ...
