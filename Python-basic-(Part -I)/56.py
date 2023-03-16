#56. Write a Python program to get the height and width of the console window.

"""
Run from terminal :  python Python-basic-\(Part\ -I\)/56.py

Output (like) :
os.terminal_size(columns=80, lines=24)
"""

# importing os module
import os

# Get the size
# of the terminal
size = os.get_terminal_size()

# Print the size
# of the terminal
print(size)


