# Introduction to NumPy

NumPy is a fundamental library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions. NumPy is widely used for scientific computing, data analysis, and machine learning. Its core feature is the `ndarray`, a powerful n-dimensional array object.

## Key Features of NumPy

- **ndarray**: A fast, flexible container for large datasets in Python.
- **Mathematical Functions**: A comprehensive collection of mathematical functions for element-wise operations.
- **Broadcasting**: A powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
- **Linear Algebra**: Built-in support for linear algebra operations, Fourier transforms, and random number generation.
- **Integration with Other Libraries**: Often used with other libraries like SciPy, pandas, and matplotlib for advanced data analysis and visualization.

## Installing NumPy

You can install NumPy using pip:

```bash
pip install numpy
```

## Creating Arrays

NumPy arrays can be created from Python lists or tuples using the `numpy.array` function. Here are some examples:

```python
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)
```

## Array Attributes

NumPy arrays have several important attributes:

- **shape**: The dimensions of the array.
- **size**: The total number of elements in the array.
- **dtype**: The data type of the elements.

```python
# Attributes of the array
print("Shape of 1D Array:", array_1d.shape)
print("Size of 1D Array:", array_1d.size)
print("Data type of 1D Array:", array_1d.dtype)
```

## Array Operations

NumPy supports a wide variety of operations, including element-wise arithmetic, mathematical functions, and more.

```python
# Element-wise arithmetic operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

sum_array = array_a + array_b
print("Sum of arrays:", sum_array)

diff_array = array_a - array_b
print("Difference of arrays:", diff_array)

prod_array = array_a * array_b
print("Element-wise product of arrays:", prod_array)

# Mathematical functions
sqrt_array = np.sqrt(array_a)
print("Square root of array:", sqrt_array)

exp_array = np.exp(array_a)
print("Exponential of array:", exp_array)
```

## Broadcasting

Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes.

```python
# Broadcasting example
array_c = np.array([1, 2, 3])
array_d = np.array([[1], [2], [3]])

broadcasted_sum = array_c + array_d
print("Broadcasted sum:\n", broadcasted_sum)
```

## Linear Algebra

NumPy has built-in support for linear algebra operations.

```python
# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix product:\n", matrix_product)

# Determinant
matrix_det = np.linalg.det(matrix_a)
print("Determinant of matrix:", matrix_det)
```

## Random Number Generation

NumPy has a powerful random number generation module.

```python
# Random number generation
random_array = np.random.rand(3, 3)  # 3x3 matrix with random numbers
print("Random array:\n", random_array)

random_int_array = np.random.randint(0, 10, (3, 3))  # 3x3 matrix with random integers between 0 and 10
print("Random integer array:\n", random_int_array)
```

# Manipulating NumPy Arrays

Manipulating arrays is a crucial part of working with NumPy. Below are various techniques and functions to effectively manipulate arrays.

## Array Reshaping

Reshaping arrays allows you to change the shape of an existing array without changing its data.

```python
import numpy as np

# Reshape 1D array to 2D array
array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = array_1d.reshape((2, 3))
print("Reshaped 1D to 2D array:\n", array_2d)

# Reshape 2D array to 3D array
array_3d = array_2d.reshape((2, 1, 3))
print("Reshaped 2D to 3D array:\n", array_3d)
```

## Array Flattening

Flattening an array means converting a multi-dimensional array into a 1D array.

```python
# Flattening a 2D array
flattened_array = array_2d.flatten()
print("Flattened array:", flattened_array)
```

## Array Transposition

Transposing an array means swapping its axes.

```python
# Transpose a 2D array
transposed_array = array_2d.T
print("Transposed array:\n", transposed_array)
```

## Array Stacking

Stacking arrays is useful for combining multiple arrays into a single array. NumPy provides several stacking functions:

- **vstack**: Stack arrays vertically (row-wise).
- **hstack**: Stack arrays horizontally (column-wise).
- **dstack**: Stack arrays depth-wise (along the third dimension).

```python
# Vertical stacking
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
vstacked_array = np.vstack((array_a, array_b))
print("Vertically stacked array:\n", vstacked_array)

# Horizontal stacking
hstacked_array = np.hstack((array_a, array_b))
print("Horizontally stacked array:", hstacked_array)

# Depth stacking
array_c = np.array([[1], [2], [3]])
array_d = np.array([[4], [5], [6]])
dstacked_array = np.dstack((array_c, array_d))
print("Depth stacked array:\n", dstacked_array)
```

## Array Splitting

Splitting arrays allows you to divide an array into multiple sub-arrays.

```python
# Horizontal splitting
hsplit_array = np.hsplit(vstacked_array, 3)
print("Horizontally split arrays:", hsplit_array)

# Vertical splitting
vsplit_array = np.vsplit(vstacked_array, 2)
print("Vertically split arrays:", vsplit_array)
```

## Array Indexing and Slicing

Indexing and slicing are used to access or modify elements of an array.

```python
# Indexing
element = array_2d[0, 1]
print("Element at index [0, 1]:", element)

# Slicing
sub_array = array_2d[:, 1:3]
print("Sliced array:\n", sub_array)
```

## Boolean Indexing

Boolean indexing is used to select elements from an array that satisfy certain conditions.

```python
# Boolean indexing
bool_index = array_1d > 3
print("Boolean index array:", bool_index)

filtered_array = array_1d[bool_index]
print("Filtered array:", filtered_array)
```

## Array Concatenation

Concatenating arrays combines multiple arrays along an existing axis.

```python
# Concatenation along axis 0
concat_array = np.concatenate((array_a, array_b))
print("Concatenated array:", concat_array)
```

## Inserting and Deleting Elements

NumPy provides functions to insert and delete elements from an array.

```python
# Inserting elements
inserted_array = np.insert(array_1d, 2, [10, 11])
print("Array after insertion:", inserted_array)

# Deleting elements
deleted_array = np.delete(array_1d, [1, 3])
print("Array after deletion:", deleted_array)
```

# NumPy Matrix Operations Examples

## Overview

This Python script demonstrates a comprehensive set of matrix operations using NumPy and SciPy. It serves as a practical guide and reference for working with matrices in scientific computing with Python.

## Contents

The script covers the following topics:

1. Creating Matrices
2. Basic Matrix Operations
3. Matrix Properties and Methods
4. Matrix Decomposition
5. Solving Linear Equations
6. Advanced Operations
7. Broadcasting
8. Masking and Indexing

Each section includes multiple examples showcasing different functions and methods.

## Requirements

- Python 3.x
- NumPy
- SciPy

## Installation

To run this script, you need to have Python installed on your system. Additionally, you'll need to install NumPy and SciPy. You can install these packages using pip:

```
pip install numpy scipy
```

## Usage

1. Save the script as `numpy_matrix_examples.py` (or any preferred name).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command:

   ```
   python numpy_matrix_examples.py
   ```

5. The script will execute all examples and print the results to the console.

## Sections Explained

1. **Creating Matrices**: Demonstrates various methods to create matrices, including manual definition, zeros, ones, identity, range, and random matrices.

2. **Basic Matrix Operations**: Covers addition, subtraction, scalar multiplication, matrix multiplication, and element-wise multiplication.

3. **Matrix Properties and Methods**: Shows how to find shape, size, transpose, trace, and determinant of a matrix.

4. **Matrix Decomposition**: Includes examples of eigenvalue decomposition, singular value decomposition (SVD), and LU decomposition.

5. **Solving Linear Equations**: Demonstrates how to solve a system of linear equations.

6. **Advanced Operations**: Covers matrix power, matrix exponential, and Kronecker product.

7. **Broadcasting**: Shows how NumPy's broadcasting feature works with matrices of different shapes.

8. **Masking and Indexing**: Demonstrates boolean masking to modify specific elements in a matrix.

## Customization

Feel free to modify the matrices or add more operations to experiment further. The script is designed to be educational and easily extendable.

## Further Reading

For more detailed information on NumPy and SciPy functions, refer to the official documentation:

- NumPy Documentation: https://numpy.org/doc/
- SciPy Documentation: https://docs.scipy.org/doc/scipy/

# Arithmetic Operations in NumPy

Arithmetic operations are fundamental to numerical computing, and NumPy provides a wide range of functions to perform element-wise arithmetic operations on arrays. This README covers basic arithmetic operations, broadcasting, and advanced mathematical functions.

## Table of Contents

1. [Basic Arithmetic Operations](#basic-arithmetic-operations)
2. [Scalar Operations](#scalar-operations)
3. [Broadcasting](#broadcasting)
4. [Universal Functions (ufuncs)](#universal-functions-ufuncs)
5. [Aggregation Functions](#aggregation-functions)
6. [Axis-Based Operations](#axis-based-operations)

## Basic Arithmetic Operations

NumPy supports element-wise addition, subtraction, multiplication, and division.

```python
import numpy as np

# Create two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

# Element-wise addition
add_result = array1 + array2
print("Addition:\n", add_result)

# Element-wise subtraction
sub_result = array1 - array2
print("Subtraction:\n", sub_result)

# Element-wise multiplication
mul_result = array1 * array2
print("Multiplication:\n", mul_result)

# Element-wise division
div_result = array1 / array2
print("Division:\n", div_result)
```

## Scalar Operations

NumPy allows arithmetic operations between arrays and scalars. The scalar operation is applied to each element of the array.

```python
# Scalar addition
scalar_add = array1 + 5
print("Scalar Addition:\n", scalar_add)

# Scalar multiplication
scalar_mul = array1 * 2
print("Scalar Multiplication:\n", scalar_mul)
```

## Broadcasting

Broadcasting allows NumPy to perform arithmetic operations on arrays of different shapes. The smaller array is "broadcast" over the larger array so that they have compatible shapes.

```python
# Broadcasting example
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array4 = np.array([1, 2, 3])

broadcast_add = array3 + array4
print("Broadcast Addition:\n", broadcast_add)
```

## Universal Functions (ufuncs)

NumPy provides universal functions (ufuncs) that are optimized for fast element-wise operations.

```python
# Create an array
array5 = np.array([1, 4, 9, 16, 25])

# Square root
sqrt_result = np.sqrt(array5)
print("Square Root:\n", sqrt_result)

# Exponential
exp_result = np.exp(array5)
print("Exponential:\n", exp_result)

# Logarithm
log_result = np.log(array5)
print("Logarithm:\n", log_result)
```

## Aggregation Functions

NumPy provides several functions to perform aggregation operations like sum, mean, max, and min.

```python
# Create an array
array6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum
sum_result = np.sum(array6)
print("Sum:\n", sum_result)

# Mean
mean_result = np.mean(array6)
print("Mean:\n", mean_result)

# Maximum
max_result = np.max(array6)
print("Maximum:\n", max_result)

# Minimum
min_result = np.min(array6)
print("Minimum:\n", min_result)
```

## Axis-Based Operations

Many NumPy functions allow specifying an axis along which to perform the operation.

```python
# Sum along rows (axis=1)
sum_rows = np.sum(array6, axis=1)
print("Sum along rows:\n", sum_rows)

# Sum along columns (axis=0)
sum_columns = np.sum(array6, axis=0)
print("Sum along columns:\n", sum_columns)
```

# Linear Algebra in NumPy

Linear algebra is a branch of mathematics that deals with vectors, matrices, and operations on them. NumPy provides a wide range of functions to perform linear algebra operations efficiently.

## Table of Contents

1. [Creating Matrices and Vectors](#creating-matrices-and-vectors)
2. [Matrix Addition and Subtraction](#matrix-addition-and-subtraction)
3. [Matrix Multiplication](#matrix-multiplication)
4. [Transpose of a Matrix](#transpose-of-a-matrix)
5. [Determinant of a Matrix](#determinant-of-a-matrix)
6. [Inverse of a Matrix](#inverse-of-a-matrix)
7. [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
8. [Solving Linear Systems](#solving-linear-systems)
9. [Singular Value Decomposition (SVD)](#singular-value-decomposition-svd)

## Creating Matrices and Vectors

You can create matrices and vectors using `numpy.array`.

```python
import numpy as np

# Create a vector
vector = np.array([1, 2, 3])
print("Vector:\n", vector)

# Create a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)
```

## Matrix Addition and Subtraction

Matrix addition and subtraction are performed element-wise.

```python
# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix addition
add_result = matrix1 + matrix2
print("Matrix Addition:\n", add_result)

# Matrix subtraction
sub_result = matrix1 - matrix2
print("Matrix Subtraction:\n", sub_result)
```

## Matrix Multiplication

Matrix multiplication (dot product) is different from element-wise multiplication. Use the `np.dot` function or the `@` operator for matrix multiplication.

```python
# Matrix multiplication
mul_result = np.dot(matrix1, matrix2)
print("Matrix Multiplication (dot product):\n", mul_result)

# Using the @ operator
mul_result_operator = matrix1 @ matrix2
print("Matrix Multiplication (@ operator):\n", mul_result_operator)
```

## Transpose of a Matrix

The transpose of a matrix is obtained by swapping its rows with its columns.

```python
# Transpose of a matrix
transpose_result = matrix.T
print("Transpose of Matrix:\n", transpose_result)
```

## Determinant of a Matrix

The determinant of a square matrix is a special number that can be calculated from its elements. Use `np.linalg.det` to find the determinant.

```python
# Determinant of a matrix
det_result = np.linalg.det(matrix1)
print("Determinant of Matrix1:", det_result)
```

## Inverse of a Matrix

The inverse of a matrix is a matrix that, when multiplied with the original matrix, yields the identity matrix. Use `np.linalg.inv` to find the inverse.

```python
# Inverse of a matrix
inverse_result = np.linalg.inv(matrix1)
print("Inverse of Matrix1:\n", inverse_result)
```

## Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors are properties of a matrix that are used in many applications like principal component analysis (PCA). Use `np.linalg.eig` to compute them.

```python
# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix1)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

## Solving Linear Systems

To solve a system of linear equations \( A \mathbf{x} = \mathbf{b} \), use `np.linalg.solve`.

```python
# Solve a system of linear equations
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = np.linalg.solve(A, b)
print("Solution of linear system:\n", x)
```

## Singular Value Decomposition (SVD)

SVD is a factorization of a matrix into three matrices and is used in many applications, including data compression and noise reduction. Use `np.linalg.svd` to perform SVD.

```python
# Singular Value Decomposition (SVD)
U, sigma, Vt = np.linalg.svd(matrix1)
print("U Matrix:\n", U)
print("Sigma Values:\n", sigma)
print("Vt Matrix:\n", Vt)
```
# Random Data, Sorting, and Searching in NumPy

NumPy provides various functions for generating random data, as well as sorting and searching arrays. These operations are essential for data analysis, simulations, and many other applications.

## Table of Contents

1. [Generating Random Data](#generating-random-data)
    - [Random Numbers](#random-numbers)
    - [Random Arrays](#random-arrays)
    - [Random Samples from Distributions](#random-samples-from-distributions)
2. [Sorting Arrays](#sorting-arrays)
3. [Searching Arrays](#searching-arrays)
    - [Finding Indices](#finding-indices)
    - [Searching Sorted Arrays](#searching-sorted-arrays)
    - [Finding Unique Elements](#finding-unique-elements)

## Generating Random Data

NumPy has a random module that allows you to generate random numbers and arrays with various distributions.

### Random Numbers

```python
import numpy as np

# Random float between 0 and 1
random_float = np.random.rand()
print("Random Float:", random_float)

# Random integer between a range
random_int = np.random.randint(1, 10)
print("Random Integer:", random_int)
```

### Random Arrays

```python
# Random array of specified shape with values between 0 and 1
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)

# Random integer array
random_int_array = np.random.randint(1, 10, size=(3, 3))
print("Random Integer Array:\n", random_int_array)
```

### Random Samples from Distributions

```python
# Normal distribution (mean=0, std=1)
normal_array = np.random.randn(3, 3)
print("Normal Distribution Array:\n", normal_array)

# Uniform distribution
uniform_array = np.random.uniform(1, 5, size=(3, 3))
print("Uniform Distribution Array:\n", uniform_array)
```

## Sorting Arrays

NumPy provides functions to sort arrays along specified axes.

```python
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
```

## Searching Arrays

NumPy provides functions to search for specific elements within arrays.

### Finding Indices

```python
# Create an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Find indices where a condition is met
indices = np.where(array > 5)
print("Indices where array > 5:", indices)
```

### Searching Sorted Arrays

```python
# Create a sorted array
sorted_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Binary search
index = np.searchsorted(sorted_array, 5)
print("Index of 5 in sorted array:", index)
```

### Finding Unique Elements

```python
# Create an array with duplicate elements
array_with_duplicates = np.array([1, 2, 2, 3, 4, 4, 5])

# Find unique elements
unique_elements = np.unique(array_with_duplicates)
print("Unique Elements:", unique_elements)
```

This README provides a comprehensive introduction to NumPy, its key features, installation instructions, and examples of creating arrays, array attributes, operations, broadcasting, linear algebra, and random number generation.