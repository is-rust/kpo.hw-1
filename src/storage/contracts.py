from typing import Protocol, Self, Callable
from items.contracts import Item


class Storage(Protocol):
    """Сервис хранения предметов."""

    def store(self: Self, item: Item, /) -> bool:
        """Добавляет предмет на хранение."""
        ...

    def filter(self: Self, fn: Callable[[Item], bool]) -> list[Item]:
        """Возвращает все предметы, удовлетворяющие фильтру."""
        ...
