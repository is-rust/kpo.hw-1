from typing import Protocol, ClassVar


class Item(Protocol):
    """ """
    name: ClassVar[str]

    model: str
    brand: str

    uuid: str


class EnergyConsumer(Item, Protocol):
    """ """
    amount: float


class Vehicle(Item, Protocol):
    """ """
    ease: int
