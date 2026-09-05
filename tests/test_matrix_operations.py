import numpy as np

from src.matrix_operations import add_matrices, subtract_matrices, multiply_matrices, transpose_matrix

def test_add_matrices():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected_result = np.array([[6, 8], [10, 12]])
    assert np.array_equal(add_matrices(A, B), expected_result)

def test_subtract_matrices():
    A = np.array([[5, 6], [7, 8]])
    B = np.array([[1, 2], [3, 4]])
    expected_result = np.array([[4, 4], [4, 4]])
    assert np.array_equal(subtract_matrices(A, B), expected_result)

def test_multiply_matrices():
    A = np.array([[5, 6], [7, 8]])
    B = np.array([[1, 2], [3, 4]])
    expected_result = np.array([[5, 12], [21, 32]])
    assert np.array_equal(multiply_matrices(A, B), expected_result)
    
def test_transpose_matrix():
    A = np.array([[1, 2], [3, 4]])
    expected_result = np.array([[1, 3], [2, 4]])
    assert np.array_equal(transpose_matrix(A), expected_result)