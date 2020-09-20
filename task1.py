"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([' '.join([str(el) for el in line]) for line in self.matrix]))

    def __add__(self, other):
        matrix_new = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix_new[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return matrix_new


matrix_1 = Matrix([[22, 11, 10], [33, 1, 14], [10, 16, 1]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [3, 2, 1]])
print(f'Матрица 1:\n{matrix_1}')
print(f'Матрица 2:\n{matrix_2}')

matrix_3 = Matrix(matrix_1.__add__(matrix_2))
print(f'Сумма двух матриц:\n{matrix_3}')