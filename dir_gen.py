import os
from datetime import datetime

def create_aoc_files():
    
    # Get the current date
    while 1:
        x = input("Use Today's Data?(Y/N) ")
        
        if x == 'Y':
            year = datetime.now().year
            day = datetime.now().day
            break
        elif x == 'N':
            year = input("What Year? ")
            if not year.isdigit():
                print("Invalid Entry")
                continue
            day = input("What day? ")
            if not day.isdigit():
                print("Invalid Entry")
                continue
            break
        else:
            print("Invalid Entry")
        
    
    # Create the directory for AoC_{day}
    dir_name = f"{year}/AoC_{day}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    else:
        print(f"Directory for {year} AoC {day} already exists")


    # header to insert in py files
    header = f"""import os
import numpy as np
import re

year = {year}
day = {day}""" + """
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/{year}AoC{day}_sample.txt')
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/{year}AoC{day}_input.txt')"""


    # Create the files in the directory
    files = [
        f"{year}AoC{day}.py",
        f"{year}AoC{day}_input.txt",
        f"{year}AoC{day}_sample.txt"
    ]

    for file in files:
        file_path = os.path.join(dir_name, file)
        if not os.path.exists(file_path):
            if file.endswith('.py'):  # For Python files, insert the code
                with open(file_path, 'w') as f:
                    f.write(header)
            else:  
                open(file_path, 'w').close()  # Create empty text file
        else:
            print(f"{file_path} already exists")

    print(f"Directory and files for {year} AoC {day} created successfully!")




create_aoc_files()
