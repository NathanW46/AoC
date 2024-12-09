import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 9
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')


map =  open(filepath, 'r').read()

files = list(map[::2])
free = list(map[1::2])



def get_checksum(data):
    total = 0
    for i, char in enumerate(data):
        total += i * int(char)

    return total




    
def reorder(data):
    for i in range(len(data)-1, 0, -1):
        while '.' in data:
            if data[i] != '.':
                j = data.index('.')
                data[j] = data[i] 
            data.pop()
            i -= 1
    return data



def process(files, free):
    data = []
    for i, num in enumerate(files):
        for j in range(int(num)):
            data.append(str(i))
            
            
        if i != len(free):
            for j in range(int(free[i])):
                data.append('.')

    return data

data = process(files, free)
data = reorder(data)
print(get_checksum(data))