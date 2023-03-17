# 59. Write a Python program to convert height (in feet and inches) to centimeters.

"""
Referance: https://byjus.com/feet-to-centimeter-calculator/#:~:text=As%20we%20know%2C%201%20foot,61%20x%202.54%20%3D%20154.94%20cm
1 foot = 12 inches
1 inch = 2.54 cm
"""


def feet_to_meter(feet, inches=0):
    return ((feet * 12) + inches) * 2.54


print(feet_to_meter(feet=5, inches=10))
