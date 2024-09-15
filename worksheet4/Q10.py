import numpy as np

# Create a 3x3 matrix
A = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print("Matrix A:\n", A)

# Find determinant of matrix A
determinant = np.linalg.det(A)
print("Determinant of Matrix A:", determinant)
