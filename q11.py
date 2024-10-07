import numpy as np
import array

array_5x5=np.zeros((5,5))
print("5x5 array of zeros:\n",array_5x5)

matrix_3x3=np.arange(9).reshape(3,3)
print("3 byb 3 matrix with values from 0 to 8;\n", matrix_3x3)

array = np.array([1, 0, 2, 0, 3, 5, 6, 8])
non_zero_indices=np.nonzero(array)
print("Indices of non zero elements",non_zero_indices[0])

random_array=np.random.rand(10,10)
random_array2=np.random.rand(10,10)
min_value=np.min(random_array)
max_value=np.max(random_array)
print("10x10 first random array\n:",random_array)
print("10x10 second random array\n:",random_array2)

print("Minimum value",min_value)
print("Max value",max_value)

# Create a random vector of size 30
random_vector = np.random.rand(30)

# Find the mean value
mean_value = np.mean(random_vector)

print("Random vector of size 30:\n", random_vector)
print("Mean value:", mean_value)




