# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# a. Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], write a list comprehension that
# generates the squares of all elements of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]

print(f'a: {squares}')


# b. What is title casing? Given a list fruits = ['green apple', 'banana', 'cherry',
# 'date'], write a list comprehension that title cases each element of the list fruits. Your output
# should look like: ['Green Apple', 'Banana', 'Cherry', 'Date'].


fruits = ['green apple', 'banana', 'cherry', 'date']
titleCasing = [fruit.title() for fruit in fruits]

print(f'b: {titleCasing}')

# c. Using dictionary comprehension, create a dictionary, nested_dictionary, where the keys are
# numbers from 1 to 3, and the values are dictionaries where the keys are the first three letters of the
# alphabet, and the values are the product of the outer and inner keys. Assume ‘a’ corresponds to 1,
# ‘b’ corresponds to 2, …, and ‘z’ corresponds to 26.
# Your output should look like:
# {1: {'a': 1, 'b': 2, 'c': 3}, 2: {'a': 2, 'b': 4, 'c': 6}, 3: {'a': 3,
# 'b': 6, 'c': 9}}
# Hint: The built-in function ord() returns the Unicode number for one-character strings.

nestedDictionary = {
    i: {chr(j): i * (j - ord('a') + 1) for j in range(ord('a'), ord('a') + 3)}
    for i in range(1, 4)
}

print(f'c: {nestedDictionary}')