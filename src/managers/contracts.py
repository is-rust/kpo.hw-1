from typing import Protocol, Self
from items.contracts import Item


class Manager(Protocol):
    """Сервис аудита и хранения предметов."""

    def audit(self: Self, item: Item, /) -> bool:
        """Проводит аудит переданного предмета."""
        ...

    def store(self: Self, item: Item, /) -> bool:
        """Отправляет на хранение переданный предмет."""
        ...
