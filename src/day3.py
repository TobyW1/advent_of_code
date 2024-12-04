import numpy as np
import re

# Part 1: Multiply the correct sections
# Read the file into a list
with open('../data/input_day3.txt', 'r') as file:
    corrupted_memory = file.readlines()

# One line
corrupted_memory = ''.join(corrupted_memory)

# Pluck out the correct strings
to_multiply = re.findall('mul\(\d{,3},\d{,3}\)', corrupted_memory)

# define multiplication
def mul(a,b):
    return a*b

def do():
    return 0

# evaluate each line and sum
print(sum([eval(line) for line in to_multiply]))


# Part 2: new functions

# Pluck out the correct strings
to_process = re.findall(r"(?:mul|do|don\'t)\(\d{,3},?\d{,3}\)", corrupted_memory)

do_status = True
new_list = []
for line in to_process:
    if line == "do()":
        do_status = True
        new_list.append(0)
    if line == "don't()":
        do_status = False
        new_list.append(0)

    else:
        if do_status:
            new_list.append(eval(line))
        else:
            new_list.append(0)

print(sum(new_list))

