from typing import Protocol, Self
from items.protocols import Item


class Auditor(Protocol):
    """Сервис аудита предметов"""

    def audit(self: Self, item: Item, /) -> bool:
        """Проводит аудит переданного предмета"""
        ...
