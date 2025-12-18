import os
import numpy as np
import re

year = 2025
day = 3
# filepath = os.path.join(os.getcwd(), f"{year}/AoC_{day}/{year}AoC{day}_sample.txt")
filepath = os.path.join(os.getcwd(), f"{year}/AoC_{day}/{year}AoC{day}_input.txt")
data = open(filepath, "r").read().splitlines()


def part1(data):
    jolts = 0
    for batt in data:
        first = 0
        second = 0
        ifirst = 0
        for i in range(len(batt) - 1):
            if int(batt[i]) > first:
                first = int(batt[i])
                ifirst = i
        for j in range(ifirst + 1, len(batt)):
            if int(batt[j]) > second:
                second = int(batt[j])
        jolts += first * 10 + second
    return jolts


def part2(data):
    jolts = 0
    for batt in data:
        k = -1
        for i in range(12):  # for each digit
            max = 0
            for j in range(len(batt) + i - 12, np.max((k + 1, i)) - 1, -1):
                if int(batt[j]) >= max:
                    max = int(batt[j])
                    k = j
            jolts += max * 10 ** (11 - i)
    return jolts


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
