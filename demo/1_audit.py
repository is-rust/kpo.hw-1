import _path  # pyright: ignore
from items.catalog import *

from utils import *
from container import Container


def main() -> None:
    context = Container()

    manager = context.manager
    manager.store(E_Bicycle(uuid='1', brand='samsung', model='m0', amount=5, ease=5))
    manager.store(E_Bicycle(uuid='2', brand='xiaomi', model='m0', amount=5, ease=10))

    storage = context.storage
    print(get_all_items_list(storage))


if __name__ == '__main__':
    main()
