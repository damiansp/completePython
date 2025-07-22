from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class ModernChair(Chair):
    def sit_on(self):
        return 'Sitting on a modern chair'


class VictorianChair(Chair):
    def sit_on(self):
        return 'Sitting on a Victorian chair'


class Table(ABC):
    @abstractmethod
    def put_on(self):
        pass


class ModernTable(Table):
    def put_on(self):
        return 'Putting item on a modern table'


class VictorianTable(Table):
    def put_on(self):
        return 'Putting item on a Victorian table'


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()


    def create_table(self):
        return VictorianTable()


def client_code(factory):
    chair = factory.create_chair()
    table = factory.create_table()
    print(chair.sit_on())
    print(table.put_on())


def main():
    mod_fac = ModernFurnitureFactory()
    vic_fac = VictorianFurnitureFactory()
    print('Mod:')
    client_code(mod_fac)
    print('\nVic:')
    client_code(vic_fac)


main()


