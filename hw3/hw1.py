from numpy import random
from matrix_oper import Matrix

random.seed(0)

matrix1_data = [[random.randint(0, 9) for _ in range(10)] for _ in range(10)]
matrix2_data = [[random.randint(0, 9) for _ in range(10)] for _ in range(10)]

# matrix1_data = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# matrix2_data = [[0.1, 0.2, 0.3],
#         [0.4, 0.5, 0.6],
#         [0.7, 0.8, 0.9]]


matrix1 = Matrix(matrix1_data)
matrix2 = Matrix(matrix2_data)

result_add = matrix1 + matrix2
result_matrix_multiplication = matrix1 * matrix2
result_Hadamard_product = matrix1 @ matrix2

result_add.save_file('artifacts/3.1/matrix+.txt')
result_matrix_multiplication.save_file('artifacts/3.1/matrix*.txt')
result_Hadamard_product.save_file('artifacts/3.1/matrix@.txt')
