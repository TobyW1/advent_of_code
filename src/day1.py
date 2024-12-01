import numpy as np


# Part 1: Sum of absolute difference of ordered pairs
# Read the file into a list
with open('../data/input_day1.txt', 'r') as file:
    lines = file.readlines()

# Strip newline characters from each line
lines = [line.strip() for line in lines]
lines = [[line.split()[0], line.split()[1]] for line in lines]
list1, list2 = np.array([line[0] for line in lines]), np.array([line[1] for line in lines])

list1.sort()
list2.sort()

print(sum(abs(list2.astype(int) - list1.astype(int))))

# Part 2: Similarity score
score_array = []
for element in list1:
    appearances = np.count_nonzero(list2==element)
    print(appearances)
    score_array.append(int(element) * appearances)

print(sum(score_array))