from typing import Self, Any
from dataclasses import fields

from utils import (
    get_all_items_list,
    get_total_energy_consumption,
    get_beginner_friendly_vehicles_list
)
from di import Container

from items.contracts import Item
from items.catalog import (
    K_Bicycle, E_Bicycle,
    K_Scooter, E_Scooter,
    C_Charger, S_Charger,
    S_Helmet, FF_Helmet
)


class App:
    uuid: int

    def __init__(self: Self) -> None:
        self.uuid = 0

        self.context = Container()
        self.storage = self.context.storage
        self.manager = self.context.manager

        self.items: dict[str, type[Item]] = {
            item.name: item for item in [
                K_Bicycle, E_Bicycle,
                K_Scooter, E_Scooter,
                C_Charger, S_Charger,
                S_Helmet, FF_Helmet
            ]
        }

    def info(self: Self) -> None:
        print('-' * 32)
        print('## Состояние парка')
        amount = get_total_energy_consumption(self.storage)
        print(f'Потребление: {amount} кВт*ч')
        print()

        items = get_all_items_list(self.storage)
        print(f'Предметов ({len(items)} шт): {items}')

        items = get_beginner_friendly_vehicles_list(self.storage)
        print(f'- Для новичков ({len(items)} шт): {items}')

        print('\n')

    def add(self: Self) -> None:
        for ind, name in enumerate(self.items.keys(), 1):
            print(f'({ind}) {name}')

        name = input('Введите имя/номер: ')

        if name.isdecimal():
            keys = list(self.items)
            if 0 <= int(name) - 1 < len(keys):
                name = keys[int(name) - 1]

        if name in self.items:
            print()

            item = self.items[name]
            args: list[Any] = []

            for field in fields(item)[1:]:

                if isinstance(field.type, str):
                    continue

                text = f'Введите {field.name} (тип {field.type.__name__}): '
                success = False

                while not success:
                    try:
                        v = input(text)
                        args.append(field.type(v))
                        success = True
                    except EOFError as e:
                        raise e
                    except Exception as e:
                        print(f'Ошибка: {e}\n')

            try:
                args = [str(self.uuid), *args]

                status = self.manager.add(item(*args))
                if status: print('Предмет добавлен')
                else:      print('Предмет отклонен')

                self.uuid += 1

            except Exception as e:
                print(f'\nОшибка: {e}')

        else:
            print('Такого предмета нет!')

    def rem(self: Self) -> None:
        uuid = input('Введите uuid: ')
        status = self.manager.rem(uuid)

        if status: print('Предмет удален')
        else:      print('Предмет не найден')
        
    def cmds(self: Self) -> None:
        print("Что хотите сделать?")
        print("(a) Добавить предмет")
        print("(r) Удалить предмет")
        print("(q) Выйти из программы")

        cmd = input('Команда: ')
        print()

        if cmd == 'q': exit(0)
        elif cmd == 'a': self.add()
        elif cmd == 'r': self.rem()
        else: print('Неизвестная команда')

        print()

    def process(self: Self) -> None:
        try:
            while True:
                self.info()
                self.cmds()
        except (Exception, KeyboardInterrupt):
            print('\nЧто-то пошло не так...')
