import numpy as np
from scipy import linalg
from scipy.linalg import expm

# 1. Creating Matrices
print("1. Creating Matrices")

# Using np.array()
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Basic matrix:\n", matrix)

# Using np.zeros(), np.ones(), np.eye()
zero_matrix = np.zeros((3, 3))
ones_matrix = np.ones((3, 3))
identity_matrix = np.eye(3)
print("\nZero matrix:\n", zero_matrix)
print("\nOnes matrix:\n", ones_matrix)
print("\nIdentity matrix:\n", identity_matrix)

# Using np.arange() or np.linspace()
range_matrix = np.arange(9).reshape(3, 3)
linear_space_matrix = np.linspace(0, 1, 9).reshape(3, 3)
print("\nRange matrix:\n", range_matrix)
print("\nLinear space matrix:\n", linear_space_matrix)

# Using np.random for random matrices
random_matrix = np.random.rand(3, 3)
print("\nRandom matrix:\n", random_matrix)

# 2. Basic Matrix Operations
print("\n2. Basic Matrix Operations")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition and Subtraction
sum_matrix = A + B
diff_matrix = A - B
print("\nSum of A and B:\n", sum_matrix)
print("\nDifference of A and B:\n", diff_matrix)

# Scalar Multiplication
scalar_product = 2 * A
print("\nScalar product (2 * A):\n", scalar_product)

# Matrix Multiplication
matrix_product = np.dot(A, B)  # or A @ B in Python 3.5+
print("\nMatrix product of A and B:\n", matrix_product)

# Element-wise Multiplication
element_wise_product = A * B
print("\nElement-wise product of A and B:\n", element_wise_product)

# 3. Matrix Properties and Methods
print("\n3. Matrix Properties and Methods")

# Shape and Size
shape = A.shape
size = A.size
print("Shape of A:", shape)
print("Size of A:", size)

# Transpose
transposed = A.T
print("\nTranspose of A:\n", transposed)

# Trace
trace = np.trace(A)
print("\nTrace of A:", trace)

# Determinant
determinant = np.linalg.det(A)
print("\nDeterminant of A:", determinant)

# 4. Matrix Decomposition
print("\n4. Matrix Decomposition")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

# Singular Value Decomposition (SVD)
U, s, V = np.linalg.svd(A)
print("\nSVD of A:")
print("U:\n", U)
print("s:", s)
print("V:\n", V)

# LU Decomposition
P, L, U = linalg.lu(A)
print("\nLU Decomposition of A:")
print("P:\n", P)
print("L:\n", L)
print("U:\n", U)

# 5. Solving Linear Equations
print("\n5. Solving Linear Equations")
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print("Solution to Ax = b:")
print("A:\n", A)
print("b:", b)
print("x:", x)

# 6. Advanced Operations
print("\n6. Advanced Operations")

# Matrix Power
matrix_power = np.linalg.matrix_power(A, 3)
print("A^3:\n", matrix_power)

# Matrix Exponential
exp_matrix = expm(A)
print("\nMatrix exponential of A:\n", exp_matrix)

# Kronecker Product
kron_product = np.kron(A, B)
print("\nKronecker product of A and B:\n", kron_product)

# 7. Broadcasting
print("\n7. Broadcasting")
A = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = A + b
print("A:\n", A)
print("b:", b)
print("A + b (broadcasting):\n", result)

# 8. Masking and Indexing
print("\n8. Masking and Indexing")
mask = A > 3
A_copy = A.copy()
A_copy[mask] = 0
print("Original A:\n", A)
print("A with elements > 3 set to 0:\n", A_copy)