import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 4
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')



word = 'XMAS'



def get_grid(filepath):
    data = open(filepath, 'r').read().split('\n')
    grid = [list(row) for row in data]
    
    return np.array(grid)

def find_all_words(board):
    global word
    rows, cols = board.shape
    total = 0
    steps = [(1, -1), (1, -1), (-2, 0), (1, 1), (1, 1)]
    
    def search_for_MAS(x, y, steps, order):
        i = 1
        for step in steps:
            x, y = x + step[0], y + step[1]

            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != order[i]:
                return False
            i+=1
        return True

    possibilities = 'MASMAS', 'MASSAM', 'SAMMAS', 'SAMSAM'

    for row in range(rows):
        for col in range(cols):
            for word in possibilities:
                if board[row][col] == word[0]:
                    if search_for_MAS(row, col, steps, word):
                        total += 1

    return total





total = find_all_words(get_grid(filepath))

print(total)


