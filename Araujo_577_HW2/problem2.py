from tqdm import tqdm
import time
import numpy as np

# a. Write a program to multiply two 700 × 700 matrices using nested for loops. Using the tqdm()
# function from the tqdm package, display a progress bar showing the progress of your program (short
# tutorial on using the tqdm package).
# b. Import the time module and use the time() method within to measure the time taken to multiply
# the two matrices (documentation on the time module).

# calculates the matrix product using for loops by multiplying the current row by the current column
def testSpeedOfLoops(m1, m2):
    m3 = np.zeros((700, 700))
    numberOfIterations = m1.shape[0]
    start = time.time()
    for i in range(numberOfIterations):
        row = m1[i] # current row
        for j in range(m1.shape[1]):
            col = m2[:, j] # current column
            arrayProduct = row * col # elementwise array product
            indexValue = np.sum(arrayProduct) # total sum of the array generated
            m3[i][j] = indexValue # value of the current index
    end = time.time()
    return end - start
    

# c. Report the average time taken to multiply two 700 × 700 matrices using nested for loops (compute
# the average over 30 randomly generated pairs of matrices)
rng = np.random.default_rng() # random number generator

timeOfTest = 0
# performs 30 tests
for k in tqdm(range(30)):
    # generates 2 random matricies of 700x700 dimensions
    matrix1 = rng.integers(0, 700, size=(700, 700))
    matrix2 = rng.integers(0, 700, size=(700, 700))

    totalTime = testSpeedOfLoops(matrix1, matrix2)
    # print(f"Total time: {totalTime} seconds")
    timeOfTest += totalTime
print(f"Average test time: {timeOfTest / 30} seconds")

# d. Repeat the above procedure, but use the NumPy method numpy.dot()instead of the two for loops.
timeOfTest = 0
def testSpeedofDotProduct(m1, m2):
    start = time.time()
    m3 = m1 @ m2
    end = time.time()
    return end - start

for l in tqdm(range(30)):
    matrix1 = rng.integers(0, 700, size=(700, 700))
    matrix2 = rng.integers(0, 700, size=(700, 700))

    totalTime = testSpeedofDotProduct(matrix1, matrix2)
    timeOfTest += totalTime

print(f"Average test time: {timeOfTest / 30} seconds")

# e. What speedup do you observe with NumPy?
# NumPy is much faster
