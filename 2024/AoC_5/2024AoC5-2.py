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

def reorder(bad_updates, rules):
    reordered = []
    for i, update in enumerate(bad_updates):
        while not check(rules, update):
            for rule in rules:  
                if (rule[0] in update) and (rule[1] in update):
                    if (update.index(rule[0]) > update.index(rule[1])):
                        val = rule[0]
                        update.remove(val)
                        update.insert(update.index(rule[1]), val)
        reordered.append(update)      
    return reordered

def check(rules, update):
    valid = True
    for rule in rules:  
        if (rule[0] in update) and (rule[1] in update):
            if (update.index(rule[0]) > update.index(rule[1])):
                valid = False
    return valid


def filter_updates(rules, updates):

    bad_updates = []
    for i,update in enumerate(updates):
        bad = False
        for rule in rules:  
            if (rule[0] in update) and (rule[1] in update):
                if (update.index(rule[0]) > update.index(rule[1])):
                    bad = True
                    break

        if bad:
            bad_updates.append(update)


    return bad_updates


def get_total(valids):
    total = 0
    for i, update in enumerate(valids):
        total += update[len(update)//2]   

    return total   


rules, updates = get_data(filepath)
bads = filter_updates(rules, updates)
valids = reorder(bads, rules)

total = get_total(valids)
print(total)
