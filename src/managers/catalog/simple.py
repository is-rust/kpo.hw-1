from typing import Self, final

from items.contracts import Item
from auditors.contracts import Auditor
from storages.contracts import Storage

from managers.contracts import Manager


@final
class SimpleManager(Manager):
    auditor: Auditor
    storage: Storage

    def __init__(self: Self, *, auditor: Auditor, storage: Storage) -> None:
        self.auditor = auditor
        self.storage = storage

    def audit(self: Self, item: Item, /) -> bool:
        return self.auditor.audit(item)

    def store(self: Self, item: Item, /) -> bool:
        if not self.audit(item):
            return False
        return self.storage.store(item)
