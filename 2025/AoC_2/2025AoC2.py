import os
import numpy as np
import re

year = 2025
day = 2
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/{year}AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/{year}AoC{day}_input.txt')

data = open(filepath, 'r').read().split(',')

def part1(puzzle_input):
    inval = 0
    ranges = [list(map(int, z.split('-'))) for z in puzzle_input]
    for i in range(0, int(np.sqrt(max([r[1] for r in ranges])))):
        ID = int(str(i)*2)
        for x in ranges:
            if x[0] <= ID <= x[1]:
                inval += ID
    return inval

def part2(puzzle_input):
    inval = 0
    ranges = [list(map(int, z.split('-'))) for z in puzzle_input]

    tested = []
    for i in range(0, int(np.sqrt(max([r[1] for r in ranges])))):
        for j in range(2, 7+1):
            ID = int(str(i)*j)
            for x in ranges:
                if x[0] <= ID <= x[1] and ID not in tested:
                    tested.append(ID)
                    inval += ID
    return inval
                

print("Part 1:", part1(data))
print("Part 2:", part2(data))
