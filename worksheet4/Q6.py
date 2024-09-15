import numpy as np

# Create a 1D array with 10 random integers between 20 and 40
array_1d = np.random.randint(20, 41, size=10)
print("1D Array:", array_1d)

# Find elements greater than 30
greater_than_30 = array_1d[array_1d > 30]
print("Elements greater than 30:", greater_than_30)


# Create a 1D array with 12 elements starting from 11
array_1d_reshaped = np.arange(11, 23)
print("1D Array:", array_1d_reshaped)

# Reshape the 1D array into a 3x4 2D array
reshaped_array = array_1d_reshaped.reshape(3, 4)
print("Reshaped 2D Array:\n", reshaped_array)
