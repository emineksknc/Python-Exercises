# 80. Write a Python program to get the current value of the recursion limit.

import sys

# Get Recursion Limit
print(sys.getrecursionlimit())

# Set Recursion Limit
sys.setrecursionlimit(10**6)
print(sys.getrecursionlimit())
