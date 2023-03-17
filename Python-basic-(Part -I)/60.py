# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.

"""


long    ||\\
edge    || \\
        ||  \\  hypotenuse
        ||   \\
        =======
        short
        edge
"""
import math


def calculate_hypotenuse(le, se):
    hypotenuse = math.sqrt(le ** 2 + se ** 2)
    return hypotenuse


print("/****** CALCULATE HYPOTENUSE ******/")

long_edge = float(input("Give a long edge : "))
short_edge = float(input("Give a short edge : "))

print("Hypotenuse : ", calculate_hypotenuse(long_edge, short_edge))
