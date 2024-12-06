import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 3
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r').read().split('do')

total = 0

            
first_list = list(data[0])
while len(data[0]) != 0 and data[0][0] != '(':
            first_list.pop(0)
            data[0] = ''.join(first_list)


first = data[0].split('mul')
for s in first:
    if (s[0] == '('):
        nums = [int(match) for match in re.findall(r'\d+', s)]
        if len(nums) >= 2:
            i = len(str(nums[0])) + len(str(nums[1])) + 1
            if (s[i+1] == ')'):
                total += nums[0]*nums[1]
            




do = True

for s in data[1:]:
    if s[0:5] == "n't()":
        do = False
        continue
    elif s[0:2] == '()':
        do = True
        s_list = list(s)
        while len(s) != 0 and s[0] != '(':
            s_list.pop(0)
            s = ''.join(s_list)
    else:
        do = False
        continue
        
    for mul in s.split('mul'):
        
        if (mul[0] == '('):
            nums = [int(match) for match in re.findall(r'\d+', mul)]
            if len(nums) >= 2:
                i = len(str(nums[0])) + len(str(nums[1])) + 1
                if (mul[i+1] == ')'):
                    total += nums[0]*nums[1]


            
print(total)