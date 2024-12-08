import os
from datetime import datetime
import numpy as np
import re
from itertools import product

year = 2024
day = 7
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')

data = open(filepath, 'r').read().replace(':','').split('\n')
data = [[int(val) for val in row.split(' ')] for row in data]

def gen_ops(len):
    return [list(op) for op in product(['+', '*'], repeat=len)]


def evaluate(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i+1]
        elif op == '*':
            result *= nums[i+1]
    return result


# def evaluate(nums, ops):
#     expression = [x for pair in zip(nums, ops) for x in pair]
#     expression.append(nums[-1])
#     expression = ''.join(expression)
#     print(expression)
#     return eval(expression)


data
total = 0
result = 0




for i,row in enumerate(data):
    target = int(row[0])
    ops = gen_ops(len(row) - 2)
    for op in ops:
        total = evaluate(row[1:], op)
        if total == target:
            result += row[0]
            break


print(result)