from typing import List
import re


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(self.matrix) != 3:
            print(f'Некорректная матрица: {self.matrix}')
        for column in self.matrix:
            if len(column) != 2:
                print(f'Некорректная матрица: {self.matrix}')
        return

    def __str__(self):
        line = f'| {self.matrix[0][0]} {self.matrix[0][1]} |\n' \
                 f'| {self.matrix[1][0]} {self.matrix[1][1]} |\n' \
                 f'| {self.matrix[2][0]} {self.matrix[2][1]} |'
        return line

    def __add__(self, other):
        new = [[0, 0], [0, 0], [0, 0]]
        il = 0
        RE_Matrix = re.compile(r'\W{2}(\d+)\s(\d+)')
        other_m = RE_Matrix.findall(str(other))
        while len(self.matrix) != il:
            ic = 0
            while len(self.matrix[il]) != ic:
                new[il][ic] = self.matrix[il][ic] + int(other_m[il][ic])
                ic += 1
            il += 1
        new_p = f'| {new[0][0]} {new[0][1]} |\n| {new[1][0]} {new[1][1]} |\n| {new[2][0]} {new[2][1]} |'
        return new_p


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])