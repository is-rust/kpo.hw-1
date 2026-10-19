from typing import Protocol, Self
from items.contracts import Item


class Manager(Protocol):
    """Сервис аудита и хранения предметов."""

    def audit(self: Self, item: Item, /) -> bool:
        """Проводит аудит переданного предмета."""
        ...

    def add(self: Self, item: Item, /) -> bool:
        """Отправляет на хранение переданный предмет."""
        ...

    def rem(self: Self, uuid: str, /) -> bool:
        """Забирает с хранения переданный предмет."""
        ...
