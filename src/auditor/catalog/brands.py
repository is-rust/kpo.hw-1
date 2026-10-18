from typing import Self, final

from items.contracts import Item
from auditor.contracts import Auditor


@final
class BrandAuditor(Auditor):
    banned: list[str]

    def __init__(self: Self, banned: list[str], /) -> None:
        self.banned = banned

    def audit(self: Self, item: Item, /) -> bool:
        return item.brand not in self.banned
