import numpy as np

from src.matrix_operations import add_matrices, subtract_matrices, multiply_matrices, transpose_matrix

def test_add_matrices():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[6, 8], [10, 12]])
    assert np.array_equal(add_matrices(A, B), expected_result)