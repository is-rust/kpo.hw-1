from typing import Self
from functools import cached_property

from auditors.contracts import Auditor
from auditors.catalog import BrandAuditor

from storages.contracts import Storage
from storages.catalog import SimpleStorage

from managers.contracts import Manager
from managers.catalog import SimpleManager


class Container:

    @cached_property
    def auditor(self: Self) -> Auditor:
        return BrandAuditor(['samsung'])

    @cached_property
    def storage(self: Self) -> Storage:
        return SimpleStorage()

    @cached_property
    def manager(self: Self) -> Manager:
        return SimpleManager(
            auditor=self.auditor,
            storage=self.storage,
        )
