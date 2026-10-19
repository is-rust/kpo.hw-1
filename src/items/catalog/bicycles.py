from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass(repr=False)
class Bicycle(Vehicle):
    """Велосипед любого типа."""
    name: ClassVar[str] = "bicycle"


@dataclass(repr=False)
class K_Bicycle(Bicycle):
    """Классический велосипед."""
    name: ClassVar[str] = "k-bicycle"


@dataclass(repr=False)
class E_Bicycle(Bicycle, EnergyConsumer):
    """Электрический велосипед."""
    name: ClassVar[str] = "e-bicycle"
