from __future__ import annotations
import numpy as np


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def __get__(self, i, j):
        return self.matrix[i][j]
    def __str__(self):


    def __add__(self, other: Matrix):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размеры таблиц должны быть одинаковые")

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] += other.matrix[i][j]


    def __mul__(self, other: int):
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

        self.matrix = result


    def __matmul__(self, other: Matrix):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размеры таблиц должны быть одинаковые")

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] *= other.matrix[i][j]