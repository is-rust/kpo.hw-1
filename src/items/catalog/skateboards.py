from typing import ClassVar, final
from items.protocols import Vehicle


class Skateboard(Vehicle):
    """ """
    name: ClassVar[str] = "skateboard"

    model: str
    brand: str

    uuid: str
    ease: int


@final
class ESkateboard(Skateboard):
    """ """
    name: ClassVar[str] = "e-skateboard"


@final
class KSkateboard(Skateboard):
    """ """
    name: ClassVar[str] = "k-skateboard"
