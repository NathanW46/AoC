import os
from datetime import datetime

def create_aoc_files():
    
    # Get the current date
    year = datetime.now().year
    day = datetime.now().day
    
    # Create the directory for AoC_{day}
    dir_name = f"{year}/AoC_{day}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


    # header to insert in py files
    header = f"""import os
from datetime import datetime
import numpy as np
import re

year = {year}
day = {day}""" + """
filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_sample.txt')
# filepath = os.path.join(os.getcwd(), f'{year}/AoC_{day}/2024AoC{day}_input.txt')"""


    # Create the files in the directory
    files = [
        f"{year}AoC{day}-1.py",
        f"{year}AoC{day}-2.py",
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

    print(f"Directory and files for {year} AoC {day} created successfully!")




create_aoc_files()