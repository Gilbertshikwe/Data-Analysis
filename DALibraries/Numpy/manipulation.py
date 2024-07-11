import numpy as np

# Reshaping
array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = array_1d.reshape((2, 3))
print("Reshaped 1D to 2D array:\n", array_2d)

array_3d = array_2d.reshape((2, 1, 3))
print("Reshaped 2D to 3D array:\n", array_3d)

# Flattening
flattened_array = array_2d.flatten()
print("Flattened array:", flattened_array)

# Transposing
transposed_array = array_2d.T
print("Transposed array:\n", transposed_array)

# Stacking
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
vstacked_array = np.vstack((array_a, array_b))
print("Vertically stacked array:\n", vstacked_array)

hstacked_array = np.hstack((array_a, array_b))
print("Horizontally stacked array:", hstacked_array)

array_c = np.array([[1], [2], [3]])
array_d = np.array([[4], [5], [6]])
dstacked_array = np.dstack((array_c, array_d))
print("Depth stacked array:\n", dstacked_array)

# Splitting
hsplit_array = np.hsplit(vstacked_array, 3)
print("Horizontally split arrays:", hsplit_array)

vsplit_array = np.vsplit(vstacked_array, 2)
print("Vertically split arrays:", vsplit_array)

# Indexing and Slicing
element = array_2d[0, 1]
print("Element at index [0, 1]:", element)

sub_array = array_2d[:, 1:3]
print("Sliced array:\n", sub_array)

# Boolean Indexing
bool_index = array_1d > 3
print("Boolean index array:", bool_index)

filtered_array = array_1d[bool_index]
print("Filtered array:", filtered_array)

# Concatenation
concat_array = np.concatenate((array_a, array_b))
print("Concatenated array:", concat_array)

# Inserting and Deleting
inserted_array = np.insert(array_1d, 2, [10, 11])
print("Array after insertion:", inserted_array)

deleted_array = np.delete(array_1d, [1, 3])
print("Array after deletion:", deleted_array)
