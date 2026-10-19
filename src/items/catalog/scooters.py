from typing import ClassVar, Self
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass(repr=False)
class Scooter(Vehicle):
    """Самокат любого типа."""
    name: ClassVar[str] = "scooter"

    def __post_init__(self: Self) -> None:
        if type(self) is Scooter:
            raise TypeError('cannot instantiate abstract class Scooter')
        super().__post_init__()


@dataclass(repr=False)
class K_Scooter(Scooter):
    """Классический самокат."""
    name: ClassVar[str] = "k-scooter"


@dataclass(repr=False)
class E_Scooter(EnergyConsumer, Scooter):
    """Электрический самокат."""
    name: ClassVar[str] = "e-scooter"

    def __post_init__(self):
        super().__post_init__()
