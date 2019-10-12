from copy import deepcopy
import numpy as np
import ctypes

#sample code https://nesi.github.io/perf-training/python-scatter/ctypes

#(double* x_array, double* y_array, int vector_size, double* beta_solution, int b_size)

#np.ctypeslib.ndpointer(dtype=numpy.float64), np.ctypeslib.ndpointer(dtype=numpy.float64), ctypes.c_int, np.ctypeslib.ndpointer(dtype=numpy.float64), ctypes.c_int

# 1. open the shared library
mylib = ctypes.CDLL("./liblls_lib.so")

# 2. tell Python the argument and result types of function mysum
mylib.lls_solver.argtypes = [ np.ctypeslib.ndpointer(dtype=np.float64), np.ctypeslib.ndpointer(dtype=np.float64), ctypes.c_int, np.ctypeslib.ndpointer(dtype=np.float64), ctypes.c_int ]

x_array = np.arange(1, 5, 1, np.float64)
y_array = np.arange(0, 4, 1, np.float64)
b_array = np.arange(0, 2, 1, np.float64)

#6, 5, 7, 10
y_array[0]=6
y_array[1]=5
y_array[2]=7
y_array[3]=10

print(x_array)
print(y_array)
print(b_array)

# 3. call function mysum
mylib.lls_solver(x_array, y_array, 4, b_array, 2)

print(b_array)

#print('sum of array: {}'.format(array_sum))
