class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join(str(i) for i in stroka) for stroka in self.matrix)

    def __add__(self, other):
        try:
            return Matrix([[int(self.matrix[i][j]) + int(other.matrix[i][j]) for j in range(len(self.matrix[i]))]
                           for i in range(len(self.matrix))])
        except IndexError:
            return 'Матрицы разной размерности'


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = Matrix([[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(a)
print()
print(b)
print()
print('Сумма матриц\n', a + b)
