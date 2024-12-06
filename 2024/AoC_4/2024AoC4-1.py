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
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def search(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i*dx, y + i*dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or board[nx][ny] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                for dx, dy in directions:
                    if search(row, col, dx, dy):
                        total += 1
    return total





total = find_all_words(get_grid(filepath))

print(total)


