import numpy as np

# Create a 1D array with 15 random integers between 10 and 60
random_array = np.random.randint(10, 61, size=15)
print("1D Random Array:", random_array)

# Compute mean
mean_value = np.mean(random_array)
print("Mean:", mean_value)

# Compute median
median_value = np.median(random_array)
print("Median:", median_value)

# Compute standard deviation
std_deviation = np.std(random_array)
print("Standard Deviation:", std_deviation)

