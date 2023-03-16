# 46. Write a Python program to retrieve the path and name of the file currently being executed.
"""
Output :
/home/emine/Desktop/Python-Exercises/Python-basic-(Part -I)/46.py
46.py
"""
import os

print(os.path.realpath(__file__))
print(os.path.basename(__file__))

