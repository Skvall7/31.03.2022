class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def make_order(self, number: int) -> str:
        long, core, make = 0, 0, ''
        while self.cells > core:
            if long == number:
                make += '\n'
                long = 0
            make += '*'
            long += 1
            core += 1
        return make

    def __int__(self):
        return self.cells

    def __add__(self, other):
        if type(other) != Cell:
            raise 'действие допустимо только для экземпляров того же класса'
        return Cell(self.cells + int(other))

    def __sub__(self, other):
        if type(other) != Cell:
            raise 'действие допустимо только для экземпляров того же класса'
        summa = Cell(self.cells - int(other))
        if int(summa) < 0:
            raise 'недопустимая операция'
        return summa

    def __mul__(self, other):
        if type(other) != Cell:
            raise 'действие допустимо только для экземпляров того же класса'
        return Cell(self.cells * int(other))

    def __truediv__(self, other):
        if type(other) != Cell:
            raise 'действие допустимо только для экземпляров того же класса'
        return Cell(self.cells // int(other))

    def __floordiv__(self, other):
        if type(other) != Cell:
            raise 'действие допустимо только для экземпляров того же класса'
        return Cell(self.cells // int(other))
    ...  # реализация других магических методов по заданию


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
