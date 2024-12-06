import os
from datetime import datetime
import numpy as np
import re

year = 2024
day = 5
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')




def get_data(filepath):
    data = open(filepath, 'r').read().split('\n\n')
    rules = [[int(x) for x in rule.split('|')] for rule in data[0].split('\n')]
    updates = [[int(x) for x in update.split(',')] for update in data[1].split('\n')]
    return rules, updates




def filter_updates(rules, updates):

    valid_updates = []
    for i,update in enumerate(updates):
        valid = True
        for rule in rules:  
            if (rule[0] in update) and (rule[1] in update):
                if (update.index(rule[0]) > update.index(rule[1])):
                    valid = False
                    break

        if valid:
            valid_updates.append(update)


        
        
        
    return valid_updates


def get_total(valids):
    total = 0
    for i, update in enumerate(valids):
        total += update[len(update)//2]   

    return total   



valids = filter_updates(*get_data(filepath))


print(get_total(valids))
