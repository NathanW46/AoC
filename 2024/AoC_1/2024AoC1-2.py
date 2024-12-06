import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 1
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r').read().split('\n')

l = []
r = []
for row in data:
    temp = row.split('   ')

    l.append(int(temp[0]))
    r.append(int(temp[1]))

score = 0

stop = max([max(l), max(r)]) + 1

for i in np.arange(0, stop, 1):
    score += i * l.count(i) * r.count(i)
    
print(score)