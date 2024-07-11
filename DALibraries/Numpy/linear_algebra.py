import numpy as np
from numpy.linalg import inv, eig, solve, det, norm, svd

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix multiplication
C = A @ B
print("Matrix Multiplication (A @ B):\n", C)

C_dot = np.dot(A, B)
print("Matrix Multiplication (np.dot(A, B)):\n", C_dot)

# Transpose of a matrix
A_transpose = A.T
print("Transpose of A:\n", A_transpose)

# Inverse of a matrix
A_inv = inv(A)
print("Inverse of A:\n", A_inv)

# Determinant of a matrix
A_det = det(A)
print("Determinant of A:", A_det)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

# Solve linear system Ax = b
b = np.array([1, 2])
x = solve(A, b)
print("Solution of Ax = b:", x)

# Singular Value Decomposition
U, sigma, Vt = svd(A)
print("U matrix:\n", U)
print("Sigma values:", sigma)
print("Vt matrix:\n", Vt)

# Matrix norm
A_norm = norm(A)
print("Frobenius norm of A:", A_norm)
