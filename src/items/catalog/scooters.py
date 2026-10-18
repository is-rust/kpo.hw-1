from typing import ClassVar, final
from items.protocols import Vehicle


class Scooter(Vehicle):
    """ """
    model: str
    brand: str

    uuid: str
    ease: int


@final
class EScooter(Scooter):
    """ """
    name: ClassVar[str] = "e-scooter"


@final
class KScooter(Scooter):
    """ """
    name: ClassVar[str] = "k-scooter"

