import numpy as np

# Create a 2D array with values from 1 to 9
array_broadcast = np.arange(1, 10).reshape(3, 3)
print("2D Array for Broadcasting:\n", array_broadcast)

# Multiply the 2D array by a scalar value of 5
broadcast_result = array_broadcast * 5
print("Result of Broadcasting:\n", broadcast_result)

