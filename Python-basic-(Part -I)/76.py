# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

"""
Run this script from command prompt or terminal:

> python 76.py 2 3 5 6

"""
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers
mul = 1
# Using argparse module
for i in range(1, n):
    mul *= int(sys.argv[i])

print("\n\nResult:", mul)