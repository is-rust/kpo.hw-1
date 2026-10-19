from typing import Self, Any
from dataclasses import fields

from utils import *
from di import Container

from items.catalog import *


ESC = '\x1b'

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

    def update(self: Self) -> None:
        print('### Состояние парка ###')
        amount = get_total_energy_consumption(self.storage)
        print(f'Потребление: {amount} кВт*ч')
        print()

        items = get_all_items_list(self.storage)
        print(f'Предметов ({len(items)} шт): {items}')

        items = get_beginner_friendly_vehicles_list(self.storage)
        print(f'- Для новичков ({len(items)} шт): {items}')

        print()

        print("Что хотите сделать?")
        print("(a) Добавить предмет")
        print("(q) Выйти из программы")

        cmd = input('Команда: ')

        if cmd == 'q':
            exit(0)

        print()
        for ind, name in enumerate(self.items.keys(), 1):
            print(f'({ind}) {name}')

        name = input('Введите имя: ')

        if name.isdecimal():
            keys = list(self.items)
            if 0 <= int(name) - 1 < len(keys):
                name = keys[int(name) - 1]

        if name in self.items:
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
                    except Exception:
                        pass

            self.manager.store(self.items[name](str(self.uuid), *args))
            self.uuid += 1

        print(f'{ESC}[H{ESC}[2J{ESC}[3J')

    def process(self: Self) -> None:
        try:
            while True: self.update()    
        except (Exception, KeyboardInterrupt):
            print('\nЧто-то пошло не так...')
