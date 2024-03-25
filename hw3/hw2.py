import numpy as np


class MatrixOperations(np.lib.mixins.NDArrayOperatorsMixin):
    def __str__(self):
        return str(self._matrix)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    def save_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self._matrix))


np.random.seed(0)

matrix1_data = np.random.randint(0, 10, (10, 10))
matrix2_data = np.random.randint(0, 10, (10, 10))

matrix1 = np.array(matrix1_data)
matrix2 = np.array(matrix2_data)

res_add = MatrixOperations()
res_sub = MatrixOperations()
res_mul = MatrixOperations()
res_div = MatrixOperations()
res_Ham = MatrixOperations()

res_add.matrix = matrix1 + matrix2
res_sub.matrix = matrix1 - matrix2
res_mul.matrix = matrix1 * matrix2
res_div.matrix = matrix1 / matrix2
res_Ham.matrix = matrix1 @ matrix2

res_add.save_file('artifacts/3.2/matrix+.txt')
res_sub.save_file('artifacts/3.2/matrix-.txt')
res_mul.save_file('artifacts/3.2/matrix*.txt')
# res_div.save_file('artifacts/3.2/matrix_div.txt')
res_Ham.save_file('artifacts/3.2/matrix@.txt')
