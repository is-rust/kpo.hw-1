from typing import ClassVar, Self
from abc import ABC

from dataclasses import dataclass


@dataclass
class Item(ABC):
    """Базовый предмет."""
    name: ClassVar[str]
    uuid: str

    brand: str
    model: str

    def __repr__(self: Self) -> str:
        return f'{{{self.name} #{self.uuid} // ({self.brand}, {self.model})}}'


@dataclass(repr=False)
class Vehicle(Item, ABC):
    """Транспорт."""
    ease: int


@dataclass(repr=False)
class EnergyConsumer(Item, ABC):
    """Потребитель энергии."""
    amount: float
