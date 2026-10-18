from typing import Self, final

from items.protocols import Item
from auditor.protocols import Auditor


@final
class BrandAuditor(Auditor):
    banned: list[str]

    def __init__(self: Self, banned: list[str], /) -> None:
        self.banned = banned

    def audit(self: Self, item: Item, /) -> bool:
        print(item.brand)
        return item.brand not in self.banned
