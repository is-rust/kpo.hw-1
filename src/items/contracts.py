from typing import ClassVar, Self
from abc import ABC

from dataclasses import dataclass
import math


@dataclass
class Item(ABC):
    """Базовый предмет."""
    name: ClassVar[str]
    uuid: str

    brand: str
    model: str

    def __post_init__(self: Self) -> None:
        if type(self) is Item:
            raise TypeError('cannot instantiate abstract class Item')

    def __repr__(self: Self) -> str:
        return f'{{{self.name} #{self.uuid} // ({self.brand}, {self.model})}}'


@dataclass(repr=False)
class Vehicle(Item, ABC):
    """Транспорт."""
    ease: int

    def __post_init__(self: Self) -> None:
        if type(self) is Vehicle:
            raise TypeError('cannot instantiate abstract class Vehicle')

        if not 1 <= self.ease <= 10:
            raise ValueError('ease должен быть в диапазоне от 1 до 10')

        super().__post_init__()


@dataclass(repr=False)
class EnergyConsumer(Item, ABC):
    """Потребитель энергии."""
    amount: float

    def __post_init__(self: Self) -> None:
        if type(self) is EnergyConsumer:
            raise TypeError('cannot instantiate abstract class EnergyConsumer')

        if not math.isfinite(self.amount):
            raise ValueError('amount не может быть nan/inf')

        if self.amount < 0:
            raise ValueError('amount не может быть < 0')

        super().__post_init__()
