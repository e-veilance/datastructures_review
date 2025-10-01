import numpy as np

# sort 1D array
onedim_arr = np.arange(9)
print("1D array", onedim_arr)
np.random.shuffle(onedim_arr) # inplace shuffle
print("shuffled 1D array", onedim_arr)

# sort 2d array
twodim_arr = np.arange(9).reshape(3,3)
print("2D array", twodim_arr)
np.random.shuffle(twodim_arr.reshape(9)) # inplace shuffle on flattened array
print("shuffled 2D array", twodim_arr)