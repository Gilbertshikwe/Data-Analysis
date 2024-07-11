import numpy as np

# Creating Arrays
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)

# Array Attributes
print("Shape of 1D Array:", array_1d.shape)
print("Size of 1D Array:", array_1d.size)
print("Data type of 1D Array:", array_1d.dtype)

# Array Operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

sum_array = array_a + array_b
print("Sum of arrays:", sum_array)

diff_array = array_a - array_b
print("Difference of arrays:", diff_array)

prod_array = array_a * array_b
print("Element-wise product of arrays:", prod_array)

sqrt_array = np.sqrt(array_a)
print("Square root of array:", sqrt_array)

exp_array = np.exp(array_a)
print("Exponential of array:", exp_array)

# Broadcasting
array_c = np.array([1, 2, 3])
array_d = np.array([[1], [2], [3]])

broadcasted_sum = array_c + array_d
print("Broadcasted sum:\n", broadcasted_sum)

# Linear Algebra
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix product:\n", matrix_product)

matrix_det = np.linalg.det(matrix_a)
print("Determinant of matrix:", matrix_det)

# Random Number Generation
random_array = np.random.rand(3, 3)
print("Random array:\n", random_array)

random_int_array = np.random.randint(0, 10, (3, 3))
print("Random integer array:\n", random_int_array)
