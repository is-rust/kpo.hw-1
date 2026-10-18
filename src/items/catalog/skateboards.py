from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass
class Skateboard(Vehicle):
    """Скейтборд любого типа."""
    name: ClassVar[str] = "skateboard"


@dataclass
class K_Skateboard(Skateboard):
    """Классический скейтборд."""
    name: ClassVar[str] = "k-skateboard"


@dataclass
class E_Skateboard(Skateboard, EnergyConsumer):
    """Электрический скейтборд."""
    name: ClassVar[str] = "e-skateboard"
    amount: float
