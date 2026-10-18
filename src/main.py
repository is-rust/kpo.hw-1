from typing import Self
from functools import cached_property

from items.catalog import *

from auditor.protocols import Auditor
from auditor.catalog import BrandAuditor

from storage.protocols import Storage
from storage.catalog import SimpleStorage

from manager.protocols import Manager
from manager.catalog import SimpleManager

# import sys


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


def main() -> None:
    context = Container()
    manager = context.manager

    manager.store(EBicycle(model='1', brand='samsung', uuid='5', ease=5))
    manager.store(EBicycle(model='1', brand='samsung', uuid='6', ease=5))


if __name__ == '__main__':
    main()
