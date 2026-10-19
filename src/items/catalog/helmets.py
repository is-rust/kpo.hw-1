from typing import ClassVar
from dataclasses import dataclass

from items.contracts import Item


@dataclass(repr=False)
class Helmet(Item):
    """Шлем любого типа."""
    name: ClassVar[str] = "helmet"


@dataclass(repr=False)
class S_Helmet(Helmet):
    """Велосипедный шлем."""
    name: ClassVar[str] = "s-helmet"


@dataclass(repr=False)
class FF_Helmet(Helmet):  # FF - Full Face
    """Мотоциклетный шлем."""
    name: ClassVar[str] = "ff-helmet"
