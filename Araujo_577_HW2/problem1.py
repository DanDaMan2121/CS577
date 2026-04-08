# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:09:27 2026

@author: Daniel
"""
import numpy as np
# a. Create a NumPy array np_array1 of integers from 0 to 25 and reshape it into a (5,5) matrix. 

a = np.arange(0, 25).reshape(5, 5)
print('Array A')
print(a)
print('=======')


# b. Create a NumPy array np_array2 of size 25 of equally spaced numbers from 5.0 to 10.0 (both
# endpoints inclusive) and print the array.
print('Array B')
b1 = np.linspace(5, 10, 25)
print(b1)
print('=======')


# This clearly shows too many digits after the decimal point. Write a function called
# matrix_round() that takes in a NumPy array and a desired precision, and returns another array of
# the same shape with all entries rounded to the desired precision.
# E.g. If the input is a (4, 2) matrix of the form
# The output of passing this matrix and a precision of 3 must return (you don’t have to print the
# precision)
# Remember, the only two inputs to the function should be the NumPy array and desired precision

def matrixRound(array, pVal):
    newArray = np.round(array, pVal)
    return newArray
print('Array B rounded')
b2 = matrixRound(b1, 3)
print(b2)
print('=======')



# c. Read the properties of matrix inversion in the class notes. Compute the inverse of the matrix V with
# the following entries (the linalg package might help here)
# Print 𝑉−1 to 3 decimal places. 
c1 = np.array([[1, 1, 1, 1, 1],
               [1, 2, 4, 8, 16],
               [1, 3, 9, 27, 81],
               [1, 4, 16, 64, 256],
               [1, 5, 25, 125, 625]])
print('Array C')
print(c1)
print('=======')

print('Array C inverse')
c2 = np.linalg.inv(c1)
print(matrixRound(c2, 3))
print('=======')

# Compute 𝑉−1𝑉 and 𝑉 𝑉−1 and print them to 3 decimal places. 
c3 = c1 @ c2
print('Array C MatrixProduct Array C inverse')
print(matrixRound(c3, 3))
print('=======')
c4 = c2 @ c1
print('Array C inverse MatrixProduct Array C')
print(matrixRound(c4, 3))
print('=======')


print('What is the name given to the matrices 𝑉−1𝑉 and 𝑉 𝑉−1?')
print('ans: Identity Matrix')
print('=======')

print('What NumPy command is used to generate such matrices?')
print('ans: np.eye(<yourValue>) or np.identity(<yourValue>)')




