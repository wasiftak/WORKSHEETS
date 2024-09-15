import numpy as np

# Create a 1D array from 5 to 25
array_1d = np.arange(5, 26)
print("1D Array:", array_1d)

# Create a 2D array with random integers between 10 and 50
array_2d = np.random.randint(10, 51, size=(3, 4))
print("2D Array:\n", array_2d)


# Array attributes for the 1D array
print("Shape of 1D Array:", array_1d.shape)
print("Size of 1D Array:", array_1d.size)
print("Data Type of 1D Array:", array_1d.dtype)

# Array attributes for the 2D array
print("Shape of 2D Array:", array_2d.shape)
print("Size of 2D Array:", array_2d.size)
print("Data Type of 2D Array:", array_2d.dtype)
