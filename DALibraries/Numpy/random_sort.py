import numpy as np

# Generating Random Data

# Random float between 0 and 1
random_float = np.random.rand()
print("Random Float:", random_float)

# Random integer between a range
random_int = np.random.randint(1, 10)
print("Random Integer:", random_int)

# Random array of specified shape with values between 0 and 1
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)

# Random integer array
random_int_array = np.random.randint(1, 10, size=(3, 3))
print("Random Integer Array:\n", random_int_array)

# Normal distribution (mean=0, std=1)
normal_array = np.random.randn(3, 3)
print("Normal Distribution Array:\n", normal_array)

# Uniform distribution
uniform_array = np.random.uniform(1, 5, size=(3, 3))
print("Uniform Distribution Array:\n", uniform_array)

# Sorting Arrays

# Create an unsorted array
unsorted_array = np.array([3, 1, 2, 5, 4])
print("Unsorted Array:", unsorted_array)

# Sort the array
sorted_array = np.sort(unsorted_array)
print("Sorted Array:", sorted_array)

# Sort along rows or columns in a 2D array
array_2d = np.array([[3, 2, 1], [6, 5, 4]])
sorted_array_row = np.sort(array_2d, axis=1)
sorted_array_col = np.sort(array_2d, axis=0)
print("Sorted 2D Array along rows:\n", sorted_array_row)
print("Sorted 2D Array along columns:\n", sorted_array_col)

# Searching Arrays

# Create an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Find indices where a condition is met
indices = np.where(array > 5)
print("Indices where array > 5:", indices)

# Create a sorted array
sorted_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Binary search
index = np.searchsorted(sorted_array, 5)
print("Index of 5 in sorted array:", index)

# Create an array with duplicate elements
array_with_duplicates = np.array([1, 2, 2, 3, 4, 4, 5])

# Find unique elements
unique_elements = np.unique(array_with_duplicates)
print("Unique Elements:", unique_elements)
