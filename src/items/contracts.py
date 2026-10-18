from typing import ClassVar
from abc import ABC

from dataclasses import dataclass


@dataclass
class Item(ABC):
    """Базовый предмет."""
    name: ClassVar[str]
    uuid: str

    brand: str
    model: str


@dataclass
class Vehicle(Item, ABC):
    """Транспорт."""
    ease: int


@dataclass
class EnergyConsumer(Item, ABC):
    """Потребитель энергии."""
    amount: float
