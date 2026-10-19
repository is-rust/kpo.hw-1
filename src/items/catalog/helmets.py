from typing import ClassVar, Self
from dataclasses import dataclass

from items.contracts import Item


@dataclass(repr=False)
class Helmet(Item):
    """Шлем любого типа."""
    name: ClassVar[str] = "helmet"

    def __post_init__(self: Self) -> None:
        if type(self) is Helmet:
            raise TypeError('cannot instantiate abstract class Helmet')
        super().__post_init__()


@dataclass(repr=False)
class S_Helmet(Helmet):
    """Велосипедный шлем."""
    name: ClassVar[str] = "s-helmet"


@dataclass(repr=False)
class FF_Helmet(Helmet):  # FF - Full Face
    """Мотоциклетный шлем."""
    name: ClassVar[str] = "ff-helmet"
