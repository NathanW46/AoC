import numpy as np

filename = "2025AoC1_input.txt"
# filename='2025AoC1_sample.txt'


dial = 50
pswd = 0
pt2 = 0

with open(filename, "r") as file:
    for i in file:
        # if True:
        #     for i in test:
        old = dial
        # part 2

        pt2 += int(i[1:]) // 100
        n = int(i[1:]) % 100
        if i[0] == "L":
            dial -= int(n)
        elif i[0] == "R":
            dial += int(n)

        new = dial

        # part 1
        if not (0 < dial < 100) and old != 0:
            pt2 += 1
        dial %= 100
        if dial == 0:
            pswd += 1

print("part 1:", pswd, "\npart 2:", pt2)
