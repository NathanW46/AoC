import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 3
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r').read().split('mul')


total = 0
for mul in data:
    if mul[0] == '(':
        nums = [int(match) for match in re.findall(r'\d+', mul)]
        if len(nums) >= 2:
            i = len(str(nums[0])) + len(str(nums[1])) + 1
            if (mul[i+1] == ')'):
                total += nums[0]*nums[1]
            
print(total)