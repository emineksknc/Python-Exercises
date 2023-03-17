# 64. Write a Python program that retrieves the date and time of file creation and modification.

import os

import time

file_path = "1.py"

time_created = os.path.getctime(file_path)
time_modified = os.path.getmtime(file_path)

time_created = time.ctime(time_created)
time_modified = time.ctime(time_modified)

print(f"The file located at the path {file_path} was created at {time_created} and was last modified at {time_modified}")
