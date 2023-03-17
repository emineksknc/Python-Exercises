# 71. Write a Python program to get a directory listing, sorted by creation date.

import os
import pathlib
import time

# Get file names from a directory
files = [os.path.abspath(file) for file in os.listdir("../Python-basic-(Part -I)")]

# Sort files
sorted_files = sorted(files, key=os.path.getctime)

# Print Results
[print(time.ctime(os.path.getctime(file)), os.path.basename(file)) for file in sorted_files]

