import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 6
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

def get_starting_pos(grid):
    return next(((i, row.index('^')) for i, row in enumerate(grid) if '^' in row), None)

def look(grid, pos, dir):
    x, y = pos
    
    dx, dy = dir
    nx, ny = x + dx, y + dy 

    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
        return "."
    elif nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
        return "oob" #out of bound
    return '#'

def move(grid, pos, dir):
    
    x, y = pos
    dx, dy = dir
    x, y = x + dx, y + dy
    return x, y



directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0



rows = open(filepath, 'r').read().split('\n')
grid = [list(row) for row in rows]
x,y = get_starting_pos(grid)


while 0 < x < len(grid) and 0 < y < len(grid[0]):
    
    match look(grid, (x,y), directions[dir]):
        case '.':
            grid[x][y] = 'X'
            x,y = move(grid, (x,y), directions[dir])
            # print(grid)
        case '#':
            dir = (dir+1) % 4
        case 'oob':
            dx, dy = directions[dir]
            grid[x][y] = 'X'
            x,y = x + dx, y + dy
        

print(sum(row.count('X') for row in grid)+1)


