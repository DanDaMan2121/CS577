# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:39:20 2026

@author: dbara
"""
import math

# a. Define a class called Vector with two attributes, dimension and coordinates. The former, dimension,
# stores the dimension of the space in which this vector object is defined, and the latter stores the vector
# object’s coordinates. Both of these need to be specified during initialization and have default values
# of 2 and [0.0, 0.0] respectively.


class Vector:
    def __init__(self, dimension=2, coordinates=None):
        self.dimension = dimension
        if coordinates is None:
            self.coordinates = [0.0] * dimension
        else:
            self.coordinates = coordinates

# b. Next, define two methods distance() and vector_sum(). The distance() method takes
# another Vector object, say, y and returns the Euclidean distance between the current Vector and y.
# The vector_sum() method also takes a Vector object, say y again, and returns another Vector
# object whose coordinates are given by the vector sum of the two vectors.

    def distance(self, otherVector):
        # Euclidean distance between self and otherVector
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(self.coordinates, otherVector.coordinates)))

    def vectorSum(self, otherVector):
        # Returns a new Vector whose coordinates are the sum of self and otherVector
        newCoordinates = [a + b for a, b in zip(self.coordinates, otherVector.coordinates)]
        return Vector(dimension=self.dimension, coordinates=newCoordinates)
    
    def vectorLength(self):
        # Returns the vector
        return math.sqrt(sum(a ** 2 for a in self.coordinates))


# c. Finally, what does the “__str__()” method do? Define a “__str__()” method that prints the
# coordinates of the Vector object.

# The __str__() method defines how the object is printed when you called print() on an object of class vector

    def __str__(self):
        return f"Vector coordinates: {self.coordinates}"

# d. Using only the above answer the following questions. Suppose 𝒙𝒙 = [1.0, −1.0, 3.0, 5.0, −2.2]
# and 𝒚𝒚 is the origin, how far is 𝒙𝒙 from 𝒚𝒚? If 𝒛𝒛 = 𝒙𝒙 + 𝒚𝒚, what is the length of the vector z? Without
# explicitly accessing any attributes of 𝒛𝒛, print its coordinates

# Define vectors
x = Vector(dimension=5, coordinates=[1.0, -1.0, 3.0, 5.0, -2.2])
y = Vector(dimension=5)  # Origin [0.0, 0.0, 0.0, 0.0, 0.0]

# Distance from x to origin
distance = x.distance(y)
print(f'Distance from x to y (origin): {distance}')

# Vector sum z = x + y
z = x.vectorSum(y)

print(f'Length of z: {z.vectorLength()}')
print(z)

