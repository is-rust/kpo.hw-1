from typing import ClassVar
from dataclasses import dataclass

from items.contracts import EnergyConsumer


@dataclass(repr=False)
class Charger(EnergyConsumer):
    """Зарядник любого типа."""
    name: ClassVar[str] = "charger"


@dataclass(repr=False)
class C_Charger(Charger):
    """Зарядник машин."""
    name: ClassVar[str] = "c-charger"


@dataclass(repr=False)
class S_Charger(Charger):
    """Зарядник самокатов."""
    name: ClassVar[str] = "s-charger"
