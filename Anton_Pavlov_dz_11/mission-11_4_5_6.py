class Warehouse:
    item: int = 0


class OfficeEquip(Warehouse):
    place = 'Склад'


class Printer(OfficeEquip):
    count: int = 0

    def new(self, *args):
        Warehouse.item += 1
        Printer.count += 1
        print(self.place, args, self.item)

    def replace(self, rep: str):
        self.place = rep
        print(f'Перемещен в {self.place}')


class Scaner(OfficeEquip):
    count: int = 0

    def new(self, *args):
        Warehouse.item += 1
        Scaner.count += 1
        print(self.place, args, self.item)

    def replace(self, rep: str):
        self.place = rep
        print(f'Перемещен в {self.place}')


class Xerox(OfficeEquip):
    count: int = 0

    def new(self, *args):
        Warehouse.item += 1
        Xerox.count += 1
        print(self.place, args, self.item)

    def replace(self, rep: str):
        self.place = rep
        print(f'Перемещен в {self.place}')


Printer().new('Фиолетовый', 'Портативный')
Scaner().new('Жёлтый', 'Портативный')
Xerox().new('Серый', 'Стационарный')
Xerox().replace('Офис')
