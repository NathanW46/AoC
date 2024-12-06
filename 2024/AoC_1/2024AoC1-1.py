import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 1
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r').read().split('\n')

left = []
right = []
for row in data:
    temp = row.split('   ')
    left.append(int(temp[0]))
    right.append(int(temp[1]))
left.sort()
right.sort()


sum = 0

for i in range(len(left)):
    sum += abs(left[i] - right[i])
    
print(sum)