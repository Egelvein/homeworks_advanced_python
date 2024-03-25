from matrix_oper_and_hash import Matrix
import numpy as np


def hash_function(val, seed, hash_val):
    # The equation, from which to express val for reverse hashing

    return val ** 3 + seed * val - 2 * val - hash_val


def unhash(S, H, a, b, tolerance=1e-6, max_iterations=1000):
    if hash_function(a, S, H) * hash_function(b, S, H) >= 0:
        print("Не удается найти корень на заданном интервале.")
        return None

    else:
        iteration = 0
        while (b - a) / 2.0 > tolerance and iteration < max_iterations:
            midpoint = (a + b) / 2.0
            
            if hash_function(midpoint, S, H) == 0:
                return midpoint
            
            elif hash_function(a, S, H) * hash_function(midpoint, S, H) < 0:
                b = midpoint
            
            else:
                a = midpoint
            
            iteration += 1
        
        return (a + b) / 2.0


np.random.seed(0)

A = np.random.randint(0, 10, (10, 10))
B = np.random.randint(0, 10, (10, 10))
C = np.random.randint(0, 10, (10, 10))
D = np.random.randint(0, 10, (10, 10))

np.savetxt('artifacts/3.3/A.txt', A, fmt='%d')
np.savetxt('artifacts/3.3/B.txt', B, fmt='%d')
np.savetxt('artifacts/3.3/C.txt', C, fmt='%d')
np.savetxt('artifacts/3.3/D.txt', D, fmt='%d')

A = Matrix(A)
B = Matrix(B)
C = Matrix(C)
D = Matrix(D)

AB = A @ B
CD = C @ D


hash_AB, len_hash_AB = AB.hash_counter()
hash_CD, _ = CD.hash_counter()


### Unhash matrix AB and save it to file for comparing
hash_matrix0 = []

for k in range (len(hash_AB)//len_hash_AB):
    hash_num = hash_AB[k*len_hash_AB : (k+1)*len_hash_AB]
    hash_num1 = hash_num.lstrip('0')
    
    if hash_num1 == '':
        hash_num1 = 0
    
    hash_matrix0.append(int(hash_num1))

hash_matrix = np.array(hash_matrix0).reshape(AB.rows, AB.cols)

S = 42 # seed
a = -1 # left border of the interval
b = 100 # right border of the interval

for i in range(len(hash_matrix)):
    for j in range(len(hash_matrix[0])):
        H = hash_matrix[i][j]
        value = unhash(S, H, a, b)
        
        if value is None:
            print('Error: ', i, j)
            hash_matrix[i][j] = 777
        
        else:
            hash_matrix[i][j] = round(value)

AB.save_file('artifacts/3.3/AB.txt')
CD.save_file('artifacts/3.3/CD.txt')
with open('Unhash_AB', 'w') as f:
    for row in hash_matrix:
        f.write(' '.join(map(str, row)) + '\n')

with open('artifacts/3.3/hash.txt', 'w') as f:
    f.write(f'Hash AB: {hash_AB}\n')
    f.write(f'Hash CD: {hash_CD}')


if hash_AB == hash_CD:
    print('Collision')
else:
    print('No collision')

