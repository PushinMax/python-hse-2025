from __future__ import annotations
import numpy as np
from functools import lru_cache

class Operation:
    def __sub__(self, other: Matrix):
        return self + Matrix([[-1 for _ in i] for i in self.matrix]) * other
    
    def __iadd__(self, other: Matrix):
        self = self + other
        return self

    def __isub__(self, other: Matrix):
        self = self - other
        return self

    def __imul__(self, other: Matrix):
        self = self * other
        return self

    def __imatmul__(self, other: Matrix):    
        self = self @ other
        return self
    


class Display:
    def __str__(self):
        return str(np.array(self.matrix))
    
    # без поддержки срезов
    def __getitem__(self, index):
        if isinstance(index, tuple):
            return self.matrix[index[0]][index[1]]
        else:
            return self.matrix[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            self.matrix[index[0]][index[1]] = value
        else:
            self.matrix[index] = value
    

class FileIO:
    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.matrix))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            data = eval(f.read())
        return cls(data)

class HashMatrix:
    def __hash__(self):
        # Сумма всех элементов + длинна
        return sum(sum(row) for row in self.matrix) + len(self.matrix)

class Matrix(Display, FileIO, HashMatrix, Operation):
    def __init__(self, matrix: list[list[int]]):
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("Все стороки должны быть 1 длинны")
        self.matrix = matrix

    def __add__(self, other: Matrix):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размеры таблиц должны быть одинаковые")

        return Matrix([[a + b for a, b in zip(row_a, row_b)] 
                      for row_a, row_b in zip(self.matrix, other.matrix)])


    def __mul__(self, other: Matrix):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размеры таблиц должны быть одинаковые")

        return Matrix([[a * b for a, b in zip(row_a, row_b)] 
                      for row_a, row_b in zip(self.matrix, other.matrix)])


    @lru_cache(maxsize=None)
    def __matmul__(self, other: Matrix):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")
        m = len(self.matrix)
        n = len(other.matrix)
        p = len(other.matrix[0])
        result = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix(result)

    def __eq__(self, other):
        return self.matrix == other.matrix            