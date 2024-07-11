import numpy as np

# Basic Arithmetic Operations
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

add_result = array1 + array2
print("Addition:\n", add_result)

sub_result = array1 - array2
print("Subtraction:\n", sub_result)

mul_result = array1 * array2
print("Multiplication:\n", mul_result)

div_result = array1 / array2
print("Division:\n", div_result)

# Scalar Operations
scalar_add = array1 + 5
print("Scalar Addition:\n", scalar_add)

scalar_mul = array1 * 2
print("Scalar Multiplication:\n", scalar_mul)

# Broadcasting
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array4 = np.array([1, 2, 3])

broadcast_add = array3 + array4
print("Broadcast Addition:\n", broadcast_add)

# Universal Functions (ufuncs)
array5 = np.array([1, 4, 9, 16, 25])

sqrt_result = np.sqrt(array5)
print("Square Root:\n", sqrt_result)

exp_result = np.exp(array5)
print("Exponential:\n", exp_result)

log_result = np.log(array5)
print("Logarithm:\n", log_result)

# Aggregation Functions
array6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

sum_result = np.sum(array6)
print("Sum:\n", sum_result)

mean_result = np.mean(array6)
print("Mean:\n", mean_result)

max_result = np.max(array6)
print("Maximum:\n", max_result)

min_result = np.min(array6)
print("Minimum:\n", min_result)

# Axis-Based Operations
sum_rows = np.sum(array6, axis=1)
print("Sum along rows:\n", sum_rows)

sum_columns = np.sum(array6, axis=0)
print("Sum along columns:\n", sum_columns)
