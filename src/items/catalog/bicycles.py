from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass
class Bicycle(Vehicle):
    """Велосипед любого типа."""
    name: ClassVar[str] = "bicycle"


@dataclass
class K_Bicycle(Bicycle):
    """Классический велосипед."""
    name: ClassVar[str] = "k-bicycle"


@dataclass
class E_Bicycle(Bicycle, EnergyConsumer):
    """Электрический велосипед."""
    name: ClassVar[str] = "e-bicycle"
    amount: float
