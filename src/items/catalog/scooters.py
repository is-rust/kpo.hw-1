from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass
class Scooter(Vehicle):
    """Самокат любого типа."""
    name: ClassVar[str] = "scooter"


@dataclass
class K_Scooter(Scooter):
    """Классический самокат."""
    name: ClassVar[str] = "k-scooter"


@dataclass
class E_Scooter(Scooter, EnergyConsumer):
    """Электрический самокат."""
    name: ClassVar[str] = "e-scooter"
    amount: float
