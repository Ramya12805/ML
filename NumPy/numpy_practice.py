import numpy as np

a = np.array([1, 2, 3], dtype='int32')
print(a)

b = np.array([[9.0, 8.0, 7.0], [1.0, 2.0, 3.0]])
print(b)

# Get Dimension
print("Dimension of a:", a.ndim)

# Get Shape
print("Shape of b:", b.shape)

# Get Type
print("Type of a:", a.dtype)

# Get Size (number of bytes per element)
print("Item size of a:", a.itemsize)

# Get total size (total number of bytes)
print("Total size of a:", a.nbytes)

arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get specific element [r, c]
print("Element at arr[1, 5]:", arr[1, 5])
print("Element at arr[1, -2]:", arr[1, -2])

# Get specific row
print("First row:", arr[0, :])

# Get specific column
print("Third column:", arr[:, 2])

# [startindex:endindex:stepsize]
print("Elements from arr[0, 1:6:2]:", arr[0, 1:6:2])
print("Elements from arr[0, 1:-1:2]:", arr[0, 1:-1:2])

# Update value
arr[1, 5] = 20
print("Updated arr:", arr)

arr[:, 2] = [1, 2]
print("Updated arr with new column values:", arr)

arr_3d = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print("3D array:", arr_3d)

# Get specific element
print("Element at arr_3d[0, 1, :]:", arr_3d[0, 1, :])

# Replace elements
arr_3d[:, 1, :] = [[9, 9]]
print("Updated 3D array:", arr_3d)

# Initializing different types of arrays

# All 0's 2D matrix
print(np.zeros(5))
print("2D array of zeros:\n", np.zeros((2, 3)))

# All 1's matrix
print(np.ones(5))
print(np.ones((4, 2, 2)))

# Any other numbers
print(np.full((2, 2), 99))

# Any other number (full_like)
print(np.full_like(arr, 4))

# Matrix of random numbers
print(np.random.rand(4, 2))

# Random integer values
print(np.random.randint(7, size=(3, 3)))
print(np.random.randint(4, 7, size=(3, 3)))
print(np.random.randint(-4, 7, size=(3, 3)))

# Identity matrix
print(np.identity(5))

# Repeat an array
r1 = np.repeat(arr, 3, axis=0)
print(r1)

arr_5d = np.array([[[[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 9, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]]]])
print(arr_5d)

output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:4, 1:4] = z
print(output)

# We have to be careful when we are copying arrays
# We shouldn't do this when copying
array_1 = np.array([1, 2, 3])
barray = array_1
barray[0] = 100
print(array_1)

# Instead we should do this
array_1 = np.array([1, 2, 3])
barray = array_1.copy()
barray[0] = 100
print(array_1)

# Mathematics
array_2 = np.array([1, 2, 3, 4])
print(array_2 + 2)
print(array_2 - 2)
print(array_2 * 2)
print(array_2 / 2)

b_array = np.array([1, 0, 1, 0])
print(array_2 + b_array)

print(array_2 ** 2)

print(np.sin(array_2))
print(np.cos(array_2))

# Linear algebra

