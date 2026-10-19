from typing import ClassVar, Self
from dataclasses import dataclass

from items.contracts import EnergyConsumer


@dataclass(repr=False)
class Charger(EnergyConsumer):
    """Зарядник любого типа."""
    name: ClassVar[str] = "charger"

    def __post_init__(self: Self) -> None:
        if type(self) is Charger:
            raise TypeError('cannot instantiate abstract class Charger')
        super().__post_init__()


@dataclass(repr=False)
class C_Charger(Charger):
    """Зарядник машин."""
    name: ClassVar[str] = "c-charger"


@dataclass(repr=False)
class S_Charger(Charger):
    """Зарядник самокатов."""
    name: ClassVar[str] = "s-charger"
