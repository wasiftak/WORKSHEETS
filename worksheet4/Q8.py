import numpy as np
# Create two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix multiplication
matrix_multiplication = np.dot(A, B)
print("Matrix Multiplication (A * B):\n", matrix_multiplication)

# Transpose of Matrix A
transpose_A = np.transpose(A)
print("Transpose of Matrix A:\n", transpose_A)
