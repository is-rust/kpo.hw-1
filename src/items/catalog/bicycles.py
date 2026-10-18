from typing import ClassVar, final
from dataclasses import dataclass

from items.protocols import Vehicle


@dataclass
class Bicycle(Vehicle):
    """ """
    model: str
    brand: str

    uuid: str
    ease: int


@final
class EBicycle(Bicycle):
    """ """
    name: ClassVar[str] = "e-bicycle"


@final
class KBicycle(Bicycle):
    """ """
    name: ClassVar[str] = "k-bicycle"
