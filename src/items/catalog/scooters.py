from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass(repr=False)
class Scooter(Vehicle):
    """Самокат любого типа."""
    name: ClassVar[str] = "scooter"


@dataclass(repr=False)
class K_Scooter(Scooter):
    """Классический самокат."""
    name: ClassVar[str] = "k-scooter"


@dataclass(repr=False)
class E_Scooter(Scooter, EnergyConsumer):
    """Электрический самокат."""
    name: ClassVar[str] = "e-scooter"
