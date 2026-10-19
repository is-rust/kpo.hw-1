from typing import ClassVar, Self
from dataclasses import dataclass

from items.contracts import Vehicle, EnergyConsumer


@dataclass(repr=False)
class Bicycle(Vehicle):
    """Велосипед любого типа."""
    name: ClassVar[str] = "bicycle"

    def __post_init__(self: Self) -> None:
        if type(self) is Bicycle:
            raise TypeError('cannot instantiate abstract class Bicycle')
        super().__post_init__()


@dataclass(repr=False)
class K_Bicycle(Bicycle):
    """Классический велосипед."""
    name: ClassVar[str] = "k-bicycle"


@dataclass(repr=False)
class E_Bicycle(EnergyConsumer, Bicycle):
    """Электрический велосипед."""
    name: ClassVar[str] = "e-bicycle"

    def __post_init__(self):
        super().__post_init__()
