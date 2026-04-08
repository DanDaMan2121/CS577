# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:31:31 2026

@author: dbara
"""
from sympy import isprime

# a. Write a function that uses map() to convert a list of binary strings into their corresponding decimal
# values. Each binary string represents a non-negative integer.
# Example input: binaries = ['1010', '1111', '0001', '100000']
# Output: [10, 15, 1, 32]

def binaryToDecimalList(binaries):
    return list(map(lambda x: int(x, 2), binaries)) # determine decimal value of binary value from binaries then return the values as a list

binaries = ['1010', '1111', '0001', '100000']
result = binaryToDecimalList(binaries)

print(f'a: {result}')

# b. Use filter() to create a list of strings from the given list that are palindromes. A palindrome is a
# string that reads the same forward and backward.
# Example input: words = ['level', 'world', 'deified', 'python', 'radar']
# Output: ['level', 'deified', 'radar']

def getPalindromes(words):
    return list(filter(lambda w: w == w[::-1], words)) # if word is not equal to the reverse of the word then filter

words = ['level', 'world', 'deified', 'python', 'radar']
result = getPalindromes(words)

print(f'b: {result}')

# c. Write a single line of Python code using map() and filter() to find the squares of even numbers
# from the given list of integers.
# Input: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))) # filter numbers on the condition of being even then square the value and add it to a new list

print(f'c: {result}')

# d. Given a list of integers, use filter() to create a new list that contains only those integers that are
# prime numbers.

result = list(filter(lambda n: n > 1 and isprime(n), numbers)) # filter numbers that are greater than 0 and are prime
print(f'd: {result}')