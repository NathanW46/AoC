import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 2
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')



data = open(filepath, 'r').read().split('\n')


result = 0
for row in data:
    buffer = 0
    safe = 0
    row = list(map(int, row.split(' ')))
    if (row[0] - row[1]) < 0:
        direction = 1
    elif (row[0] - row[1]) > 0:
        direction = -1
    else:
        if (row[1] - row[2]) < 0:
            direction = 1
        elif (row[1] - row[2]) > 0:
            direction = -1
        else:
            direction = 0
        
    for i in range(len(row)-1):
    
        match (direction):
            case 1:
                if -3 <= (row[i] - row[i+1]) < 0:
                    safe += 1
                elif buffer == 0:
                    buffer += 1
                    i += 1
                    safe += 1
                else:
                    safe -= 1

                    
            case -1:
                if 0 < (row[i] - row[i+1]) <= 3:
                    safe += 1
                    
                elif buffer == 0:
                    buffer += 1
                    safe += 1
                    
                else:
                    safe -= 1

            case _:
                continue
        
    if safe == len(row)-1:
        result += 1

            
            
            
        
        
        



print(result)