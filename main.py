import numpy as np

from src.matrix_operations import add_matrices, subtract_matrices, multiply_matrices, transpose_matrix

A = np.loadtxt('data/matrix_A.csv', delimiter=',')
B = np.loadtxt('data/matrix_B.csv', delimiter=',')

print("A + B:")
print(add_matrices(A, B))

print("\nA - B:")
print(subtract_matrices(A, B))

print("\nA x B:")
print(multiply_matrices(A, B))

print("\nA^T:")
print(transpose_matrix(A))