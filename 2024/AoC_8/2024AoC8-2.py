import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 8
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r' ).read().split('\n')
data = [list(row) for row in data]
rows, cols = len(data), len(data[0])

map = [['.' for _ in range(rows)] for _ in range(cols)] 



def get_nodes(data, char):
    indices = []
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if element == char:
                indices.append((i, j))
    return indices

def get_uniq(data):
    chars = []
    for row in data:
        for char in row:
            if char not in chars and char !='.':
                chars.append(char)
    return chars


def find_antinodes(map, nodes):
    rows, cols = len(map), len(map[0])
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):

                difference = tuple(nodes[j][k] - nodes[i][k] for k in range(2))
                antinode = tuple(nodes[i][k] - difference[k] for k in range(2))
                
                n = 2
                while 0 <= antinode[0] < rows and 0 <=  antinode[1] < cols:
                    map[antinode[0]][antinode[1]] = '#'
                    antinode = tuple(nodes[i][k] - difference[k]*n for k in range(2))
                    n += 1
                    
                antinode = tuple(nodes[i][k] + difference[k] for k in range(2))
                m = 2
                while 0 <= antinode[0] < rows and 0 <=  antinode[1] < cols:
                    map[antinode[0]][antinode[1]] = '#'
                    antinode = tuple(nodes[i][k] + difference[k]*m for k in range(2))
                    m += 1

                    
    return map

chars = get_uniq(data)

for char in chars:
    nodes = get_nodes(data, char)
    if len(nodes) > 1:
        for node in nodes:
            map[node[0]][node[1]] = '#'
    map = find_antinodes(map, nodes)

antinodes = get_nodes(map, '#')
print(len(antinodes))
