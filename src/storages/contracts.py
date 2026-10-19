from typing import Protocol, Self, Callable
from items.contracts import Item


class Storage(Protocol):
    """Сервис хранения предметов."""

    def add(self: Self, item: Item, /) -> bool:
        """Добавляет на хранение переданный предмет."""
        ...

    def rem(self: Self, uuid: str, /) -> bool:
        """Забирает с хранения переданный предмет."""
        ...

    def filter(self: Self, fn: Callable[[Item], bool]) -> list[Item]:
        """Возвращает все предметы, удовлетворяющие фильтру."""
        ...
