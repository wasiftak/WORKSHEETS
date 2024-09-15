import numpy as np

# Create a 4x4 array with values from 10 to 25
array_2d = np.arange(10, 26).reshape(4, 4)
print("2D Array:\n", array_2d)

# Extract second row
second_row = array_2d[1, :]
print("Second row:", second_row)

# Extract last column
last_column = array_2d[:, -1]
print("Last column:", last_column)

# Replace the first row with zeros
array_2d[0, :] = 0
print("Array after replacing first row with zeros:\n", array_2d)
