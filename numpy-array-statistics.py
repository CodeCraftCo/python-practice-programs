#A Python program that calculates the minimum, maximum, and average values of a NumPy array.
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
minval = np.min(arr)
maxval = np.max(arr)
avgval = np.mean(arr)
print("Minimum Value:", minval)
print("Average Value:", avgval)
print("Maximum Value:", maxval)